import { Logger } from 'winston';
import { IsEmail, IsString, IsUUID, MaxLength } from 'class-validator';
import { AutoValidator } from '@desen-web/common/utils/validate.util';
import { User } from '@desen-web/users/domain/entities/user.entity';
import { UserRepository } from '@desen-web/users/domain/repositories/user.repository';
import { GetUserByEmailUseCase } from '@desen-web/users/application/usecases/user/get_by_email.usecase';
import { filterProperties } from '@desen-web/common/utils/filter_properties.util';

type TGetUserByEmailRequest = Pick<User, 'email'>;

export class GetUserByEmailRequest
  extends AutoValidator
  implements TGetUserByEmailRequest
{
  @IsEmail()
  email: string;

  constructor(props: TGetUserByEmailRequest) {
    super(props);
  }
}

type TGetUserByEmailResponse = Pick<User, 'id' | 'name' | 'password' | 'email'>;

export class GetUserByEmailResponse
  extends AutoValidator
  implements TGetUserByEmailResponse
{
  @IsUUID()
  id: string;

  @IsString()
  name: string;

  @IsString()
  @MaxLength(255)
  password: string;

  @IsEmail()
  email: string;

  constructor(props: TGetUserByEmailResponse) {
    super(
      filterProperties(props, {
        id: null,
        name: null,
        password: null,
        email: null,
      } as TGetUserByEmailResponse),
    );
  }
}

export class GetUserByEmailController {
  private readonly usecase: GetUserByEmailUseCase;

  constructor(
    private readonly logger: Logger,
    userRepository: UserRepository,
  ) {
    this.logger = logger.child({
      context: GetUserByEmailController.name,
    });
    this.usecase = new GetUserByEmailUseCase(this.logger, userRepository);
  }

  async execute(
    request: GetUserByEmailRequest,
  ): Promise<GetUserByEmailResponse> {
    this.logger.debug('Getting user request.', { request });

    const { email } = request;

    const user = await this.usecase.execute(email);

    if (!user) return null;

    const response = new GetUserByEmailResponse(user);

    return response;
  }
}
