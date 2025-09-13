import {
  Controller,
  Post,
  HttpCode,
  HttpStatus,
  UseGuards,
} from '@nestjs/common';
import { IsEmail, IsNotEmpty, IsString, MaxLength } from 'class-validator';
import { Logger } from 'winston';
import {
  ApiTags,
  ApiBody,
  ApiOperation,
  ApiOkResponse,
  ApiUnauthorizedResponse,
  ApiBadRequestResponse,
  ApiProperty,
} from '@nestjs/swagger';
import { Public } from '@desen-web/common/decorators/public.decorator';
import { LoggerParam } from '@desen-web/common/decorators/logger.decorator';
import { AuthUserParam } from '@desen-web/users/infrastructure/nest/decorators/auth_user.decorator';
import { LocalAuthGuard } from '@desen-web/api-users/infrastructure/nest/auth/local_auth.guard';
import { AccessTokenProvider } from '@desen-web/api-users/infrastructure/nest/auth/access_token.provider';
import { HTTP_ENDPOINTS } from '@desen-web/api-users/infrastructure/nest/controllers/endpoint.constants';
import { AuthUser } from '@desen-web/api-users/infrastructure/nest/auth/auth_user.dto';

export class AuthenticateRestRequest {
  @ApiProperty({
    description: 'User email.',
    example: 'john.doe@example.com',
  })
  @IsEmail()
  username!: string;

  @ApiProperty({
    description: 'User defined password.',
    example: '007GoldenEye',
  })
  @IsNotEmpty()
  @IsString()
  @MaxLength(255)
  password!: string;

  constructor(props: AuthenticateRestRequest) {
    Object.assign(this, props);
  }
}

/**
 * Login response DTO.
 */
class AuthenticateRestResponse {
  @ApiProperty({
    type: 'string',
    description:
      'JWT access token. Token used to access all protected endpoints.',
  })
  access_token!: string;
}

/**
 * User authentication controller.
 */
@ApiTags('Authentication')
@Public()
@Controller(HTTP_ENDPOINTS.AUTH.LOGIN)
@UseGuards(LocalAuthGuard)
export class LoginAuthRestController {
  /**
   * Default constructor.
   *
   * @param accessTokenProvider Access token generator.
   */
  constructor(private readonly accessTokenProvider: AccessTokenProvider) {}

  /**
   * Login user by phone number and password. Authentication process is executed
   * by Passport local strategy.
   * @see LocalStrategy
   * @see LocalAuthGuard
   * @param user The logged user.
   * @param requestId HTTP request id,
   * @returns Authentication token.
   */
  @ApiOperation({
    summary: 'Create Access Token for Login',
    description: `<b>Description</b>: Generate an access token by providing your username (email) and password in the request body. 
      The access token is required for logging in and accessing authorized sections.`,
  })
  @ApiBody({
    type: AuthenticateRestRequest,
    required: true,
    description: 'Login requires phone number and password.',
  })
  @ApiOkResponse({
    description: 'User authenticated successfully.',
    type: AuthenticateRestResponse,
  })
  @ApiUnauthorizedResponse({
    description: 'User authentication failed.',
  })
  @ApiBadRequestResponse({
    description:
      'If any required params are missing or has invalid format or type.',
  })
  @Post()
  @HttpCode(HttpStatus.OK)
  async execute(
    @AuthUserParam() user: AuthUser,
    @LoggerParam(LoginAuthRestController)
    logger: Logger,
  ): Promise<AuthenticateRestResponse> {
    logger.debug('Creating access token to user.', { user });

    // Generate access token to authenticated user.
    const accessToken =
      await this.accessTokenProvider.generateAccessToken(user);

    logger.debug('User access token created.', { user });

    return {
      access_token: accessToken,
    };
  }
}
