import { BuildOptions } from 'sequelize';
import {
  AllowNull,
  Column,
  CreatedAt,
  DataType,
  DeletedAt,
  Model,
  PrimaryKey,
  Table,
  Unique,
  UpdatedAt,
} from 'sequelize-typescript';
import { User, UserEntity } from '@desen-web/users/domain/entities/user.entity';

export type UserAttributes = User;
export type UserCreationAttributes = Pick<
  UserAttributes,
  'name' | 'email' | 'password'
>;

@Table({
  tableName: 'users',
  timestamps: true,
  paranoid: true,
})
export class UserModel
  extends Model<UserAttributes, UserCreationAttributes>
  implements User
{
  @PrimaryKey
  @AllowNull(false)
  @Column(DataType.UUID)
  id: string;

  @AllowNull(false)
  @Column(DataType.STRING)
  name: string;

  @AllowNull(false)
  @Column(DataType.STRING)
  password: string;

  @Unique
  @AllowNull(false)
  @Column(DataType.STRING)
  email: string;

  @CreatedAt
  createdAt: Date;

  @UpdatedAt
  updatedAt: Date;

  @DeletedAt
  deletedAt: Date;

  constructor(values?: UserCreationAttributes, options?: BuildOptions) {
    super(values, options);
  }

  /**
   * Converts this model to an entity.
   * @returns An entity.
   */
  toDomain(): User {
    return new UserEntity(this.get({ plain: true }));
  }
}
