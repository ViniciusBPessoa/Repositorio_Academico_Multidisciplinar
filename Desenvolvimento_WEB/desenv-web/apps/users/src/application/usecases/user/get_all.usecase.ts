import type { Logger } from 'winston';
import type { UserRepository } from '@desen-web/users/domain/repositories/user.repository';
import type { User } from '@desen-web/users/domain/entities/user.entity';

export class GetAllUserUseCase {
  /**
   * Default constructor.
   * @param logger Global logger instance.
   * @param userRepository User repository.
   */
  constructor(
    private readonly logger: Logger,
    private readonly userRepository: UserRepository,
  ) {
    this.logger = logger.child({ context: GetAllUserUseCase.name });
  }

  /**
   * Get all user.
   * @returns User entity array.
   */
  async execute(): Promise<User[]> {
    this.logger.debug('Search all users.');

    const result = await this.userRepository.getAll();

    this.logger.debug('Users found.', { result });

    return result;
  }
}
