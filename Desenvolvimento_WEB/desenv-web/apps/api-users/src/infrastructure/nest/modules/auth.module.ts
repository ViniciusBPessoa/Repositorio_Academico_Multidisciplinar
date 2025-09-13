import { Module } from '@nestjs/common';
import { PassportModule } from '@nestjs/passport';
import { ConfigModule } from '@nestjs/config';
import { APP_GUARD } from '@nestjs/core';
import { BcryptModule } from '@desen-web/common/modules/bcrypt.module';
import { NatsModule } from '@desen-web/common/modules/rpc.module';
import { JwtModule } from '@desen-web/common/modules/jwt.module';
import { LoggerModule } from '@desen-web/common/modules/logger.module';
import { ValidationModule } from '@desen-web/common/modules/validation.module';
import { LocalStrategy } from '@desen-web/api-users/infrastructure/nest/auth/local.strategy';
import { JwtStrategy } from '@desen-web/api-users/infrastructure/nest/auth/jwt.strategy';
import { LoginAuthRestController } from '@desen-web/api-users/infrastructure/nest/controllers/auth/login.controller';
import { AccessTokenProvider } from '@desen-web/api-users/infrastructure/nest/auth/access_token.provider';
import { JwtGuard } from '@desen-web/api-users/infrastructure/nest/auth/jwt.guard';
import { ChangeUserPasswordRestController } from '@desen-web/api-users/infrastructure/nest/controllers/auth/change_password.controller';
import { ChangeUserPasswordServiceNats } from '@desen-web/users/infrastructure/nest/exports/user/change_password.service';

/**
 * Authentication endpoints module.
 */
@Module({
  imports: [
    ConfigModule,
    JwtModule.registerAsync(),
    NatsModule.forFeature([ChangeUserPasswordServiceNats]),
    LoggerModule,
    PassportModule,
    BcryptModule,
    ValidationModule,
  ],
  controllers: [LoginAuthRestController, ChangeUserPasswordRestController],
  providers: [
    {
      provide: APP_GUARD,
      useClass: JwtGuard,
    },
    LocalStrategy,
    JwtStrategy,
    AccessTokenProvider,
  ],
})
export class AuthModule {}
