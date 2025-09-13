import {
  DefaultException,
  Exception,
} from '@desen-web/common/helpers/error.helper';
import { ExceptionTypes } from '@desen-web/common/helpers/error.constants';
import { User } from '@desen-web/users/domain/entities/user.entity';

@Exception(ExceptionTypes.USER, 'USER_ALREADY_EXISTS')
export class UserAlreadyExistsException extends DefaultException {
  constructor(user: Partial<User>) {
    super({
      type: ExceptionTypes.USER,
      code: 'USER_ALREADY_EXISTS',
      data: user,
    });
  }
}
