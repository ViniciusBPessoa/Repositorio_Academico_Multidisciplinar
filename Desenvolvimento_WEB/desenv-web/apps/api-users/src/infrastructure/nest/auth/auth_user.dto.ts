import type { User } from '@desen-web/users/domain/entities/user.entity';

export type AuthUser = Pick<User, 'id' | 'name' | 'email' | 'password'>;
