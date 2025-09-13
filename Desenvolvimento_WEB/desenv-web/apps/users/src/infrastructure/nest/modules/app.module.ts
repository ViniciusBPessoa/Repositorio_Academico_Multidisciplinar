import { ConfigModule } from '@nestjs/config';
import { Logger, Module } from '@nestjs/common';
import { TerminusModule } from '@nestjs/terminus';
import { LoggerModule } from '@desen-web/common/modules/logger.module';
import { UserModule } from './user.module';

@Module({
  imports: [
    ConfigModule.forRoot({ envFilePath: ['.users.env'] }),
    LoggerModule,
    UserModule,
    TerminusModule,
  ],
  providers: [Logger],
})
export class AppModule {}
