import { Logger } from 'winston';
import {
  NatsService,
  NatsAddService,
} from '@desen-web/common/modules/rpc.module';
import { NATS_SERVICES } from '@desen-web/users/infrastructure/nats/nats.constants';
import { GetAllUserResponse } from '@desen-web/users/interface/controllers/user/get_all.controller';
import { GetAllUserNatsRequest } from '@desen-web/users/infrastructure/nest/controllers/user/get_all.controller';

const SERVICE = NATS_SERVICES.USER.GET_ALL;

/**
 * Service to call get all users at users microservice.
 */
@NatsAddService(SERVICE)
export class GetAllUserServiceNats {
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
      context: GetAllUserServiceNats.name,
    });
  }

  /**
   * Call user microservice.
   * @returns Paginated users if found.
   */
  async execute(): Promise<GetAllUserResponse> {
    const logger = this.logger.child({ loggerId: this.requestId });

    // Request Nats message.
    const data: GetAllUserNatsRequest = {
      key: null,
      headers: { requestId: this.requestId },
      value: null,
    };

    logger.debug('Get all user message.', { data });

    // Call user microservice.
    const result = await this.natsService.send<
      GetAllUserResponse,
      GetAllUserNatsRequest
    >(SERVICE, data);

    logger.debug('Get all user result.', {
      result,
    });

    return result;
  }
}
