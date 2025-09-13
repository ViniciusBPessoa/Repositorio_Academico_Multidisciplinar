import { Body, Controller, Logger, Post } from '@nestjs/common';
import { ConfigService } from '@nestjs/config';
import {
  ApiBadRequestResponse,
  ApiBearerAuth,
  ApiCreatedResponse,
  ApiOperation,
  ApiProperty,
  ApiTags,
} from '@nestjs/swagger';
import { IsString, IsStrongPassword, IsUUID, Length } from 'class-validator';
import { LoggerParam } from '@desen-web/common/decorators/logger.decorator';
import { BcryptHashService } from '@desen-web/common/modules/bcrypt.module';
import { ForbiddenException } from '@desen-web/common/exceptions/forbidden.exception';
import { HTTP_ENDPOINTS } from '@desen-web/api-users/infrastructure/nest/controllers/endpoint.constants';
import { AuthUserParam } from '@desen-web/users/infrastructure/nest/decorators/auth_user.decorator';
import { ChangeUserPasswordServiceNats } from '@desen-web/users/infrastructure/nest/exports/user/change_password.service';
import {
  ChangeUserPasswordRequest,
  ChangeUserPasswordResponse,
} from '@desen-web/users/interface/controllers/user/change_password.controller';
import { NatsServiceParam } from '@desen-web/common/decorators/nats_service.decorator';
import { AuthUser } from '@desen-web/api-users/infrastructure/nest/auth/auth_user.dto';

class ChangeUserPasswordBody {
  @ApiProperty({
    description: 'Old client password.',
    example: '007GoldenEye',
    required: true,
  })
  @IsString()
  @Length(8, 255)
  old_password: string;

  @ApiProperty({
    description: 'New password.',
    example: '007NoTimeToDi%',
  })
  @IsStrongPassword({
    minLength: 8,
    minLowercase: 1,
    minNumbers: 1,
    minSymbols: 1,
    minUppercase: 1,
  })
  new_password: string;
}

class ChangeUserPasswordRestResponse {
  @ApiProperty({
    description: 'User ID.',
    example: 'f6e2e084-29b9-4935-a059-5473b13033aa',
    required: true,
  })
  @IsUUID()
  id: string;

  constructor(props: ChangeUserPasswordResponse) {
    this.id = props.id;
  }
}

interface ChangeUserPasswordRestConfig {
  APP_CHANGE_PASSWORD_SALT_ROUNDS: number;
}

/**
 * Change user password controller.
 */
@ApiTags('Authentication')
@Controller(HTTP_ENDPOINTS.AUTH.CHANGE_PASSWORD)
@ApiBearerAuth()
export class ChangeUserPasswordRestController {
  private readonly saltRounds: number;

  constructor(
    private readonly hashService: BcryptHashService,
    configService: ConfigService<ChangeUserPasswordRestConfig>,
  ) {
    const salt = configService.get<number>('APP_CHANGE_PASSWORD_SALT_ROUNDS');

    this.saltRounds = salt ? Number(salt) : 10;
  }

  /**
   * change user password endpoint.
   */
  @ApiOperation({
    summary: 'Change Password',
    description:
      '<b>Description</b>: Change the user password by providing the old and new passwords.',
  })
  @ApiCreatedResponse({
    description: 'User password updated successfully.',
    type: ChangeUserPasswordRestResponse,
  })
  @ApiBadRequestResponse({
    description:
      'If any required params are missing or has invalid format or type.',
  })
  @Post()
  async execute(
    @AuthUserParam() user: AuthUser,
    @NatsServiceParam(ChangeUserPasswordServiceNats)
    changePasswordService: ChangeUserPasswordServiceNats,
    @LoggerParam(ChangeUserPasswordRestController)
    logger: Logger,
    @Body() body: ChangeUserPasswordBody,
  ): Promise<ChangeUserPasswordRestResponse> {
    const { old_password: oldPassword, new_password: newPassword } = body;

    const oldPasswordMatch = this.hashService.compareHash(
      oldPassword,
      user.password,
    );

    if (!oldPasswordMatch) {
      throw new ForbiddenException();
    }

    const newPasswordHash = this.hashService.hashSync(
      newPassword,
      this.saltRounds,
    );

    // Create a payload.
    const payload: ChangeUserPasswordRequest = {
      id: user.id,
      password: newPasswordHash,
    };

    logger.debug('Change user password.', { payload });

    // Call change user password service.
    const result = await changePasswordService.execute(payload);

    logger.debug('User password updated.', { result });

    const response = new ChangeUserPasswordRestResponse(result);

    return response;
  }
}
