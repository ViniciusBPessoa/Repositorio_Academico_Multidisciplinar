import {
  DefaultException,
  Exception,
} from '@desen-web/common/helpers/error.helper';
import { ExceptionTypes } from '@desen-web/common/helpers/error.constants';

@Exception(ExceptionTypes.SYSTEM, 'MISSING_ENV_VAR')
export class MissingEnvVarException extends DefaultException {
  constructor(missing: string | number | string[]) {
    super({
      message: `Missing env var: ${missing}`,
      type: ExceptionTypes.SYSTEM,
      code: 'MISSING_ENV_VAR',
      data: missing,
    });
  }
}
