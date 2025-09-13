import type { Logger } from 'winston';
import { MissingDataException } from '@desen-web/common/exceptions/missing_data.exception';
import type { User } from '@desen-web/users/domain/entities/user.entity';
import type { UserRepository } from '@desen-web/users/domain/repositories/user.repository';
import { UserNotFoundException } from '@desen-web/users/application/exceptions/user_not_found.exception';

export class ChangeUserPasswordUseCase {
  /**
   * Default constructor.
   * @param logger Global logger instance.
   * @param userRepository User repository.
   */
  constructor(
    private logger: Logger,
    private readonly userRepository: UserRepository,
  ) {
    this.logger = logger.child({ context: ChangeUserPasswordUseCase.name });
  }

  /**
   * Update user password.
   *
   * @param user User to update password.
   * @param password The new user password.
   * @returns User updated.
   */
  async execute(id: User['id'], password: string): Promise<User> {
    if (!id || !password) {
      throw new MissingDataException([
        ...(!id ? ['User Id'] : []),
        ...(!password ? ['Password'] : []),
      ]);
    }

    const user = await this.userRepository.getById(id);

    if (!user) {
      throw new UserNotFoundException({ id });
    }

    this.logger.debug('User found.', { user });

    const updatedUser = await this.userRepository.updatePassword(
      user,
      password,
    );

    this.logger.debug('User updated', { user: updatedUser });

    return updatedUser;
  }
}
