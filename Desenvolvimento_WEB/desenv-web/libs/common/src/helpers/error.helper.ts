import { ExceptionTypes } from './error.constants';

export interface IException {
  type: ExceptionTypes;
  code: string;
  data?: any;
  message?: string;
  retriable?: boolean;
}

export class DefaultException extends Error implements IException {
  static readonly registeredExceptions: { [key: string]: DefaultException } =
    {};
  type: ExceptionTypes;
  code: string;
  data?: any;
  causedByStack: Error['stack'][] = [];
  retriable = false;

  constructor(exception: IException) {
    super(exception.message);
    this.code = exception.code;
    this.type = exception.type;
    this.data = exception.data;
    this.retriable = exception.retriable;
  }

  isUserError(): boolean {
    return [
      ExceptionTypes.USER,
      ExceptionTypes.ADMIN,
      ExceptionTypes.FORBIDDEN,
      ExceptionTypes.UNAUTHORIZED,
      ExceptionTypes.CONFLICT,
    ].includes(this.type);
  }
}

export const Exception = (type: ExceptionTypes, code: string) => {
  return (target: any) => {
    DefaultException.registeredExceptions[code] = target;
    target.prototype.type = type;
    target.prototype.code = code;
  };
};
