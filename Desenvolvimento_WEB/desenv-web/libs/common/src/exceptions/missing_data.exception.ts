import {
  DefaultException,
  Exception,
} from '@desen-web/common/helpers/error.helper';
import { ExceptionTypes } from '@desen-web/common/helpers/error.constants';

@Exception(ExceptionTypes.USER, 'MISSING_DATA')
export class MissingDataException extends DefaultException {
  constructor(missingData: string[] | string) {
    super({
      message: `Missing data: ${
        typeof missingData === 'string'
          ? missingData
          : missingData?.filter((x) => x).join(', ')
      }`,
      type: ExceptionTypes.USER,
      code: 'MISSING_DATA',
      data:
        typeof missingData === 'string'
          ? missingData
          : missingData?.filter((x) => x),
    });
  }
}
