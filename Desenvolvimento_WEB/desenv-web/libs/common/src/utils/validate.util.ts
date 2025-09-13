import type { ValidationError } from 'class-validator';
import { validateSync } from 'class-validator';
import { InvalidDataFormatException } from '../exceptions/invalid_data_format.exception';

export const validate = (value: any): void => {
  const errors = validateSync(value, {
    forbidNonWhitelisted: true,
    whitelist: true,
  });

  if (errors.length) {
    throw new InvalidDataFormatException(
      errors.map((err: ValidationError) => JSON.stringify(err.constraints)),
    );
  }
};

export abstract class AutoValidator {
  constructor(props: any) {
    Object.assign(this, props);
    validate(this);
  }

  /**
   * WARNING: DO NOT OVERRIDE THIS METHOD
   *
   * All classes objects that go through client kafka must have toString method.
   * @returns JSON string.
   */
  toString(): string {
    return JSON.stringify(this);
  }
}
