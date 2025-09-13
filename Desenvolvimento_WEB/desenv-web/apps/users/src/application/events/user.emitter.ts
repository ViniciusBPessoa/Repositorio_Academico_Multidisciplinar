import type { User } from '@desen-web/users/domain/entities/user.entity';

export type UserEvent = Pick<User, 'id' | 'name' | 'email'>;

export interface UserEventEmitter {
  /**
   * Emit creatd user event.
   * @param event event to fire.
   */
  createdUser: (event: UserEvent) => void;

  /**
   * Emit updated user event.
   * @param event event to fire.
   */
  updatedUser: (event: UserEvent) => void;

  /**
   * Emit updated user password event.
   * @param event event to fire.
   */
  updatedUserPassword: (event: UserEvent) => void;
}
