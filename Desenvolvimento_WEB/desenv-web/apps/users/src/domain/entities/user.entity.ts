import type { Domain } from '@desen-web/common/helpers/domain.helper';

export interface User extends Domain<string> {
  name: string;
  email: string;
  password: string;
}

export class UserEntity implements User {
  id: string;
  name: string;
  email: string;
  password: string;
  createdAt: Date;

  constructor(props: User | Domain<string>) {
    Object.assign(this, props);
  }
}
