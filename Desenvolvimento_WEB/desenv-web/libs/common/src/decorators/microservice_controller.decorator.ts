import { applyDecorators, UseFilters, UseInterceptors } from '@nestjs/common';
import { DefaultExceptionFilter } from '../filters';
import {
  RequestIdInterceptor,
  LoggerInterceptor,
  TransactionInterceptor,
  ExceptionInterceptor,
  NatsServiceInterceptor,
  NatsEventInterceptor,
} from '../interceptors';

export function MicroserviceController(interceptors: any[] = []) {
  return applyDecorators(
    UseFilters(DefaultExceptionFilter),
    UseInterceptors(
      RequestIdInterceptor,
      LoggerInterceptor,
      TransactionInterceptor,
      NatsServiceInterceptor,
      NatsEventInterceptor,
      ExceptionInterceptor,
      ...interceptors,
    ),
  );
}

export const ObserverController = MicroserviceController;

/**
 * Decorator for observers of APIs that do not rely on the Transaction interceptor or Rpc interceptor.
 */
export const ApiObserverController = () => {
  return applyDecorators(
    UseFilters(DefaultExceptionFilter),
    UseInterceptors(
      RequestIdInterceptor,
      LoggerInterceptor,
      ExceptionInterceptor,
    ),
  );
};
