import { Logger } from 'winston';
import { NatsEventEmitter } from '@desen-web/common/interceptors/nats_event.interceptor';
import { NatsMessage } from '@desen-web/common/helpers/nats_message.helper';
import { NatsAddEvent } from '@desen-web/common/modules/rpc.module';
import { NATS_EVENTS } from '@desen-web/users/infrastructure/nats/nats.constants';
import {
  UserControllerEvent,
  UserEventEmitterControllerInterface,
  UserEventType,
} from '@desen-web/users/interface/events/user.emitter';

const eventMapper = NATS_EVENTS.USER;

type UserNatsEvent = NatsMessage<UserControllerEvent>;

/**
 * User microservice.
 */
@NatsAddEvent(Object.values(eventMapper))
export class UserEventNatsEmitter
  implements UserEventEmitterControllerInterface
{
  /**
   * Default constructor.
   * @param requestId Unique shared request ID.
   * @param eventEmitter Client to access Nats.
   * @param logger Global logger.
   */
  constructor(
    private readonly requestId: string,
    private readonly eventEmitter: NatsEventEmitter,
    private readonly logger: Logger,
  ) {
    this.logger = logger.child({ context: UserEventNatsEmitter.name });
  }

  /**
   * Call  to emit message.
   * @param eventName The event name.
   * @param event The event data.
   */
  emitUserEvent(eventName: UserEventType, event: UserControllerEvent): void {
    // Request Nats message.
    const data: UserNatsEvent = {
      key: `${event.uuid}`,
      headers: { requestId: this.requestId },
      value: event,
    };

    this.logger.debug('Emit User event.', { eventName, data });

    // Call create PixDecodedAccount microservice.
    const result = this.eventEmitter.emit({
      name: eventMapper[eventName],
      data,
    });

    this.logger.debug('User event emitted.', { result });
  }
}
