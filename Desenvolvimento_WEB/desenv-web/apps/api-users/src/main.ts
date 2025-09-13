import { readFileSync, existsSync } from 'node:fs';
import type {
  NestApplicationOptions,
  INestApplication,
  ValidationError,
} from '@nestjs/common';
import {
  ValidationPipe,
  VersioningType,
  VERSION_NEUTRAL,
} from '@nestjs/common';
import { NestFactory, Reflector } from '@nestjs/core';
import { ConfigService } from '@nestjs/config';
import type { SwaggerCustomOptions } from '@nestjs/swagger';
import { SwaggerModule, DocumentBuilder } from '@nestjs/swagger';
import type { Logger } from 'winston';
import helmet from 'helmet';
import {
  createNatsTransport,
  NatsService,
} from '@desen-web/common/modules/rpc.module';
import {
  DefaultExceptionFilter,
  HttpExceptionFilter,
} from '@desen-web/common/filters/exception.filter';
import { HttpLoggerInterceptor } from '@desen-web/common/interceptors/http_logger.interceptor';
import { ResponseInterceptor } from '@desen-web/common/interceptors/response.interceptor';
import { LoggerInterceptor } from '@desen-web/common/interceptors/logger.interceptor';
import { RequestIdInterceptor } from '@desen-web/common/interceptors/request_id.interceptor';
import { ValidationException } from '@desen-web/common/exceptions/validation.exception';
import {
  ConsoleLoggerModule,
  LOGGER_SERVICE,
  LOGGER_SERVICE_PROVIDER,
} from '@desen-web/common/modules/logger.module';
import { ExceptionInterceptor } from '@desen-web/common/interceptors/exception.interceptor';
import { shutdown } from '@desen-web/common/utils/shutdown.util';
import { AppModule } from '@desen-web/api-users/infrastructure/nest/modules/app.module';
import { NatsServiceInterceptor } from '@desen-web/common/interceptors/nats_service.interceptor';

const HTTPS_KEY_FILE = process.env.APP_HTTPS_KEY_FILE;
const HTTPS_CERT_FILE = process.env.APP_HTTPS_CERT_FILE;

let app: INestApplication = null;
declare const _BUILD_INFO_: any;

async function bootstrap() {
  const appOptions: NestApplicationOptions = {
    logger: new ConsoleLoggerModule(),
    cors: true,
  };

  const IS_HTTPS = existsSync(HTTPS_KEY_FILE) && existsSync(HTTPS_CERT_FILE);
  if (IS_HTTPS) {
    // Load https certificates
    appOptions.httpsOptions = {
      key: readFileSync(HTTPS_KEY_FILE),
      cert: readFileSync(HTTPS_CERT_FILE),
    };
  }

  // Bootstrap the microservice (load all submodules).
  app = await NestFactory.create(AppModule, appOptions);

  app.enableVersioning({
    type: VersioningType.URI,
    defaultVersion: VERSION_NEUTRAL,
  });

  const logger = app.get<Logger>(LOGGER_SERVICE);
  const configService = app.get(ConfigService);
  const natsService = app.get(NatsService);
  const reflector = app.get(Reflector);
  const appPort = configService.get<number>('APP_PORT', 3000);
  const appEnv = configService.get<string>('APP_ENV', 'local');

  // Build OpenAPI server.
  if (appEnv !== 'production') openapi();

  // Set default logger.
  app.useLogger(app.get(LOGGER_SERVICE_PROVIDER));

  // Log build info.
  logger.info('Build info.', { info: _BUILD_INFO_ });

  // Set default interceptors.
  app.useGlobalInterceptors(
    new RequestIdInterceptor(),
    new LoggerInterceptor(logger),
    new HttpLoggerInterceptor(logger),
    new NatsServiceInterceptor(natsService),
    new ResponseInterceptor(reflector),
    new ExceptionInterceptor(logger),
  );

  // Set default filters.
  app.useGlobalFilters(
    new DefaultExceptionFilter(logger),
    new HttpExceptionFilter(logger),
  );

  // Set default pipes.
  app.useGlobalPipes(
    new ValidationPipe({
      whitelist: true,
      forbidNonWhitelisted: true,
      exceptionFactory: (errors: ValidationError[]) => {
        return new ValidationException(errors);
      },
    }),
  );

  // Use helmet and metrics path.
  app.use(helmet());

  // Enable graceful shutdown
  app.enableShutdownHooks();

  await app.init();

  // Client for all microservices.
  const service = app.connectMicroservice(
    createNatsTransport(configService, logger),
  );

  await service.listen();

  await app.listen(appPort);

  logger.info('Microservice HTTP successfully started.', { appPort });
}

function openapi() {
  const config = new DocumentBuilder()
    .setTitle('Users API GATEWAY')
    .setDescription('API Gateway for users')
    .setVersion(_BUILD_INFO_.package.version)
    .setContact(
      _BUILD_INFO_.package.name,
      _BUILD_INFO_.package.url,
      _BUILD_INFO_.package.email,
    )
    .setLicense('All rights reserved', _BUILD_INFO_.package.url)
    .addBearerAuth()
    .build();

  const document = SwaggerModule.createDocument(app, config);
  const customOptions: SwaggerCustomOptions = {
    customSiteTitle: 'Users API GATEWAY',
    swaggerOptions: { persistAuthorization: true },
  };

  SwaggerModule.setup('api', app, document, customOptions);
}

bootstrap().catch((error) => shutdown(app, error));
