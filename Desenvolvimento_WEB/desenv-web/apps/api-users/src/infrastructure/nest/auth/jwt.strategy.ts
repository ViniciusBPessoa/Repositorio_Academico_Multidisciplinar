import { Logger } from 'winston';
import { v4 as uuidV4 } from 'uuid';
import { ExtractJwt, Strategy } from 'passport-jwt';
import { PassportStrategy } from '@nestjs/passport';
import { Injectable, UnauthorizedException } from '@nestjs/common';
import { ConfigService } from '@nestjs/config';
import {
  InjectNatsService,
  NatsService,
} from '@desen-web/common/modules/rpc.module';
import { InjectLogger } from '@desen-web/common/modules/logger.module';
import { AccessToken } from '@desen-web/api-users/infrastructure/nest/auth/auth_token.entity';
import { JwtConfig } from './jwt.config';
import { AuthUser } from './auth_user.dto';
import { GetUserByIdRequest } from '@desen-web/users/interface/controllers/user/get_by_id.controller';
import { GetUserByIdServiceNats } from '@desen-web/users/infrastructure/nest/exports/user/get_by_id.service';
import { filterProperties } from '@desen-web/common/utils/filter_properties.util';

/**
 * Implement JWT authentication strategy. Get access token from authentication
 * header, verify and decode it.
 * Should be necessary to call user microservice to get additional user data
 * because old token format.
 */
@Injectable()
export class JwtStrategy extends PassportStrategy(Strategy) {
  /**
   * Default constructor. Instantiate JWT service to verify and decode access
   * token.
   *
   * @param natsService Nats service.
   * @param configService Configuration data.
   * @param logger Global logger
   * @param cache Cache
   */
  constructor(
    @InjectNatsService() private readonly natsService: NatsService,
    configService: ConfigService<JwtConfig>,
    @InjectLogger() private logger: Logger,
  ) {
    // Build JWT service.
    super({
      jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
      ignoreExpiration:
        configService.get<string>('APP_JWT_IGNORE_EXPIRATION', 'false') ===
        'true',
      passReqToCallback: true,
      secretOrKey: configService.get<string>('APP_JWT_TOKEN'),
    });
    this.logger = logger.child({ context: JwtStrategy.name });
  }

  /**
   * Decode validated access token payload. Sometimes call user microservice to get
   * additional user data.
   *
   * @param request The express request object.
   * @param payload Validated access token payload.
   * @returns Authenticated user.
   */
  async validate(request: any, payload: AccessToken): Promise<AuthUser> {
    // Check if a previous authorization exists.
    const requestId = request?.id ?? uuidV4();

    this.logger = this.logger.child({ loggerId: requestId });

    const id = payload.id;

    // Create a request.
    const getRequest = new GetUserByIdRequest({ id });

    this.logger.debug('Get additional user data.', { id });

    const getUserByIdService = new GetUserByIdServiceNats(
      requestId,
      this.logger,
      this.natsService,
    );

    // Send request to user service.
    const user = await getUserByIdService.execute(getRequest);

    this.logger.debug('User authenticated.', { user, version: 0 });

    // If no user found, kick user.
    if (!user) {
      this.logger.debug('User not found.', { id });
      throw new UnauthorizedException();
    }

    const authUser: AuthUser = filterProperties(user, {
      email: null,
      id: null,
      name: null,
      password: null,
    } as AuthUser);

    // New we have all required data.
    return authUser;
  }
}
