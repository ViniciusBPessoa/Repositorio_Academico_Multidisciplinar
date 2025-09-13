import type { DynamicModule } from '@nestjs/common';
import type { ConfigModuleOptions } from '@nestjs/config';
import { ConfigModule as NestConfigModule } from '@nestjs/config';

export class ConfigModule {
  static forRoot(options: ConfigModuleOptions): DynamicModule {
    options = Object.assign({}, { isGlobal: true }, options);
    return {
      module: ConfigModule,
      imports: [NestConfigModule.forRoot(options)],
    };
  }
}
