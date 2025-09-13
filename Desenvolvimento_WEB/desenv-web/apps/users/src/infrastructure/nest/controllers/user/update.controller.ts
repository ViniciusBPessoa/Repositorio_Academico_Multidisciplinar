import { Logger } from 'winston';
import { Controller } from '@nestjs/common';
import {
  NatsMessage,
  NatsResponse,
} from '@desen-web/common/helpers/nats_message.helper';
import {
  NatsMessagePattern,
  Payload,
} from '@desen-web/common/modules/rpc.module';
import { LoggerParam } from '@desen-web/common/decorators/logger.decorator';
import { MicroserviceController } from '@desen-web/common/decorators/microservice_controller.decorator';
import { RepositoryParam } from '@desen-web/common/decorators/repository.decorator';
import { EventEmitterParam } from '@desen-web/common/decorators/event_emitter.decorator';
import { UserRepository } from '@desen-web/users/domain/repositories/user.repository';
import {
  UpdateUserController,
  UpdateUserRequest,
  UpdateUserResponse,
} from '@desen-web/users/interface/controllers/user/update.controller';
import { UserEventEmitterControllerInterface } from '@desen-web/users/interface/events/user.emitter';
import { UserDatabaseRepository } from '@desen-web/users/infrastructure/sequelize/repositories/user.repository';
import { NATS_SERVICES } from '@desen-web/users/infrastructure/nats/nats.constants';
import { UserEventNatsEmitter } from '@desen-web/users/infrastructure/nest/events/user.emitter';

export type UpdateUserNatsRequest = NatsMessage<UpdateUserRequest>;
export type UpdateUserNatsResponse = NatsResponse<UpdateUserResponse>;

/**
 * Update user controller.
 */
@Controller()
@MicroserviceController()
export class UpdateUserMicroserviceController {
  /**
   * Parse update user message and call update user controller.
   *
   * @param userRepository User repository.
   * @param logger Request logger.
   * @param message Request Nats message.
   * @returns Response Nats message.
   */
  @NatsMessagePattern(NATS_SERVICES.USER.UPDATE)
  async execute(
    @RepositoryParam(UserDatabaseRepository)
    userRepository: UserRepository,
    @LoggerParam(UpdateUserMicroserviceController)
    logger: Logger,
    @Payload() message: UpdateUserRequest,
    @EventEmitterParam(UserEventNatsEmitter)
    userEventEmitter: UserEventEmitterControllerInterface,
  ): Promise<UpdateUserNatsResponse> {
    logger.debug('Received message.', { value: message });

    // Parse nats message.
    const payload = new UpdateUserRequest(message);

    logger.info('Updating user.', { payload });

    // Create update user controller.
    const controller = new UpdateUserController(
      logger,
      userRepository,
      userEventEmitter,
    );

    // Update user.
    const updatedUser = await controller.execute(payload);

    logger.info('User updated.', { updatedUser });

    return {
      value: updatedUser,
    };
  }
}
