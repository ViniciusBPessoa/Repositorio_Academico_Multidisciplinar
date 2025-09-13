import type { User } from '@desen-web/users/domain/entities/user.entity';

export type CreateUserData = Omit<User, 'createdAt'>;
export type UpdateUserData = Partial<
  Omit<User, 'id' | 'password' | 'createdAt'>
> &
  Pick<User, 'id'>;

export interface UserRepository {
  /**
   * Creates a new user.
   * @param user The user object to be created, omitting the 'id' field.
   * @returns A promise that resolves to the created User object.
   */
  create(user: CreateUserData): Promise<User>;

  /**
   * Updates an existing user.
   * @param user The user object with updated information, including at least the 'id' field.
   * @returns A promise that resolves to the updated User object.
   */
  update(user: UpdateUserData): Promise<User>;

  /**
   * Updates an existing user.
   * @param user The user object with updated information, including at least the 'id' field.
   * @returns A promise that resolves to the updated User object.
   */
  updatePassword(user: User, password: User['password']): Promise<User>;

  /**
   * Retrieves a user by their ID.
   * @param id The numeric ID of the user to find.
   * @returns A promise that resolves to the User object if found, or null otherwise.
   */
  getById(id: User['id']): Promise<User | null>;

  /**
   * Retrieves a user by their email address.
   * @param email The email address of the user to find.
   * @returns A promise that resolves to the User object if found, or null otherwise.
   */
  getByEmail(email: User['email']): Promise<User | null>;

  /**
   * Retrieves all users.
   * @returns A promise that resolves to array of User objects.
   */
  getAll(): Promise<User[]>;
}
