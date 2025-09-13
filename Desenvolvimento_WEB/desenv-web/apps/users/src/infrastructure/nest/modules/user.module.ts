import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { ScheduleModule } from '@nestjs/schedule';
import { BcryptModule } from '@desen-web/common/modules/bcrypt.module';
import { DatabaseModule } from '@desen-web/common/modules/sequelize.module';
import { NatsModule } from '@desen-web/common/modules/rpc.module';
import { LoggerModule } from '@desen-web/common/modules/logger.module';
import { ValidationModule } from '@desen-web/common/modules/validation.module';
import { UpdateUserMicroserviceController } from '@desen-web/users/infrastructure/nest/controllers/user/update.controller';
import { UserModel } from '@desen-web/users/infrastructure/sequelize/models/user.model';
import { CreateUserMicroserviceController } from '@desen-web/users/infrastructure/nest/controllers/user/create.controller';
import { GetUserByEmailMicroserviceController } from '@desen-web/users/infrastructure/nest/controllers/user/get_by_email.controller';
import { ChangeUserPasswordMicroserviceController } from '@desen-web/users/infrastructure/nest/controllers/user/change_password.controller';
import { GetUserByIdMicroserviceController } from '@desen-web/users/infrastructure/nest/controllers/user/get_by_id.controller';
import { GetAllUserMicroserviceController } from '@desen-web/users/infrastructure/nest/controllers/user/get_all.controller';

@Module({
  imports: [
    ScheduleModule.forRoot(),
    ConfigModule,
    LoggerModule,
    ValidationModule,
    NatsModule.forFeature(),
    BcryptModule,
    DatabaseModule.forFeature([UserModel]),
  ],
  controllers: [
    UpdateUserMicroserviceController,
    CreateUserMicroserviceController,
    GetUserByEmailMicroserviceController,
    ChangeUserPasswordMicroserviceController,
    GetUserByIdMicroserviceController,
    GetAllUserMicroserviceController,
  ],
})
export class UserModule {}
