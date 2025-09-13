import {
  DefaultException,
  Exception,
} from '@desen-web/common/helpers/error.helper';
import { ExceptionTypes } from '@desen-web/common/helpers/error.constants';

@Exception(ExceptionTypes.FORBIDDEN, 'FORBIDDEN')
export class ForbiddenException extends DefaultException {
  constructor(data?: any) {
    super({
      message: 'Forbidden',
      type: ExceptionTypes.FORBIDDEN,
      code: 'FORBIDDEN',
      data,
    });
  }
}
