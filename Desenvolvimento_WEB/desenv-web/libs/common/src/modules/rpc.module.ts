import { NatsContext, Payload } from '@nestjs/microservices';
import type { ExecutionContext } from '@nestjs/common';
import { createParamDecorator } from '@nestjs/common';
import {
  InjectNatsService,
  NatsAddEvent,
  NatsAddService,
  NatsEventPattern,
  NatsMessagePattern,
  NatsModule,
  NatsService,
  RemoteNatsService,
  createNatsTransport,
} from './nats.module';
import { NotImplementedException, NullPointerException } from '../exceptions';
import { RequestId } from '../decorators/request_id.decorator';
import { NATS_SERVICE, NATS_CLIENT } from './nats.constants';
import { ProtocolType } from '../helpers/protocol.helper';

const RpcPayload = () => Payload('value');

const RpcCtx = createParamDecorator(
  (Class: any, context: ExecutionContext): NatsContext => {
    const protocol = context.getType();
    if (protocol !== ProtocolType.RPC) {
      throw new NotImplementedException(
        `Protocol ${protocol} is not implemented.`,
      );
    }

    const ctx = context.switchToRpc();
    const request = ctx.getContext<NatsContext>();
    // Headers only exists on getData(), because there's no data on getHeaders().
    const headers = ctx.getData?.()?.headers;

    const [subject] = request.getArgs();

    if (!subject) {
      throw new NullPointerException(
        'Request subject is not defined. Check if NatsContext is available.',
      );
    }

    // So it creates a new NatsContext with right headers value from getData().
    return new NatsContext([subject, headers]);
  },
);

export {
  NatsContext,
  NatsService,
  NatsModule,
  RemoteNatsService,
  createNatsTransport,
  NatsAddService,
  NatsAddEvent,
  NatsMessagePattern,
  NatsEventPattern,
  InjectNatsService,
  RpcPayload as Payload,
  RpcCtx as Ctx,
  RequestId,
  NATS_CLIENT,
  NATS_SERVICE,
};
