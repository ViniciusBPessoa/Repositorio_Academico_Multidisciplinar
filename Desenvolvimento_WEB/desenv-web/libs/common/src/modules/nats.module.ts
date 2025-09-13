import { readFileSync, existsSync } from 'node:fs';
import { isBoolean, isNumber } from 'class-validator';
import { Milliseconds } from 'cache-manager';
import { Logger } from 'winston';
import {
  DynamicModule,
  Inject,
  Injectable,
  OnModuleDestroy,
  OnModuleInit,
} from '@nestjs/common';
import { ConfigModule, ConfigService } from '@nestjs/config';
import {
  Transport,
  MessagePattern,
  EventPattern,
  ClientNats,
  NatsOptions,
  ClientProxyFactory,
} from '@nestjs/microservices';
import { NatsConnection } from 'nats';
import { TimeoutError, lastValueFrom, timeout } from 'rxjs';
import { NATS_CLIENT, NATS_SERVICE } from './nats.constants';
import { InjectLogger, LOGGER_SERVICE, LoggerModule } from './logger.module';
import { DefaultException } from '../helpers/error.helper';
import {
  NullPointerException,
  MissingEnvVarException,
  NotLoadedNatsServiceException,
  TimeoutException,
} from '../exceptions';

export interface NatsCoreConfig {
  APP_NAME: string;
  APP_NATS_SERVERS: string;
  APP_NATS_SUBJECTS: string;
  APP_NATS_SUBJECT_PREFIX: string;
  APP_NATS_ENABLE_TLS: string;
  APP_NATS_KEY_FILE: string;
  APP_NATS_CERT_FILE: string;
  APP_NATS_CA_FILE: string;
  APP_NATS_HANDSHAKE_FIRST: string;
  APP_NATS_DELIVERY_POLICY: string;
  APP_NATS_DELIVER_GROUP: string;
  APP_NATS_DELIVER_TO: string;
  APP_NATS_MANUAL_ACK: string;
  APP_NATS_ACK_POLICY: string;
  APP_NATS_ENABLE_REQUEST_ID_AS_KEY: string;
  APP_NATS_SEND_TIMEOUT: string;
  APP_NATS_EMIT_TIMEOUT: string;
  APP_NATS_QUEUE_GROUP: string;
}

export const InjectNatsService = () => Inject(NATS_SERVICE);

const NATS_CORE_TRANSPORT = Transport.NATS;

type DeliverPolicy =
  | 'All'
  | 'Last'
  | 'New'
  | 'ByStartSequence'
  | 'ByStartTime'
  | 'last_per_subject';

type AckPolicy = 'Explicit' | 'All' | 'None';

function createNatsCoreOptions(
  configService: ConfigService<NatsCoreConfig>,
  /* eslint-disable @typescript-eslint/no-unused-vars */
  logger: Logger,
): NatsOptions {
  const appServers = configService.get<string>('APP_NATS_SERVERS');
  if (!appServers) {
    throw new MissingEnvVarException(['APP_NATS_SERVERS']);
  }

  const appName = configService.get<string>('APP_NAME', 'no-app-name');
  const deliverPolicy = configService.get<DeliverPolicy>(
    'APP_NATS_DELIVERY_POLICY',
    'All',
  );
  const deliverGroup = configService.get<string>('APP_NATS_DELIVER_GROUP');
  if (!deliverGroup) {
    throw new MissingEnvVarException(['APP_NATS_DELIVER_GROUP']);
  }

  const deliverTo = configService.get<string>('APP_NATS_DELIVER_TO');
  if (!deliverTo) {
    throw new MissingEnvVarException(['APP_NATS_DELIVER_TO']);
  }

  const manualAck =
    configService.get<string>('APP_NATS_MANUAL_ACK', 'false') === 'true';
  const ackPolicy = configService.get<AckPolicy>(
    'APP_NATS_ACK_POLICY',
    'Explicit',
  );

  const queueGroup = configService.get<string>('APP_NATS_QUEUE_GROUP');
  if (!queueGroup) {
    throw new MissingEnvVarException(['APP_NATS_QUEUE_GROUP']);
  }

  const natsOptions: NatsOptions = {
    options: {
      name: appName,
      servers: appServers,
      queue: queueGroup,
      deliverPolicy,
      deliverGroup,
      deliverTo,
      ackPolicy,
      manualAck,
    },
  };

  const enableTls =
    configService.get<string>('APP_NATS_ENABLE_TLS', 'false') === 'true';

  if (enableTls) {
    const keyFile = configService.get<string>('APP_NATS_KEY_FILE', null);
    const certFile = configService.get<string>('APP_NATS_CERT_FILE', null);
    const caFile = configService.get<string>('APP_NATS_CA_FILE', null);

    const handshakeFirst =
      configService.get<string>('APP_NATS_HANDSHAKE_FIRST', 'true') === 'true';

    const isSafeTLS =
      existsSync(keyFile) && existsSync(certFile) && existsSync(caFile);

    if (isSafeTLS) {
      // Load https certificates.
      natsOptions.options.tls = {
        handshakeFirst,
        keyFile: readFileSync(keyFile).toString(),
        certFile: readFileSync(certFile).toString(),
        caFile: readFileSync(caFile).toString(),
      };
    }
  }

  return natsOptions;
}

export function createNatsTransport(
  configService: ConfigService<NatsCoreConfig>,
  logger: Logger,
): NatsOptions {
  const natsOptions: NatsOptions = createNatsCoreOptions(configService, logger);

  return {
    transport: NATS_CORE_TRANSPORT,
    options: natsOptions.options,
  };
}

export const NatsClientProvider = {
  provide: NATS_CLIENT,
  inject: [ConfigService, LOGGER_SERVICE],
  useFactory: async (
    configService: ConfigService<NatsCoreConfig>,
    logger: Logger,
  ) => {
    return ClientProxyFactory.create(
      createNatsTransport(configService, logger),
    );
  },
};

function applyPrefix(prefix: string, subject: string) {
  if (!prefix) return subject;

  return `${prefix}.${subject}`;
}

@Injectable()
export class NatsService implements OnModuleInit, OnModuleDestroy {
  /**
   * Nats Connection useful for drain
   */
  private nc: NatsConnection;

  /**
   * Created and subscribed subjects.
   */
  private static readonly subjects: string[] = [];

  /**
   * Created and subscribed events.
   */
  private static readonly events: string[] = [];

  /**
   * Subject prefix.
   */
  private readonly subjectPrefix: string;

  /**
   * Enable requestId as Key.
   */
  private readonly enableRequestIdAsKey: boolean;

  /**
   * Nats send timeout in milliseconds.
   */
  private readonly natsSendTimeout?: Milliseconds;

  /**
   * Nats emit timeout in milliseconds.
   */
  private readonly natsEmitTimeout?: Milliseconds;

  /**
   * Default constructor.
   * @param clientNats Nats client.
   * @param configService environment configuration.
   * @param logger Global logger.
   */
  constructor(
    @Inject(NATS_CLIENT) private readonly clientNats: ClientNats,
    configService: ConfigService<NatsCoreConfig>,
    @InjectLogger() private readonly logger: Logger,
  ) {
    this.logger = logger.child({ context: NatsService.name });

    this.enableRequestIdAsKey =
      configService.get<string>(
        'APP_NATS_ENABLE_REQUEST_ID_AS_KEY',
        'false',
      ) === 'true';

    const natsSendTimeout = configService.get<string>('APP_NATS_SEND_TIMEOUT');
    this.natsSendTimeout = natsSendTimeout && Number(natsSendTimeout);

    const natsEmitTimeout = configService.get<string>('APP_NATS_EMIT_TIMEOUT');
    this.natsEmitTimeout = natsEmitTimeout && Number(natsEmitTimeout);

    this.subjectPrefix = configService.get<string>(
      'APP_NATS_SUBJECT_PREFIX',
      null,
    );
  }

  async onModuleInit(): Promise<void> {
    // Connect to NATS-Server.
    this.nc = await this.clientNats.connect();
  }

  async onModuleDestroy(): Promise<void> {
    if (this.nc && !this.nc.isClosed()) {
      await this.nc.drain();
      await this.clientNats?.close();
    }
  }

  static getSubjects(): string[] {
    return NatsService.subjects;
  }

  /**
   * Add subjects to subjects list.
   * @param subjects The subjects to fill in class subjects.
   */
  static subscribe(subjects: string[] | string): void {
    if (!Array.isArray(subjects)) {
      subjects = [subjects];
    }

    const filteredSubjects = subjects.filter(
      (subject) => !this.subjects.includes(subject),
    );
    for (const subject of filteredSubjects) {
      this.subjects.push(subject);
    }
  }
  subscribe(subjects: string[] | string): void {
    NatsService.subscribe(subjects);
  }

  /**
   * Add subjectPrefix to subject.
   * @param subject Subject to add a prefix.
   * @returns Subject with prefix.
   */
  private getSubjectPrefix(subject: string): string {
    return applyPrefix(this.subjectPrefix, subject);
  }

  /**
   * Add events to stream list.
   * @param events The event to add in stream.
   */
  static createEvents(events: string[] | string): void {
    if (!Array.isArray(events)) {
      events = [events];
    }

    const filteredEvents = events.filter(
      (event) => !this.events.includes(event),
    );
    for (const event of filteredEvents) {
      this.events.push(event);
    }
  }

  /**
   * Add events to stream list.
   * @param events The event to add in stream.
   */
  createEvents(events: string[] | string): void {
    NatsService.createEvents(events);
  }

  /**
   * Proxy send function to client Nats.
   * @param pattern Subject name.
   * @param data Message data.
   * @returns Reply message.
   */
  async send<TResult = any, TInput = any>(
    pattern: any,
    data: TInput,
  ): Promise<TResult> {
    // Sanity check.
    if (!pattern) {
      throw new NullPointerException('Pattern is required.');
    }

    let logger = this.logger;

    // Apply subject prefix.
    pattern = this.getSubjectPrefix(pattern);

    // Set Headers.
    if (data?.['headers']) {
      const headers: { [key: string]: any } = {};
      if (data?.['headers']?.['requestId']) {
        const requestId = data['headers']['requestId'];
        logger = logger.child({ loggerId: requestId });

        if (this.enableRequestIdAsKey) {
          headers['key'] = requestId;
        }
      }
    }

    try {
      // If the 'query' property exists in the payload, log the message without including 'data'.
      if (!data?.['value']?.['query']) {
        logger.debug('Send nats message.', { pattern, data });
      } else {
        logger.debug('Send nats message.', { pattern });
      }

      // Call microservice.
      const source = !isNumber(this.natsSendTimeout)
        ? this.clientNats.send<TResult, TInput>(pattern, data)
        : this.clientNats
            .send<TResult, TInput>(pattern, data)
            .pipe(timeout(this.natsSendTimeout));

      const result = await lastValueFrom(source);

      logger.debug('Replied nats message.', { result });

      return result['value'];
    } catch (error) {
      logger.error('Received nats error message.', error);

      if (error instanceof TimeoutError) {
        throw new TimeoutException(error.message);
      }

      if (
        'code' in error &&
        DefaultException.registeredExceptions[error.code]
      ) {
        const RegisteredException: any =
          DefaultException.registeredExceptions[error.code];

        const exception: DefaultException = new RegisteredException();
        exception.data = error.data;
        exception.causedByStack = error.causedByStack;

        throw exception;
      }
      if (
        error.message?.includes(
          'The client consumer did not subscribe to the corresponding reply subject',
        )
      ) {
        const exception = new NotLoadedNatsServiceException(pattern);
        exception.causedByStack = [error.stack];

        throw exception;
      }

      throw new DefaultException(error);
    }
  }

  /**
   * Proxy emit function to client Nats.
   * @param pattern Subject name.
   * @param data Event data.
   * @returns Reply message.
   */
  async emit<TResult = any, TInput = any>(
    pattern: any,
    data: TInput,
  ): Promise<TResult> {
    // Sanity check.
    if (!pattern) {
      throw new NullPointerException('Pattern is required.');
    }

    let logger = this.logger;

    pattern = this.getSubjectPrefix(pattern);

    try {
      // Get logger id.
      if (data?.['headers']?.['requestId']) {
        const headers = data['headers'];
        logger = logger.child({ loggerId: headers.requestId });
        if (this.enableRequestIdAsKey) {
          data['key'] = headers.requestId;
        }
      }

      logger.debug('Fire Nats event.', { pattern, data });

      const source = !isNumber(this.natsEmitTimeout)
        ? this.clientNats.emit<TResult, TInput>(pattern, data)
        : this.clientNats
            .emit<TResult, TInput>(pattern, data)
            .pipe(timeout(this.natsEmitTimeout));

      const result = await lastValueFrom(source);

      logger.debug('Replied Nats event.', { result });

      return result;
    } catch (error) {
      logger.error('Received nats error event.', error);

      throw new DefaultException(error);
    }
  }

  /**
   * Not needed for nats, just to maintain compatibility
   */
  async createTopics(
    patterns: string[] = [],
    events: string[] = [],
  ): Promise<void> {
    return;
  }
}

export const NatsServiceInjectProvider = {
  provide: NATS_SERVICE,
  useExisting: NatsService,
};

@Injectable()
class GlobalNatsService {
  constructor(natsService: NatsService) {
    NatsModule.natsService = natsService;
  }
}

export class NatsModule {
  static natsService: NatsService;
  static readonly services: any = {};

  static forFeature(services: any[] = []): DynamicModule {
    for (const service of services) {
      this.services[service.name] = service;
      NatsService.subscribe(service._services ?? []);
    }

    return {
      module: NatsModule,
      imports: [ConfigModule, LoggerModule],
      providers: [
        NatsClientProvider,
        NatsService,
        GlobalNatsService,
        NatsServiceInjectProvider,
      ],
      exports: [NatsClientProvider, NatsService, NatsServiceInjectProvider],
    };
  }

  static getService(ctor: RemoteNatsServiceConstructor): boolean {
    // Check if this ctor is already verified.
    if (isBoolean(ctor._cacheVerify)) {
      return ctor._cacheVerify;
    }

    // If not, check ctor name in service list.
    if (this.services[ctor.name]) {
      ctor._cacheVerify = true;
      return true;
    }

    // If not, check if this ctor has services in service list
    // and save the verify value on _cacheVerify.
    ctor._cacheVerify =
      !!ctor._services?.length &&
      ctor._services.every((service) => this.services[service.name]);
    return ctor._cacheVerify;
  }

  static createRemoteService(
    ctor: RemoteNatsServiceConstructor,
    requestId: string,
    logger: Logger,
    natsService: NatsService,
  ) {
    if (!this.getService(ctor)) {
      throw new NotLoadedNatsServiceException(ctor.name);
    }

    return new ctor(requestId, logger, natsService);
  }
}

export const NatsAddService = (services: string[] | string) => {
  /* eslint-disable @typescript-eslint/no-empty-object-type */
  return <T extends { new (...args: any[]): {} }>(className: T) => {
    const newClass = class extends className {
      static readonly _services: string[] = Array.isArray(services)
        ? services
        : [services];
    };
    // Only to keep the original class name.
    Object.defineProperty(newClass, 'name', { value: className.name });
    return newClass;
  };
};

export const NatsAddEvent = (events: string[] | string) => {
  /* eslint-disable @typescript-eslint/no-empty-object-type */
  return <T extends { new (...args: any[]): {} }>(className: T) => {
    NatsService.createEvents(events);
  };
};

const SUBJECT_PREFIX = process.env.APP_NATS_SUBJECT_PREFIX;

export function NatsMessagePattern(pattern: string): MethodDecorator {
  pattern = applyPrefix(SUBJECT_PREFIX, pattern);
  return MessagePattern(pattern, NATS_CORE_TRANSPORT);
}

export function NatsEventPattern(pattern: string): MethodDecorator {
  pattern = applyPrefix(SUBJECT_PREFIX, pattern);
  return EventPattern(pattern, NATS_CORE_TRANSPORT);
}

export interface RemoteNatsService {
  requestId: string;
  logger: Logger;
  natsService: NatsService;
}

interface RemoteNatsServiceConstructor {
  _services?: any[];
  _cacheVerify?: boolean;

  new (
    requestId: string,
    logger: Logger,
    natsService: NatsService,
  ): RemoteNatsService;
}
