import { DatabaseRepository } from '@desen-web/common/modules/sequelize.module';
import type { User } from '@desen-web/users/domain/entities/user.entity';
import type {
  CreateUserData,
  UpdateUserData,
  UserRepository,
} from '@desen-web/users/domain/repositories/user.repository';
import { UserModel } from '@desen-web/users/infrastructure/sequelize/models/user.model';

type UserId = User['id'];
type UserEmail = User['email'];
type UserPassword = User['password'];

export class UserDatabaseRepository
  extends DatabaseRepository
  implements UserRepository
{
  static toDomain(model: UserModel | null): User | null {
    return model?.toDomain() ?? null;
  }

  async create(user: CreateUserData): Promise<User> {
    const createdUser = await UserModel.create(user, {
      transaction: this.transaction,
    });
    return createdUser.toDomain();
  }

  async update(user: UpdateUserData): Promise<User> {
    const [, [userUpdated]] = await UserModel.update(user, {
      where: { id: user.id },
      transaction: this.transaction,
      returning: true,
    });
    return UserDatabaseRepository.toDomain(userUpdated);
  }

  async updatePassword(user: User, password: UserPassword): Promise<User> {
    const [, [userUpdated]] = await UserModel.update(
      { password },
      {
        where: { id: user.id },
        transaction: this.transaction,
        returning: true,
      },
    );
    return UserDatabaseRepository.toDomain(userUpdated);
  }

  async getById(id: UserId): Promise<User | null> {
    const user = await UserModel.findOne({
      where: { id },
    });
    return UserDatabaseRepository.toDomain(user);
  }

  async getByEmail(email: UserEmail): Promise<User | null> {
    const user = await UserModel.findOne({
      where: { email },
    });
    return UserDatabaseRepository.toDomain(user);
  }

  async getAll(): Promise<User[]> {
    const users = await UserModel.findAll();

    return users.map(UserDatabaseRepository.toDomain);
  }
}
