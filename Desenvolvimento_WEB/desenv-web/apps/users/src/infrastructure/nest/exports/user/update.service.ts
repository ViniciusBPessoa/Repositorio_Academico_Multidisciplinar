import { Logger } from 'winston';
import {
  NatsService,
  NatsAddService,
} from '@desen-web/common/modules/rpc.module';
import { UpdateUserNatsRequest } from '@desen-web/users/infrastructure/nest/controllers/user/update.controller';
import { NATS_SERVICES } from '@desen-web/users/infrastructure/nats/nats.constants';
import {
  UpdateUserRequest,
  UpdateUserResponse,
} from '@desen-web/users/interface/controllers/user/update.controller';

const SERVICE = NATS_SERVICES.USER.UPDATE;

/**
 * Service to call update user at users microservice.
 *
 * This class must be created for each request.
 */
@NatsAddService(SERVICE)
export class UpdateUserServiceNats {
  /**
   * Default constructor.
   * @param requestId The request id.
   * @param logger Global logger.
   * @param natsService Service to access Nats.
   */
  constructor(
    private readonly requestId: string,
    private readonly logger: Logger,
    private readonly natsService: NatsService,
  ) {
    this.logger = logger.child({ context: UpdateUserServiceNats.name });
  }

  /**
   * Call update user microservice.
   * @param request Update user data.
   * @returns Updated user data.
   */
  async execute(request: UpdateUserRequest): Promise<UpdateUserResponse> {
    // Create request Nats message.
    const data: UpdateUserNatsRequest = {
      key: `${request.id}`,
      headers: { requestId: this.requestId },
      value: request,
    };

    this.logger.debug('Send update user message.', { data });

    // Call update user microservice.
    const result = await this.natsService.send<
      UpdateUserResponse,
      UpdateUserNatsRequest
    >(SERVICE, data);

    this.logger.debug('Received updated user message.', { result });

    return result;
  }
}
