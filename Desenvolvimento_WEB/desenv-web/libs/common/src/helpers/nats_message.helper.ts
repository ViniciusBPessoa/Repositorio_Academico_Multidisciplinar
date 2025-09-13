import type { NatsContext } from '@nestjs/microservices';

/**
 * Message sent through nats cluster.
 */
export abstract class NatsMessage<T = any> {
  /**
   * Nats message key.
   */
  private _key?: string;

  get key(): string {
    return this._key;
  }

  set key(key: string) {
    this._key = key;
  }

  /**
   * Nats message headers.
   */
  private _headers?: any = {};

  get headers(): any {
    return this._headers;
  }

  set headers(headers: any) {
    this._headers = headers ?? {};
  }

  /**
   * Nats message value.
   */
  private _value?: string;

  get value(): T {
    return JSON.parse(this._value);
  }

  set value(value: T) {
    this._value = JSON.stringify(value ?? {});
  }
}

export type NatsResponse<T = any> = {
  value: T;
  ctx?: NatsContext;
};
