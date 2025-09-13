import type { Logger } from 'winston';
import { ConfigService } from '@nestjs/config';
import type { INestApplication } from '@nestjs/common';
import { NestFactory } from '@nestjs/core';
import { createNatsTransport } from '@desen-web/common/modules/rpc.module';
import {
  ConsoleLoggerModule,
  LOGGER_SERVICE,
  LOGGER_SERVICE_PROVIDER,
} from '@desen-web/common/modules/logger.module';
import { shutdown } from '@desen-web/common/utils/shutdown.util';
import { AppModule } from '@desen-web/users/infrastructure/nest/modules/app.module';

let app: INestApplication = null;
declare const _BUILD_INFO_: any;

async function bootstrap() {
  // Bootstrap the microservice (load all submodules).
  app = await NestFactory.create(AppModule, {
    logger: new ConsoleLoggerModule(),
  });

  // Get nats client configuration.
  const configService = app.get(ConfigService);
  const appPort = configService.get<number>('APP_PORT', 3000);
  const logger: Logger = app.get(LOGGER_SERVICE);

  // Set default logger.
  app.useLogger(app.get(LOGGER_SERVICE_PROVIDER));

  // Log build info.
  logger.info('Build info.', { info: _BUILD_INFO_ });

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

bootstrap().catch((error) => shutdown(app, error));
