export function filterProperties<T>(o: any, type: T): T {
  const n: Partial<T> = {};

  for (const key in type) {
    if (Object.prototype.hasOwnProperty.call(o, key)) {
      (n as any)[key] = o[key];
    }
  }
  return n as T;
}
