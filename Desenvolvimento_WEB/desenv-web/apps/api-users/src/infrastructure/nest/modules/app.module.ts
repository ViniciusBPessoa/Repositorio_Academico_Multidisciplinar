import { Logger, MiddlewareConsumer, Module, NestModule } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { TerminusModule } from '@nestjs/terminus';
import { JwtModule } from '@desen-web/common/modules/jwt.module';
import { NatsModule } from '@desen-web/common/modules/rpc.module';
import { LoggerMiddleware } from '@desen-web/common/middlewares/logger.middleware';
import { LoggerModule } from '@desen-web/common/modules/logger.module';
import { RequestIdMiddleware } from '@desen-web/common/middlewares/request_id.middleware';
import { BcryptModule } from '@desen-web/common/modules/bcrypt.module';
import { ValidationModule } from '@desen-web/common/modules/validation.module';
import { AuthModule } from './auth.module';
import { UserModule } from './user.module';

/**
 * API Users gateway module
 */
@Module({
  providers: [Logger],
  imports: [
    ConfigModule.forRoot({ envFilePath: ['.api-users.env'] }),
    NatsModule,
    JwtModule,
    BcryptModule,
    ValidationModule,
    LoggerModule,
    AuthModule,
    UserModule,
    TerminusModule,
  ],
})
export class AppModule implements NestModule {
  /**
   * Add middlewares to nest app.
   * @param consumer Nest middleware manager.
   */
  configure(consumer: MiddlewareConsumer) {
    consumer.apply(RequestIdMiddleware, LoggerMiddleware).forRoutes('*');
  }
}
