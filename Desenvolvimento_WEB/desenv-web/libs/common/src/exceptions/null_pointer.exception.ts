import { ExceptionTypes } from '../helpers/error.constants';
import { DefaultException, Exception } from '../helpers/error.helper';

@Exception(ExceptionTypes.SYSTEM, 'NULL_POINTER')
export class NullPointerException extends DefaultException {
  constructor(detail?: string) {
    super({
      message: 'Null pointer',
      type: ExceptionTypes.SYSTEM,
      code: 'NULL_POINTER',
      data: detail,
    });
  }
}
