import { Logger } from 'winston';
import { v4 as uuidV4 } from 'uuid';
import { Strategy } from 'passport-local';
import { PassportStrategy } from '@nestjs/passport';
import { Injectable, UnauthorizedException } from '@nestjs/common';
import { BcryptHashService } from '@desen-web/common/modules/bcrypt.module';
import {
  InjectNatsService,
  NatsService,
} from '@desen-web/common/modules/rpc.module';
import { InjectLogger } from '@desen-web/common/modules/logger.module';
import {
  InjectValidator,
  Validator,
} from '@desen-web/common/modules/validation.module';
import { AuthenticateRestRequest } from '@desen-web/api-users/infrastructure/nest/controllers/auth/login.controller';
import { AuthUser } from './auth_user.dto';
import { GetUserByEmailRequest } from '@desen-web/users/interface/controllers/user/get_by_email.controller';
import { GetUserByEmailServiceNats } from '@desen-web/users/infrastructure/nest/exports/user/get_by_email.service';
import { filterProperties } from '@desen-web/common/utils/filter_properties.util';

/**
 * Implement local strategy. Authenticate user with phone number and password.
 */
@Injectable()
export class LocalStrategy extends PassportStrategy(Strategy, 'local') {
  private readonly mobileSessionSystemId: string;

  /**
   * Default constructor builds a local logger instance.
   * @param natsService Nats service.
   * @param hashService Password hash compare service.
   * @param validator validate service.
   * @param logger Global logger.
   * @param configService Config Service.
   */
  constructor(
    @InjectNatsService() private readonly natsService: NatsService,
    private readonly hashService: BcryptHashService,
    @InjectValidator() private readonly validator: Validator,
    @InjectLogger() private logger: Logger,
  ) {
    // Tells passport to get username and password from request body.
    super({
      usernameField: 'username',
      passwordField: 'password',
      passReqToCallback: true,
    });
    this.logger = logger.child({ context: LocalStrategy.name });
  }

  /**
   * Authenticate user by phone number and password.
   * @param request The express request object.
   * @param username User username.
   * @param password User password.
   * @returns Authenticated user.
   */
  async validate(
    request: any,
    username: string,
    password: string,
  ): Promise<AuthUser> {
    const requestId = request?.id ?? uuidV4();

    this.logger = this.logger.child({ loggerId: requestId });
    this.logger.debug('Authenticating user.', { username });

    const payload = new AuthenticateRestRequest({
      username,
      password,
    });
    await this.validator(payload);

    username = username.replace(/\+/, '');

    const userData = new GetUserByEmailRequest({ email: username });

    // Create get user service
    const getUserByPhoneNumberService = new GetUserByEmailServiceNats(
      requestId,
      this.logger,
      this.natsService,
    );

    // Get user data.
    const userFound = await getUserByPhoneNumberService.execute(userData);

    // If no user found, kick user.
    if (!userFound) {
      this.logger.debug('User not found.', { phoneNumber: username });
      throw new UnauthorizedException();
    }

    // If user has no password, kick user.
    if (!userFound.password) {
      this.logger.debug('User has no password.', { phoneNumber: username });
      throw new UnauthorizedException();
    }

    // If password is incorrect, kick user.
    if (!this.hashService.compareHash(password, userFound.password)) {
      this.logger.debug('Password does not match.', { phoneNumber: username });
      throw new UnauthorizedException();
    }

    this.logger.debug('User authenticated successfully.', {
      phoneNumber: username,
    });

    // All required data are available on access token payload.
    return filterProperties(userFound, {
      email: null,
      id: null,
      name: null,
      password: null,
    } as AuthUser);
  }
}
