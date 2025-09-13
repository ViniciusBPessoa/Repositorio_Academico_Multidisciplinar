import {
  DefaultException,
  Exception,
} from '@desen-web/common/helpers/error.helper';
import { ExceptionTypes } from '@desen-web/common/helpers/error.constants';

@Exception(ExceptionTypes.USER, 'INVALID_FORMAT')
export class InvalidDataFormatException extends DefaultException {
  constructor(invalidList: string[]) {
    super({
      message: 'Invalid data format',
      type: ExceptionTypes.USER,
      code: 'INVALID_FORMAT',
      data: {
        invalidList: invalidList?.filter((x) => x),
        count: invalidList?.length ?? 1,
      },
    });
  }
}
