import { Logger } from 'winston';
import { v4 as uuidV4 } from 'uuid';
import { NextFunction } from 'express';
import { Injectable, NestMiddleware } from '@nestjs/common';
import { InjectLogger } from '../modules/logger.module';

@Injectable()
export class RequestIdMiddleware implements NestMiddleware {
  /**
   * Default constructor.
   * @param logger Global logger
   */
  constructor(@InjectLogger() private readonly logger: Logger) {
    this.logger = logger.child({ context: RequestIdMiddleware.name });
  }

  /**
   * Intercepts request and add an id to the request.
   * @param request HTTP request.
   * @param response HTTP response.
   * @param next Next function.
   */
  use(request: any, response: any, next: NextFunction) {
    // If there is no request id, then create a new one.
    request.id = request.id ?? uuidV4();

    const logger = this.logger.child({ loggerId: request.id });
    logger.debug('Added request ID.', { requestId: request.id });

    // Go to next middleware on pipeline.
    next();
  }
}
