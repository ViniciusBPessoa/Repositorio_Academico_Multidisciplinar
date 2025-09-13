import { ExceptionTypes } from '../helpers/error.constants';
import { DefaultException, Exception } from '../helpers/error.helper';

@Exception(ExceptionTypes.SYSTEM, 'NOT_IMPLEMENTED')
export class NotImplementedException extends DefaultException {
  constructor(detail?: string) {
    super({
      message: 'Not implemented',
      type: ExceptionTypes.SYSTEM,
      code: 'NOT_IMPLEMENTED',
      data: detail,
    });
  }
}
