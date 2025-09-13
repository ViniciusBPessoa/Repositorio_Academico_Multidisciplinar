import {
  CallHandler,
  ExecutionContext,
  HttpStatus,
  Injectable,
  NestInterceptor,
} from '@nestjs/common';
import { Logger } from 'winston';
import { catchError, tap } from 'rxjs/operators';
import { InjectLogger } from '../modules/logger.module';
import { ExceptionTypes } from '../helpers/error.constants';

@Injectable()
export class HttpLoggerInterceptor implements NestInterceptor {
  constructor(@InjectLogger() private readonly logger: Logger) {
    this.logger = logger.child({ context: HttpLoggerInterceptor.name });
  }

  intercept(context: ExecutionContext, next: CallHandler) {
    const req = context.switchToHttp().getRequest();
    const { id, ip, originalUrl, method, headers, params, query, body, path } =
      req;
    const userAgent = req.get('user-agent') || 'NO_AGENT';

    // Prefer request logger instance.
    const logger = (req.logger ?? this.logger).child({
      context: HttpLoggerInterceptor.name,
    });

    const request: any = {
      id,
      method,
      originalUrl,
      userAgent,
      ip,
      path,
    };

    // FIXME: Adicionar um metadata nos controllers para indicar a remocao do log.
    const protectedUlrs = originalUrl.startsWith('/auth');

    // Exclude sensitive information from log.
    if (!protectedUlrs) {
      request.params = params;
      request.body = body;
      request.query = query;
    }

    if (req.user) {
      request.userId = req.user.uuid ?? req.user.id ?? req.user.email;
      request.userApiId = req.user.apiId;
    }

    request.headers = {
      ...headers,
      authorization: 'Protected',
      cookie: 'Protected',
    };

    const userId: string = request.userId ?? '-';
    const clientIp: string = ip;

    logger.info(
      `REQ: ${id} <| ${userId} |> | ${method} ${originalUrl} - ${userAgent} ${clientIp}`,
      { request },
    );

    const start = Date.now();

    return next.handle().pipe(
      tap((data) => {
        const res = context.switchToHttp().getResponse();
        const { statusCode } = res;
        const elapsedTime = Date.now() - start;

        const response: any = { statusCode, elapsedTime };

        // Exclude sensitive information from log.
        if (!protectedUlrs) {
          response.data = data;
        }

        logger.info(
          `RES: ${id} <| ${userId} |> | ${method} ${originalUrl} ${statusCode} | ${userAgent} ${clientIp} | ${elapsedTime}ms`,
          { request, response },
        );
      }),
      catchError((error) => {
        const elapsedTime = Date.now() - start;

        const statusCode =
          error.type === ExceptionTypes.USER
            ? HttpStatus.UNPROCESSABLE_ENTITY
            : HttpStatus.INTERNAL_SERVER_ERROR;

        const response = {
          statusCode,
          elapsedTime,
          error,
        };

        const logMessage = `RES: ${id} <| ${userId} |> | ${method} ${originalUrl} ${statusCode} | ${userAgent} ${clientIp} | ${elapsedTime}ms`;

        if (statusCode >= HttpStatus.INTERNAL_SERVER_ERROR) {
          logger.error(logMessage, { request, response });
        } else {
          logger.info(logMessage, { request, response });
        }

        throw error;
      }),
    );
  }
}
