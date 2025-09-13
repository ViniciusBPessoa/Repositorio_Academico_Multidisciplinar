import type { Logger } from 'winston';
import { MissingDataException } from '@desen-web/common/exceptions/missing_data.exception';
import type { User } from '@desen-web/users/domain/entities/user.entity';
import type { UserRepository } from '@desen-web/users/domain/repositories/user.repository';

export class GetUserByIdUseCase {
  constructor(
    private readonly logger: Logger,
    private readonly userRepository: UserRepository,
  ) {
    this.logger = logger.child({ context: GetUserByIdUseCase.name });
  }

  /**
   * Get user by id.
   *
   * @param id User id.
   * @returns The user found.
   * @throws {MissingDataException} Thrown when any required params are missing.
   */
  async execute(id: User['id']): Promise<User> {
    // Data input check
    if (!id) {
      throw new MissingDataException('ID');
    }

    // Search user
    const user = await this.userRepository.getById(id);

    this.logger.debug('User found.', { user });

    return user;
  }
}
