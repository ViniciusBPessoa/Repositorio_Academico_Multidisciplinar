import {
  DefaultException,
  Exception,
} from '@desen-web/common/helpers/error.helper';
import { ExceptionTypes } from '@desen-web/common/helpers/error.constants';

@Exception(ExceptionTypes.UNAUTHORIZED, 'UNAUTHORIZED')
export class UnauthorizedException extends DefaultException {
  constructor(data?: any) {
    super({
      message: 'Unauthorized request',
      type: ExceptionTypes.UNAUTHORIZED,
      code: 'UNAUTHORIZED',
      data,
    });
  }
}
