import { Logger } from 'winston';
import {
  NatsService,
  NatsAddService,
} from '@desen-web/common/modules/rpc.module';
import { GetUserByIdNatsRequest } from '@desen-web/users/infrastructure/nest/controllers/user/get_by_id.controller';
import { NATS_SERVICES } from '@desen-web/users/infrastructure/nats/nats.constants';
import {
  GetUserByIdRequest,
  GetUserByIdResponse,
} from '@desen-web/users/interface/controllers/user/get_by_id.controller';

const SERVICE = NATS_SERVICES.USER.GET_BY_ID;

/**
 * Service to call get user by id at users microservice.
 */
@NatsAddService(SERVICE)
export class GetUserByIdServiceNats {
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
    this.logger = logger.child({ context: GetUserByIdServiceNats.name });
  }

  /**
   * Call get user by id microservice.
   *
   * @param request The user's id.
   * @returns User if found or null otherwise.
   */
  async execute(request: GetUserByIdRequest): Promise<GetUserByIdResponse> {
    // Create request Nats message.
    const data: GetUserByIdNatsRequest = {
      key: `${request.id}`,
      headers: { requestId: this.requestId },
      value: request,
    };

    this.logger.debug('Get user by id message.', { data });

    // Call get user by uuid microservice.
    const result = await this.natsService.send<
      GetUserByIdResponse,
      GetUserByIdNatsRequest
    >(SERVICE, data);

    this.logger.debug('Received user message.', { result });

    // If no user found.
    if (!result) return null;

    return result;
  }
}
