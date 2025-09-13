import { ExceptionTypes } from '../helpers/error.constants';
import { DefaultException, Exception } from '../helpers/error.helper';

@Exception(ExceptionTypes.SYSTEM, 'NATS')
export class NatsException extends DefaultException {
  constructor(error: Error) {
    super({
      message: 'Nats error',
      type: ExceptionTypes.SYSTEM,
      code: 'NATS',
      data: error,
    });
  }
}

@Exception(ExceptionTypes.SYSTEM, 'NOT_LOADED_NATS_SERVICE')
export class NotLoadedNatsServiceException extends DefaultException {
  constructor(serviceName: string) {
    super({
      message:
        'The client consumer did not subscribe to the corresponding reply topic. Please load nats service with NatsModule.forFeature().',
      type: ExceptionTypes.SYSTEM,
      code: 'NOT_LOADED_NATS_SERVICE',
      data: serviceName,
    });
  }
}
