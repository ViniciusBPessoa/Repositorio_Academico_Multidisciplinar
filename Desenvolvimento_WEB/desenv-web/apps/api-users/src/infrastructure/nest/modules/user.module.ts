import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { BcryptModule } from '@desen-web/common/modules/bcrypt.module';
import { NatsModule } from '@desen-web/common/modules/rpc.module';
import { LoggerModule } from '@desen-web/common/modules/logger.module';
import { ValidationModule } from '@desen-web/common/modules/validation.module';

/**
 * User endpoint modules.
 */
@Module({
  imports: [
    ConfigModule,
    LoggerModule,
    NatsModule.forFeature([]),
    BcryptModule,
    ValidationModule,
  ],
  controllers: [],
})
export class UserModule {}
