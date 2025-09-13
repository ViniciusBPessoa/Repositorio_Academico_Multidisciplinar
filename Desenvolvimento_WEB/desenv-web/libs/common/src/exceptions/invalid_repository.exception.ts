import {
  DefaultException,
  Exception,
} from '@desen-web/common/helpers/error.helper';
import { ExceptionTypes } from '@desen-web/common/helpers/error.constants';

@Exception(ExceptionTypes.SYSTEM, 'INVALID_REPOSITORY_EXCEPTION')
export class InvalidRepositoryException extends DefaultException {
  constructor(repositoryName: string) {
    super({
      message: `${repositoryName} must extend DatabaseRepository.`,
      type: ExceptionTypes.SYSTEM,
      code: 'INVALID_REPOSITORY_EXCEPTION',
      data: { repositoryName },
    });
  }
}
