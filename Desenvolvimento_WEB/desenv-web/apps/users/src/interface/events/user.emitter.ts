import {
  IsUUID,
  IsNotEmpty,
  IsString,
  IsEmail,
  MaxLength,
} from 'class-validator';
import { AutoValidator } from '@desen-web/common/utils/validate.util';
import {
  UserEvent,
  UserEventEmitter,
} from '@desen-web/users/application/events/user.emitter';

export enum UserEventType {
  UPDATED = 'UPDATED',
  CREATED = 'CREATED',
  UPDATED_PASSWORD = 'UPDATED_PASSWORD',
}

type TUserControllerEvent = Pick<UserEvent, 'id' | 'name' | 'email'>;

export class UserControllerEvent
  extends AutoValidator
  implements TUserControllerEvent
{
  @IsUUID()
  id: string;

  @IsString()
  @IsNotEmpty()
  @MaxLength(255)
  name: string;

  @IsEmail()
  @MaxLength(255)
  email: string;

  constructor(props: TUserControllerEvent) {
    super(props);
  }
}

export interface UserEventEmitterControllerInterface {
  /**
   * Emit user event.
   * @param eventName The event name.
   * @param event Data.
   */
  emitUserEvent(eventName: UserEventType, event: UserControllerEvent): void;
}

export class UserEventEmitterController implements UserEventEmitter {
  constructor(
    private readonly eventEmitter: UserEventEmitterControllerInterface,
  ) {}

  /**
   * Emit user event.
   * @param eventName The event name.
   * @param event Data.
   */
  createdUser(event: UserEvent): void {
    const controllerEvent = this.formatData(event);
    this.eventEmitter.emitUserEvent(UserEventType.CREATED, controllerEvent);
  }

  /**
   * Emit user event.
   * @param eventName The event name.
   * @param event Data.
   */
  updatedUser(event: UserEvent): void {
    const controllerEvent = this.formatData(event);
    this.eventEmitter.emitUserEvent(UserEventType.UPDATED, controllerEvent);
  }

  updatedUserPassword(event: UserEvent): void {
    const controllerEvent = this.formatData(event);
    this.eventEmitter.emitUserEvent(
      UserEventType.UPDATED_PASSWORD,
      controllerEvent,
    );
  }

  /**
   * Format user event data to controller event.
   * @param event User event data.
   * @returns Formatted controller event.
   */
  private formatData(event: UserEvent): UserControllerEvent {
    return new UserControllerEvent({
      id: event.id,
      name: event.name,
      email: event.email,
    });
  }
}
