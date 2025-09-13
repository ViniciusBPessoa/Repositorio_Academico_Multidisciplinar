import type { ExecutionContext } from '@nestjs/common';
import { createParamDecorator } from '@nestjs/common';
import { NotImplementedException } from '@desen-web/common/exceptions/not_implemented.exception';
import { NullPointerException } from '@desen-web/common/exceptions/null_pointer.exception';
import { ProtocolType } from '@desen-web/common/helpers/protocol.helper';
import type { AuthUser } from '@desen-web/users/domain/entities/auth_user.entity';

/**
 * Get request auth user.
 */
export const AuthUserParam = createParamDecorator(
  (Class: any, context: ExecutionContext): AuthUser => {
    let request: any = null;

    const protocol = context.getType();
    if (protocol === ProtocolType.HTTP) {
      const ctx = context.switchToHttp();
      request = ctx.getRequest();
    } else {
      throw new NotImplementedException(
        `Protocol ${protocol} is not implemented.`,
      );
    }

    if (!request.user) {
      throw new NullPointerException(
        'Request user is not defined. Check if JwtAuthGuard is available.',
      );
    }

    return request.user;
  },
);
