import { registerDecorator, type ValidationOptions } from 'class-validator';

export function IsAllVersionUUID(validationOptions?: ValidationOptions) {
  return (object: any, propertyName: string) => {
    registerDecorator({
      name: 'IsAllVersionUUID',
      target: object.constructor,
      propertyName: propertyName,
      constraints: [],
      options: validationOptions,
      validator: {
        validate(value: any) {
          // Regex that checks all UUID versions.
          const regex = new RegExp(
            /[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/g,
          );
          return value && !!regex.exec(value);
        },
      },
    });
  };
}
