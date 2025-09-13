import { Logger } from 'winston';
import {
  NatsService,
  NatsAddService,
} from '@desen-web/common/modules/rpc.module';
import { ChangeUserPasswordNatsRequest } from '@desen-web/users/infrastructure/nest/controllers/user/change_password.controller';
import { NATS_SERVICES } from '@desen-web/users/infrastructure/nats/nats.constants';
import {
  ChangeUserPasswordRequest,
  ChangeUserPasswordResponse,
} from '@desen-web/users/interface/controllers/user/change_password.controller';

const SERVICE = NATS_SERVICES.USER.CHANGE_PASSWORD;

/**
 * Service to call change user password at users microservice.
 *
 * This class must be created for each request.
 */
@NatsAddService(SERVICE)
export class ChangeUserPasswordServiceNats {
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
      context: ChangeUserPasswordServiceNats.name,
    });
  }

  /**
   * Call Users microservice to change user password.
   * @param payload Data.
   */
  async execute(
    payload: ChangeUserPasswordRequest,
  ): Promise<ChangeUserPasswordResponse> {
    const logger = this.logger.child({ loggerId: this.requestId });

    // Request Nats message.
    const data: ChangeUserPasswordNatsRequest = {
      key: `${payload.id}`,
      headers: { requestId: this.requestId },
      value: payload,
    };

    logger.debug('Send change user password message.', { data });

    // Call change user password microservice.
    const result = await this.natsService.send<
      ChangeUserPasswordResponse,
      ChangeUserPasswordNatsRequest
    >(SERVICE, data);

    logger.debug('Received change user password message.', { result });

    return result;
  }
}
