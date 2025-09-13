import { Logger } from 'winston';
import {
  Injectable,
  NestInterceptor,
  ExecutionContext,
  CallHandler,
} from '@nestjs/common';
import { Observable, catchError, tap } from 'rxjs';
import { DefaultEvent, DefaultEventEmitter } from '../helpers/event.helper';
import {
  InjectNatsService,
  NatsService,
  NatsContext,
} from '../modules/rpc.module';
import { NotImplementedException } from '../exceptions/not_implemented.exception';
import { NullPointerException } from '../exceptions/null_pointer.exception';
import { ProtocolType } from '../helpers/protocol.helper';

/**
 * Fire events to kafka after next handler.
 */
export class NatsEventEmitter implements DefaultEventEmitter {
  /**
   * Store events to be sent to kafka after next handler.
   */
  private readonly events: DefaultEvent[] = [];

  /**
   * Default constructor.
   *
   * @param logger Logger instance.
   * @param kafkaService Service to access kafka.
   */
  constructor(
    private readonly logger: Logger,
    private readonly kafkaService: NatsService,
  ) {
    this.logger = logger.child({ context: NatsEventEmitter.name });
  }

  /**
   * Fire event to kafka.
   * @param event Nats event.
   */
  emit(event: DefaultEvent) {
    this.logger.debug('Fired event.', { event });
    // Sanity check.
    if (!event.name) {
      this.logger.error('Event name is required.');
    }
    this.events.push(event);
  }

  /**
   * Fire event to kafka.
   */
  async fireEvents() {
    if (!this.events.length) {
      this.logger.debug('No events to fire.');
      return;
    }

    const chunk = (arr: DefaultEvent[], size: number) =>
      Array.from({ length: Math.ceil(arr.length / size) }, (v, i) =>
        arr.slice(i * size, i * size + size),
      );

    const eventChunks = chunk(this.events, 100);
    let count = 0;

    for (const eventChunk of eventChunks) {
      this.logger.debug(
        `Firing events page ${++count} of ${eventChunks.length}`,
      );

      const eventsPromise = await Promise.allSettled(
        eventChunk.map((event) =>
          this.kafkaService.emit(event.name, event.data),
        ),
      );

      eventsPromise.forEach((event, i) => {
        if (event.status === 'fulfilled') {
          this.logger.debug('Nats event fired.', { event: this.events[i] });
        } else {
          this.logger.error('Nats event NOT fired.', {
            event: this.events[i],
            reason: event.reason,
          });
        }
      });

      await new Promise((resolve) => setTimeout(resolve, 100));
    }
  }
}

/**
 * Intercepts all events fired and send it to kafka.
 */
@Injectable()
export class NatsEventInterceptor implements NestInterceptor {
  constructor(
    @InjectNatsService() private readonly kafkaService: NatsService,
  ) {}

  async intercept(
    context: ExecutionContext,
    next: CallHandler,
  ): Promise<Observable<any>> {
    // Get request.
    let request: any = null;

    const protocol = context.getType();
    if (protocol === ProtocolType.HTTP) {
      const ctx = context.switchToHttp();
      request = ctx.getRequest();
    } else if (protocol === ProtocolType.RPC) {
      const ctx = context.switchToRpc();
      request = ctx.getContext<NatsContext>();
    } else {
      throw new NotImplementedException(
        `Protocol ${protocol} is not implemented.`,
      );
    }

    // Sanity check!
    if (!request.logger) {
      throw new NullPointerException(
        'Request logger is not defined. Check if LoggerInterceptor is available.',
      );
    }

    // Create a local logger instance.
    const logger = request.logger.child({
      context: NatsEventInterceptor.name,
    });

    // All events fired by request will be sent to kafka.
    const emitter = new NatsEventEmitter(logger, this.kafkaService);

    logger.debug('Nats emitter created.');

    // Store event emitter to be used by nest controllers.
    request.emitter = emitter;

    // If there is no transaction created...
    if (!request.transaction?.afterCommit) {
      // Call next handler and fire event after that.
      return next.handle().pipe(
        tap(async () => {
          logger.debug('Firing kafka events after handler.');
          return emitter.fireEvents();
        }),
        catchError(async (err) => {
          logger.debug('Nats events not fired after handler.');
          throw err;
        }),
      );
    }

    // Fire events to kafka after database commit.
    request.transaction.afterCommit(() => {
      logger.debug('Firing kafka events after database commit.');
      return emitter.fireEvents();
    });

    return next.handle();
  }
}
