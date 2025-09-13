import type { Logger } from 'winston';
import type { INestApplicationContext } from '@nestjs/common';
import { LOGGER_SERVICE } from '../modules/logger.module';

export async function shutdown(app?: INestApplicationContext, error?: Error) {
  const logger = app?.get<Logger>(LOGGER_SERVICE) ?? console;

  logger.info('Shutting down Nest app...');

  if (error) {
    logger.error(`Uncaught exception error: ${error.message}\n${error.stack}`);
  }

  app?.flushLogs();
  await app?.close();

  logger.info('Goodbye cruel world!');

  process.exit(error ? -1 : 0);
}
