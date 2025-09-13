export class NatsRecordBuilder<T = any> {
  private headers?: any;
  private value: T;

  setValue(value: T) {
    this.value = value;
    return this;
  }

  setHeaders(headers: any) {
    this.headers = headers;
    return this;
  }

  build() {
    return {
      headers: { ...this.headers },
      data: { ...this.value },
    };
  }
}
