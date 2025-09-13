import { Logger } from 'winston';
import {
  IsUUID,
  IsNotEmpty,
  IsString,
  MaxLength,
  IsEmail,
} from 'class-validator';
import { AutoValidator } from '@desen-web/common/utils/validate.util';
import { User } from '@desen-web/users/domain/entities/user.entity';
import { UserRepository } from '@desen-web/users/domain/repositories/user.repository';
import { CreateUserUseCase } from '@desen-web/users/application/usecases/user/create.usecase';
import {
  UserEventEmitterController,
  UserEventEmitterControllerInterface,
} from '@desen-web/users/interface/events/user.emitter';
import { IsIsoStringDateFormat } from '@desen-web/common/decorators/validate_iso_string_date_format.decorator';
import { filterProperties } from '@desen-web/common/utils/filter_properties.util';

type TCreateUserRequest = Pick<User, 'id' | 'name' | 'password' | 'email'>;

export class CreateUserRequest
  extends AutoValidator
  implements TCreateUserRequest
{
  @IsUUID()
  id: string;

  @IsString()
  @IsNotEmpty()
  @MaxLength(255)
  name: string;

  @IsString()
  @IsNotEmpty()
  @MaxLength(255)
  password: string;

  @IsEmail()
  email: string;

  constructor(props: TCreateUserRequest) {
    super(props);
  }
}

type TCreateUserBySignupResponse = Pick<
  User,
  'id' | 'name' | 'email' | 'createdAt'
>;

export class CreateUserResponse
  extends AutoValidator
  implements TCreateUserBySignupResponse
{
  @IsUUID()
  id: string;

  @IsString()
  name: string;

  @IsEmail()
  email: string;

  @IsIsoStringDateFormat('YYYY-MM-DDTHH:mm:ss.SSSZ', {
    message: 'Invalid format createdAt',
  })
  createdAt: User['createdAt'];

  constructor(props: TCreateUserBySignupResponse) {
    super(
      filterProperties(props, {
        email: null,
        id: null,
        name: null,
        createdAt: null,
      } as TCreateUserBySignupResponse),
    );
  }
}

export class CreateUserController {
  private readonly usecase: CreateUserUseCase;

  constructor(
    private readonly logger: Logger,
    userRepository: UserRepository,
    userServiceEventEmitter: UserEventEmitterControllerInterface,
  ) {
    this.logger = logger.child({
      context: CreateUserController.name,
    });

    const userEventEmitter = new UserEventEmitterController(
      userServiceEventEmitter,
    );

    this.usecase = new CreateUserUseCase(
      this.logger,
      userRepository,
      userEventEmitter,
    );
  }

  async execute(request: CreateUserRequest): Promise<CreateUserResponse> {
    this.logger.debug('Create user request.', { request });

    const createdUser = await this.usecase.execute(request);

    const response = new CreateUserResponse(createdUser);

    this.logger.info('Create user response.', { user: response });

    return response;
  }
}
