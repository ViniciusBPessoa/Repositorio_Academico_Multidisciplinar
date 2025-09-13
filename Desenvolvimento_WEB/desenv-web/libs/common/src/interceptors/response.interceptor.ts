import {
  Injectable,
  NestInterceptor,
  ExecutionContext,
  CallHandler,
} from '@nestjs/common';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { Reflector } from '@nestjs/core';
/**
 * Response format.
 */
export interface Response<T> {
  success: boolean;
  data: T;
  error: any;
}

/**
 * Intercepts response and change it to response format.
 */
@Injectable()
export class ResponseInterceptor<T> implements NestInterceptor<T, Response<T>> {
  /**
   * Default interceptor constructor.
   * @param reflector Access to class or method modifiers.
   */
  constructor(private readonly reflector: Reflector) {}

  /**
   * Intercept response and map data to response format.
   * @param context Request context.
   * @param next Next handle function.
   * @returns Modified response data.
   */
  intercept(
    context: ExecutionContext,
    next: CallHandler,
  ): Observable<Response<T>> {
    return next.handle().pipe(
      map((data) => ({
        success: true,
        data,
        error: null,
      })),
    );
  }
}
