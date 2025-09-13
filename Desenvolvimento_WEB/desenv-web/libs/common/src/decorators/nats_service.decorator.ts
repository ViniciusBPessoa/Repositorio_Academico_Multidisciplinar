import type { ExecutionContext } from '@nestjs/common';
import { createParamDecorator } from '@nestjs/common';
import type { RemoteNatsService } from '../modules/rpc.module';
import { NatsModule } from '../modules/rpc.module';
import { NotImplementedException } from '../exceptions/not_implemented.exception';
import { NullPointerException } from '../exceptions/null_pointer.exception';
import { ProtocolType } from '../helpers/protocol.helper';

/**
 * Get kafka service.
 */
export const NatsServiceParam = createParamDecorator(
  (NatsService: any, context: ExecutionContext): RemoteNatsService => {
    let request: any = null;

    const protocol = context.getType();
    if (protocol === ProtocolType.HTTP) {
      const ctx = context.switchToHttp();
      request = ctx.getRequest();
    } else if (protocol === ProtocolType.RPC) {
      const ctx = context.switchToRpc();
      request = ctx.getContext();
    } else {
      throw new NotImplementedException(
        `Protocol ${protocol} is not implemented.`,
      );
    }

    const { id, kafkaService, logger } = request;

    if (!id || !logger || !kafkaService) {
      throw new NullPointerException(
        `Request id, logger, or kafkaService are not defined. 
        Check if RequestIdInterceptor, LoggerInterceptor, or *NatsServiceInterceptor are available.`,
      );
    }

    return NatsModule.createRemoteService(
      NatsService,
      id,
      logger,
      kafkaService,
    );
  },
);
