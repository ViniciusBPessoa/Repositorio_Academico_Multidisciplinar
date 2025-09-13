import { Controller } from '@nestjs/common';
import { Logger } from 'winston';
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
import { UserRepository } from '@desen-web/users/domain/repositories/user.repository';
import {
  GetUserByIdController,
  GetUserByIdRequest,
  GetUserByIdResponse,
} from '@desen-web/users/interface/controllers/user/get_by_id.controller';
import { NATS_SERVICES } from '@desen-web/users/infrastructure/nats/nats.constants';
import { UserDatabaseRepository } from '@desen-web/users/infrastructure/sequelize/repositories/user.repository';

export type GetUserByIdNatsRequest = NatsMessage<GetUserByIdRequest>;
export type GetUserByIdNatsResponse = NatsResponse<GetUserByIdResponse>;

/**
 * User RPC controller.
 */
@Controller()
@MicroserviceController()
export class GetUserByIdMicroserviceController {
  /**
   * Consumer of get user by id.
   *
   * @param userRepository User repository.
   * @param message Request Nats message.
   * @param logger Request logger.
   * @returns Response Nats message.
   */
  @NatsMessagePattern(NATS_SERVICES.USER.GET_BY_ID)
  async execute(
    @RepositoryParam(UserDatabaseRepository)
    userRepository: UserRepository,
    @LoggerParam(GetUserByIdMicroserviceController)
    logger: Logger,
    @Payload() message: GetUserByIdRequest,
  ): Promise<GetUserByIdNatsResponse> {
    logger.debug('Received message.', { value: message });

    // Parse nats message.
    const payload = new GetUserByIdRequest(message);

    logger.info('Getting user.', { payload });

    // Create and call get user by uuid controller.
    const controller = new GetUserByIdController(logger, userRepository);

    // Get user
    const user = await controller.execute(payload);

    logger.info('User found.', { user });

    return {
      value: user,
    };
  }
}
