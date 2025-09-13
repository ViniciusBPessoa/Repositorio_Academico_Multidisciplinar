import { Injectable, Module } from '@nestjs/common';
import * as bcrypt from 'bcrypt';
import { InvalidDataFormatException } from '../exceptions/invalid_data_format.exception';

const PASSWORD_LENGTH = 72; // For bcrypt, maxLength is 72 characters
@Injectable()
export class BcryptHashService {
  hashSync(password: string, saltOrRounds: number): string {
    if (password.length > PASSWORD_LENGTH) {
      throw new InvalidDataFormatException([
        `Password max length must be ${PASSWORD_LENGTH} characters `,
      ]);
    }

    return bcrypt.hashSync(password, saltOrRounds);
  }
  compareHash(password: string, hash: string): boolean {
    return bcrypt.compareSync(password, hash);
  }
}

@Module({
  providers: [BcryptHashService],
  exports: [BcryptHashService],
})
export class BcryptModule {}
