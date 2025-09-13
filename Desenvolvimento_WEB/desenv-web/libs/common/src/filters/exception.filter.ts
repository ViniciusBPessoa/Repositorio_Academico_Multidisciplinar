import {
  Catch,
  ArgumentsHost,
  ExceptionFilter,
  HttpStatus,
  HttpException,
} from '@nestjs/common';
import { Logger } from 'winston';
import { Response } from 'express';
import { Observable, of, throwError } from 'rxjs';
import { HeaderParam } from '../dtos/http_header.dto';
import { InjectLogger } from '../modules';
import { DefaultException, ExceptionTypes, ProtocolType } from '../helpers';
import { NotImplementedException } from '../exceptions';

/**
 * Capture all default exception thrown by services.
 */
@Catch(DefaultException)
export class DefaultExceptionFilter
  implements ExceptionFilter<DefaultException>
{
  /**
   * Default constructor.
   * @param logger Global logger.
   */
  constructor(@InjectLogger() private readonly logger: Logger) {
    this.logger = logger.child({ context: DefaultExceptionFilter.name });
  }

  /**
   * Process default exceptions.
   * @param exception Default exception catched.
   * @param host Request context.
   */
  catch(exception: DefaultException, host: ArgumentsHost): Observable<any> {
    const protocol = host.getType();
    if (protocol === ProtocolType.RPC) {
      const ctx = host.switchToRpc();
      const request = ctx.getContext();

      // Add catch error to cause by stack in RPC reply message.
      exception.causedByStack.push(exception.stack);

      // If request is nats-based, return exception as object
      if (request?.getHeaders) {
        return throwError(() => exception);
      }

      // If the request is from a service call, throw error to service.
      // Or the exception is retriable, throw error to kafka retries infinitely.
      if (
        request?.getMessage()?.headers?.kafka_correlationId ||
        exception.retriable
      ) {
        // Stringify exception to send it through kafka if it is a message pattern.
        return throwError(() => JSON.stringify(exception));
      }
      // Bypass exception if it is an event pattern and not retriable.
      return of(exception);
    }
    if (protocol === ProtocolType.HTTP) {
      const ctx = host.switchToHttp();
      const request = ctx.getRequest();
      const response = ctx.getResponse<Response>();

      const logger = this.logger.child({ loggerId: request.id });

      if (
        [ExceptionTypes.SYSTEM, ExceptionTypes.UNKNOWN].includes(exception.type)
      ) {
        logger.error('INTERNAL ERROR', { exception });
      } else {
        logger.debug('User error.', { exception });
      }

      // Did exception happen because a user miss information or system bug?
      let status = HttpStatus.INTERNAL_SERVER_ERROR;

      switch (exception.type) {
        case ExceptionTypes.USER:
        case ExceptionTypes.ADMIN:
          status = HttpStatus.UNPROCESSABLE_ENTITY;
          break;
        case ExceptionTypes.FORBIDDEN:
          status = HttpStatus.FORBIDDEN;
          break;
        case ExceptionTypes.UNAUTHORIZED:
          status = HttpStatus.UNAUTHORIZED;
          break;
        case ExceptionTypes.CONFLICT:
          status = HttpStatus.CONFLICT;
          break;
      }

      logException(logger, request, status);

      const message = exception.message;

      // Reply to user
      response.status(status).json({
        success: false,
        data: null,
        error: exception.isUserError()
          ? ExceptionTypes.USER
          : ExceptionTypes.SYSTEM,
        message,
      });
    } else {
      // Sanity check. This will never happen. (I believe).
      throw new NotImplementedException(
        `Protocol ${protocol} is not implemented.`,
      );
    }
  }
}

/**
 * Capture all default exception thrown by services.
 */
@Catch(DefaultException)
export class ApiAsServiceDefaultExceptionFilter
  implements ExceptionFilter<DefaultException>
{
  /**
   * Default constructor.
   * @param logger Global logger.
   */
  constructor(@InjectLogger() private readonly logger: Logger) {
    this.logger = logger.child({ context: DefaultExceptionFilter.name });
  }

  /**
   * Process default exceptions.
   * @param exception Default exception catched.
   * @param host Request context.
   */
  catch(exception: DefaultException, host: ArgumentsHost): Observable<any> {
    const protocol = host.getType();
    if (protocol === ProtocolType.RPC) {
      const ctx = host.switchToRpc();
      const request = ctx.getContext();

      // Add catch error to cause by stack in RPC reply message.
      exception.causedByStack.push(exception.stack);

      // If request is nats-based, return exception as object
      if (request?.getHeaders) {
        return throwError(() => exception);
      }

      // If the request is from a service call, throw error to service.
      // Or the exception is retriable, throw error to kafka retries infinitely.
      if (
        request?.getMessage()?.headers?.kafka_correlationId ||
        exception.retriable
      ) {
        // Stringify exception to send it through kafka if it is a message pattern.
        return throwError(() => JSON.stringify(exception));
      }
      // Bypass exception if it is an event pattern and not retriable.
      return of(exception);
    }
    if (protocol === ProtocolType.HTTP) {
      const ctx = host.switchToHttp();
      const request = ctx.getRequest();
      const response = ctx.getResponse<Response>();

      const logger = this.logger.child({ loggerId: request.id });

      if (
        [ExceptionTypes.SYSTEM, ExceptionTypes.UNKNOWN].includes(exception.type)
      ) {
        logger.error('INTERNAL ERROR', { exception });
      } else {
        logger.debug('User error.', { exception });
      }

      // Did exception happen because a user miss information or system bug?
      let status = HttpStatus.INTERNAL_SERVER_ERROR;

      switch (exception.type) {
        case ExceptionTypes.USER:
        case ExceptionTypes.ADMIN:
          status = HttpStatus.UNPROCESSABLE_ENTITY;
          break;
        case ExceptionTypes.FORBIDDEN:
          status = HttpStatus.FORBIDDEN;
          break;
        case ExceptionTypes.UNAUTHORIZED:
          status = HttpStatus.UNAUTHORIZED;
          break;
        case ExceptionTypes.CONFLICT:
          status = HttpStatus.CONFLICT;
          break;
      }

      logException(logger, request, status);

      const message = exception.message;

      // Reply to user
      response.status(status).json({
        success: false,
        data: null,
        error: exception.isUserError()
          ? ExceptionTypes.USER
          : ExceptionTypes.SYSTEM,
        message,
        code: exception.code,
      });
    } else {
      // Sanity check. This will never happen. (I believe).
      throw new NotImplementedException(
        `Protocol ${protocol} is not implemented.`,
      );
    }
  }
}

/**
 * Process HTTP exception.
 */
@Catch(HttpException)
export class HttpExceptionFilter implements ExceptionFilter<HttpException> {
  /**
   * Default constructor.
   * @param logger Global logger.
   */
  constructor(@InjectLogger() private readonly logger: Logger) {
    this.logger = logger.child({ context: HttpExceptionFilter.name });
  }

  /**
   * Process HTTP exceptions.
   * @param exception HTTP exception catched.
   * @param host Request context.
   */
  catch(exception: HttpException, host: ArgumentsHost) {
    const ctx = host.switchToHttp();
    const request = ctx.getRequest();
    const response = ctx.getResponse<Response>();
    const status = exception.getStatus();

    const logger = this.logger.child({ loggerId: request.id });

    logException(logger, request, status);

    if (status >= HttpStatus.INTERNAL_SERVER_ERROR) {
      logger.error('INTERNAL ERROR', { exception });
    } else {
      logger.debug('USER ERROR.', { exception });
    }

    const message = exception.message;

    // Reply to user
    response.status(status).json({
      success: false,
      data: null,
      error:
        status < HttpStatus.INTERNAL_SERVER_ERROR
          ? ExceptionTypes.USER
          : ExceptionTypes.SYSTEM,
      message,
    });
  }
}

function logException(logger: Logger, request: any, status: number) {
  const { id, ip, originalUrl, method } = request;

  if (request.user) {
    request.userId =
      request.user.uuid ?? request.user.id ?? request.user.phoneNumber;
    request.userApiId = request.user.apiId;
  }

  const userAgent: string = request.get('user-agent') || 'NO_AGENT';
  const userId: string = request.userId ?? '-';
  const clientIp: string = request.headers[HeaderParam.CF_CONNECTION_IP] ?? ip;
  const nonce: string = request.headers[HeaderParam.NONCE] ?? '-';
  const userApiId: string = request.userApiId ?? '-';

  logger.info(
    `RES: ${id} <| ${userId} |> ${userApiId} | ${method} ${originalUrl} ${status} | ${userAgent} ${clientIp} ${nonce}`,
  );
}
