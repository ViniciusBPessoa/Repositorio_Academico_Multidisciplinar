import { ExceptionTypes } from '../helpers/error.constants';
import { DefaultException, Exception } from '../helpers/error.helper';

@Exception(ExceptionTypes.UNKNOWN, 'UNKNOWN')
export class UnknownException extends DefaultException {
  constructor(error: Error) {
    super({
      message: 'Unexpected error',
      type: ExceptionTypes.UNKNOWN,
      code: 'UNKNOWN',
      data: error,
    });
  }
}
