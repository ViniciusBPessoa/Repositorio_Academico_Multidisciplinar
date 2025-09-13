import type { ExecutionContext } from '@nestjs/common';
import { createParamDecorator, applyDecorators } from '@nestjs/common';
import { ApiHeader } from '@nestjs/swagger';
import { HeaderParam } from '../dtos/http_header.dto';
import { ProtocolType } from '../helpers/protocol.helper';
import { NullPointerException } from '../exceptions/null_pointer.exception';
import { NotImplementedException } from '../exceptions/not_implemented.exception';

export function TransactionApiHeader() {
  return applyDecorators(
    ApiHeader({
      name: HeaderParam.X_TRANSACTION_ID,
      description:
        'The transaction ID is a UUID (v4) used to uniquely identify the object that will be created. All objects must have an identifier.',
      required: true,
    }),
  );
}

/**
 * Get request transaction id.
 */
export const RequestTransactionId = createParamDecorator(
  (data: any, context: ExecutionContext): string => {
    const protocol = context.getType();
    if (protocol !== ProtocolType.HTTP) {
      throw new NotImplementedException(
        `Protocol ${protocol} is not implemented.`,
      );
    }

    const ctx = context.switchToHttp();
    const request = ctx.getRequest();

    const { requestTransactionId } = request;

    if (!requestTransactionId) {
      throw new NullPointerException(
        `Request transactionId. 
        Check if RequestTransactionIdInterceptor are available.`,
      );
    }

    return requestTransactionId;
  },
);
