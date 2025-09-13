import { Logger } from 'winston';
import { IsString, IsUUID, MaxLength, IsEmail } from 'class-validator';
import { AutoValidator } from '@desen-web/common/utils/validate.util';
import {
  UpdateUserData,
  UserRepository,
} from '@desen-web/users/domain/repositories/user.repository';
import { UpdateUserUseCase } from '@desen-web/users/application/usecases/user/update.usecase';
import {
  UserEventEmitterController,
  UserEventEmitterControllerInterface,
} from '@desen-web/users/interface/events/user.emitter';
import { User } from '@desen-web/users/domain/entities/user.entity';
import { filterProperties } from '@desen-web/common/utils/filter_properties.util';

type TUpdateUserRequest = UpdateUserData;

type TUpdateUserResponse = TUpdateUserRequest;

export class UpdateUserRequest
  extends AutoValidator
  implements TUpdateUserRequest
{
  @IsUUID()
  id: UpdateUserData['id'];

  @IsString()
  @MaxLength(255)
  name: UpdateUserData['name'];

  @IsEmail()
  @MaxLength(255)
  email: UpdateUserData['email'];

  constructor(props: UpdateUserRequest) {
    super(props);
  }
}

export class UpdateUserResponse
  extends AutoValidator
  implements TUpdateUserResponse
{
  @IsUUID()
  id: User['id'];

  @IsString()
  @MaxLength(255)
  name: User['name'];

  @IsEmail()
  @MaxLength(255)
  email: User['email'];

  constructor(props: TUpdateUserResponse) {
    super(
      filterProperties(props, {
        id: null,
        name: null,
        email: null,
      } as TUpdateUserResponse),
    );
  }
}

export class UpdateUserController {
  private readonly usecase: UpdateUserUseCase;

  constructor(
    private readonly logger: Logger,
    userRepository: UserRepository,
    serviceEventEmitter: UserEventEmitterControllerInterface,
  ) {
    this.logger = logger.child({ context: UpdateUserController.name });
    const eventEmitter = new UserEventEmitterController(serviceEventEmitter);

    this.usecase = new UpdateUserUseCase(logger, userRepository, eventEmitter);
  }

  async execute(request: UpdateUserRequest): Promise<UpdateUserResponse> {
    this.logger.info('Updating user request.', { request });

    await this.usecase.execute(request);

    const response = new UpdateUserResponse(request);

    this.logger.info('Update user response.', { response });

    return response;
  }
}
