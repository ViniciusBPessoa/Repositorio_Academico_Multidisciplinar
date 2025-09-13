import { ExceptionTypes } from '../helpers/error.constants';
import { DefaultException, Exception } from '../helpers/error.helper';

@Exception(ExceptionTypes.SYSTEM, 'DATABASE')
export class DatabaseException extends DefaultException {
  constructor(error: Error) {
    super({
      message: 'Database error',
      type: ExceptionTypes.SYSTEM,
      code: 'DATABASE',
      data: error,
    });
  }
}
