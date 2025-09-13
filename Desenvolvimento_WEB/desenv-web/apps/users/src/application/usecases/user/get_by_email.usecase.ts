import type { Logger } from 'winston';
import { MissingDataException } from '@desen-web/common/exceptions/missing_data.exception';
import type { User } from '@desen-web/users/domain/entities/user.entity';
import type { UserRepository } from '@desen-web/users/domain/repositories/user.repository';

export class GetUserByEmailUseCase {
  constructor(
    private logger: Logger,
    private readonly userRepository: UserRepository,
  ) {
    this.logger = logger.child({ context: GetUserByEmailUseCase.name });
  }

  /**
   * Get user by email.
   *
   * @param email User email.
   * @returns The user found.
   * @throws {MissingDataException} Thrown when any required params are missing.
   */
  async execute(email: string): Promise<User> {
    // Data input check
    if (!email) {
      throw new MissingDataException(['Email']);
    }

    // Search user
    const user = await this.userRepository.getByEmail(email);

    this.logger.debug('User found.', { user });

    return user;
  }
}
