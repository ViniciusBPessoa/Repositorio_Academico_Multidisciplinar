export class InvalidDecoratorItemException extends Error {
  private readonly msg: string;

  constructor(decorator: string, item: string, context: string) {
    const message = `Invalid ${item} passed to ${decorator}() decorator (${context}).`;
    super(message);

    this.msg = message;
  }

  public what(): string {
    return this.msg;
  }
}

export function validateEach(
  context: { name: string },
  arr: any[],
  predicate: Function,
  decorator: string,
  item: string,
): boolean {
  if (!context?.name) {
    return true;
  }
  const errors = arr.some((str) => !predicate(str));
  if (errors) {
    throw new InvalidDecoratorItemException(decorator, item, context.name);
  }
  return true;
}

export const isEmpty = (array: any): boolean => !(array && array.length > 0);

export const isFunction = (val: any): val is Function =>
  typeof val === 'function';

export function extendArrayMetadata<T extends Array<unknown>>(
  key: string,
  metadata: T,
  target: Function,
) {
  const previousValue = Reflect.getMetadata(key, target) || [];
  const value = [...previousValue, ...metadata];
  Reflect.defineMetadata(key, value, target);
}
