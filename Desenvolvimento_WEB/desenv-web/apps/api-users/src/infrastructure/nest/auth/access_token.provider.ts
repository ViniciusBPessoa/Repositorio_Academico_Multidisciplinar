import { Injectable } from '@nestjs/common';
import { ConfigService } from '@nestjs/config';
import { JwtService } from '@nestjs/jwt';
import { AccessToken } from '@desen-web/api-users/infrastructure/nest/auth/auth_token.entity';
import { JwtConfig } from '@desen-web/api-users/infrastructure/nest/auth/jwt.config';
import { AuthUser } from './auth_user.dto';

/**
 * Build access token from an authenticated user.
 */
@Injectable()
export class AccessTokenProvider {
  private readonly version: number;
  private readonly expiresIn: number;

  /**
   * Default constructor.
   * @param jwtService JWT sign service.
   * @param configService Configuration data.
   * @param redisService
   */
  constructor(
    private readonly jwtService: JwtService,
    configService: ConfigService<JwtConfig>,
  ) {
    this.version = Number(configService.get<number>('APP_JWT_VERSION', 1));
    this.expiresIn = Number(
      configService.get<number>('APP_JWT_EXPIRES_IN_S', 300),
    );
  }

  /**
   * Generate an access token to auth user.
   * @param user Authenticated user.
   * @returns JWT access token.
   */
  async generateAccessToken(user: AuthUser): Promise<string> {
    const payload: AccessToken = {
      version: this.version,
      id: user.id,
    };

    // Sign access token.
    return this.jwtService.sign(payload, { expiresIn: this.expiresIn });
  }
}
