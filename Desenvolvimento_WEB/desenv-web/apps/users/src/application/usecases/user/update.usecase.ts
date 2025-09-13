import type { Logger } from 'winston';
import { MissingDataException } from '@desen-web/common/exceptions/missing_data.exception';
import type { User } from '@desen-web/users/domain/entities/user.entity';
import type {
  UpdateUserData,
  UserRepository,
} from '@desen-web/users/domain/repositories/user.repository';
import type { UserEventEmitter } from '@desen-web/users/application/events/user.emitter';
import { UserNotFoundException } from '@desen-web/users/application/exceptions/user_not_found.exception';
import { filterProperties } from '@desen-web/common/utils/filter_properties.util';

export class UpdateUserUseCase {
  constructor(
    private readonly logger: Logger,
    private readonly userRepository: UserRepository,
    private readonly eventEmitter: UserEventEmitter,
  ) {
    this.logger = logger.child({ context: UpdateUserUseCase.name });
  }

  /**
   * Update user properties.
   * @param updateData Object containing user uuid and properties to update.
   * @throws {MissingDataException} When uuid is missing.
   * @throws {UserNotFoundException} When user is not found.
   */
  async execute(updateData: UpdateUserData): Promise<User> {
    if (!updateData?.id) {
      throw new MissingDataException('User Uuid');
    }

    const { id } = updateData;

    const user = await this.userRepository.getById(id);

    this.logger.debug('User found.', { user });

    if (!user) {
      throw new UserNotFoundException({ id });
    }

    const updatedUser = await this.userRepository.update({
      ...user,
      ...filterProperties(updateData, {
        id: null,
        name: null,
        email: null,
        updatedAt: null,
      } as UpdateUserData),
    });

    this.logger.debug('User updated.', { updatedUser });

    this.eventEmitter.updatedUser(updatedUser);

    return updatedUser;
  }
}
