import { Controller } from '@nestjs/common';
import { Logger } from 'winston';
import { EventEmitterParam } from '@desen-web/common/decorators/event_emitter.decorator';
import {
  NatsMessage,
  NatsResponse,
} from '@desen-web/common/helpers/nats_message.helper';
import {
  Ctx,
  NatsContext,
  NatsMessagePattern,
  Payload,
} from '@desen-web/common/modules/rpc.module';
import { LoggerParam } from '@desen-web/common/decorators/logger.decorator';
import { MicroserviceController } from '@desen-web/common/decorators/microservice_controller.decorator';
import { RepositoryParam } from '@desen-web/common/decorators/repository.decorator';
import { UserRepository } from '@desen-web/users/domain/repositories/user.repository';
import {
  CreateUserController,
  CreateUserRequest,
  CreateUserResponse,
} from '@desen-web/users/interface/controllers/user/create.controller';
import { UserEventEmitterControllerInterface } from '@desen-web/users/interface/events/user.emitter';
import { NATS_SERVICES } from '@desen-web/users/infrastructure/nats/nats.constants';
import { UserDatabaseRepository } from '@desen-web/users/infrastructure/sequelize/repositories/user.repository';
import { UserEventNatsEmitter } from '@desen-web/users/infrastructure/nest/events/user.emitter';

export type CreateUserNatsRequest = NatsMessage<CreateUserRequest>;
export type CreateUserNatsResponse = NatsResponse<CreateUserResponse>;

/**
 * User RPC controller.
 */
@Controller()
@MicroserviceController()
export class CreateUserMicroserviceController {
  /**
   * Consumer of create user by signup.
   *
   * @param userRepository User repository.
   * @param logger Request logger.
   * @param userEventEmitter User event emitter.
   * @param message Request Nats message.
   * @returns Response Nats message.
   */
  @NatsMessagePattern(NATS_SERVICES.USER.CREATE)
  async execute(
    @RepositoryParam(UserDatabaseRepository)
    userRepository: UserRepository,
    @LoggerParam(CreateUserMicroserviceController)
    logger: Logger,
    @EventEmitterParam(UserEventNatsEmitter)
    userEventEmitter: UserEventEmitterControllerInterface,
    @Payload() message: CreateUserRequest,
    @Ctx() ctx: NatsContext,
  ): Promise<CreateUserNatsResponse> {
    logger.debug('Received message.', { value: message });

    // Load and validate message payload.
    const payload = new CreateUserRequest(message);

    logger.info('Create user by signup.', { payload });

    // Create and call create user by signup controller.
    const controller = new CreateUserController(
      logger,
      userRepository,
      userEventEmitter,
    );

    // Create user
    const user = await controller.execute(payload);

    logger.info('User created.', { user });

    return {
      value: user,
      ctx,
    };
  }
}
