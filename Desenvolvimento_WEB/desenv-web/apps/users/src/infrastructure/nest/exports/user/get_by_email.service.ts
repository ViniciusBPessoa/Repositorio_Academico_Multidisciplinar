import { Logger } from 'winston';
import {
  NatsService,
  NatsAddService,
} from '@desen-web/common/modules/rpc.module';
import {
  GetUserByEmailResponse,
  GetUserByEmailRequest,
} from '@desen-web/users/interface/controllers/user/get_by_email.controller';
import { GetUserByEmailNatsRequest } from '@desen-web/users/infrastructure/nest/controllers/user/get_by_email.controller';
import { NATS_SERVICES } from '@desen-web/users/infrastructure/nats/nats.constants';

/**
 * User microservice
 */
@NatsAddService(NATS_SERVICES.USER.GET_BY_EMAIL)
export class GetUserByEmailServiceNats {
  /**
   * Default constructor.
   * @param logger Global logger.
   * @param natsService Service to access Nats.
   */
  constructor(
    private readonly requestId: string,
    private readonly logger: Logger,
    private readonly natsService: NatsService,
  ) {
    this.logger = logger.child({
      context: GetUserByEmailServiceNats.name,
    });
  }

  /**
   * Get user by email microservice.
   * @param request Get user by email data.
   * @returns User if found or null otherwise.
   */
  async execute(
    request: GetUserByEmailRequest,
  ): Promise<GetUserByEmailResponse> {
    const logger = this.logger.child({ loggerId: this.requestId });

    const data: GetUserByEmailNatsRequest = {
      key: `${request.email}`,
      headers: { requestId: this.requestId },
      value: request,
    };

    logger.debug('Get user by email message.', { data });

    const result = await this.natsService.send<
      GetUserByEmailResponse,
      GetUserByEmailNatsRequest
    >(NATS_SERVICES.USER.GET_BY_EMAIL, data);

    logger.debug('Received user message.', { result });

    return result;
  }
}
