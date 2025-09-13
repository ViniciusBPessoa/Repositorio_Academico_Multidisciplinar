import { v4 as uuidV4 } from 'uuid';
import type { ExecutionContext } from '@nestjs/common';
import { createParamDecorator } from '@nestjs/common';
import type { NatsContext } from '../modules/rpc.module';
import { ProtocolType } from '../helpers/protocol.helper';
import { NotImplementedException } from '../exceptions/not_implemented.exception';

/**
 * Create a child logger with request logger ID.
 */
export const RequestId = createParamDecorator(
  (data: any, context: ExecutionContext): string => {
    let requestId = uuidV4();

    const protocol = context.getType();
    if (protocol === ProtocolType.HTTP) {
      const ctx = context.switchToHttp();
      const request = ctx.getRequest();
      requestId = request.id ?? requestId;
    } else if (protocol === ProtocolType.RPC) {
      const ctx = context.switchToRpc();
      const request = ctx.getContext<NatsContext>();
      requestId = request.getHeaders()?.requestId?.toString() ?? requestId;
    } else {
      throw new NotImplementedException(
        `Protocol ${protocol} is not implemented.`,
      );
    }

    return requestId;
  },
);
