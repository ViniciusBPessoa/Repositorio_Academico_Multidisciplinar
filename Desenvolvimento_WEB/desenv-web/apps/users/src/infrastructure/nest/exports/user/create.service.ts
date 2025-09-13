import { Logger } from 'winston';
import {
  NatsService,
  NatsAddService,
} from '@desen-web/common/modules/rpc.module';
import { CreateUserNatsRequest } from '@desen-web/users/infrastructure/nest/controllers/user/create.controller';
import { NATS_SERVICES } from '@desen-web/users/infrastructure/nats/nats.constants';
import {
  CreateUserRequest,
  CreateUserResponse,
} from '@desen-web/users/interface/controllers/user/create.controller';

/**
 * Service to call create user at users microservice.
 *
 * This class must be created for each request.
 */
@NatsAddService(NATS_SERVICES.USER.CREATE)
export class CreateUserServiceNats {
  /**
   * Default constructor.
   * @param requestId Unique shared request ID.
   * @param logger Global logger.
   * @param natsService Service to access Nats.
   */
  constructor(
    private readonly requestId: string,
    private readonly logger: Logger,
    private readonly natsService: NatsService,
  ) {
    this.logger = logger.child({
      context: CreateUserServiceNats.name,
    });
  }

  /**
   * Call Users microservice to create a new user.
   * @param payload Data.
   */
  async execute(payload: CreateUserRequest): Promise<CreateUserResponse> {
    const logger = this.logger.child({ loggerId: this.requestId });

    // Request Nats message.
    const data: CreateUserNatsRequest = {
      key: `${payload.id}`,
      headers: { requestId: this.requestId },
      value: payload,
    };

    logger.debug('Send create user by signup message.', { data });

    // Call create users microservice.
    const result = await this.natsService.send<
      CreateUserResponse,
      CreateUserNatsRequest
    >(NATS_SERVICES.USER.CREATE, data);

    logger.debug('Received create user by signup message.', { result });

    return result;
  }
}
