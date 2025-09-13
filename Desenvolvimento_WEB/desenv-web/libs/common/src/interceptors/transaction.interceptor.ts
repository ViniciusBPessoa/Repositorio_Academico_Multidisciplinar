import {
  Injectable,
  NestInterceptor,
  ExecutionContext,
  CallHandler,
} from '@nestjs/common';
import { Logger } from 'winston';
import { Reflector } from '@nestjs/core';
import { Observable, catchError, tap } from 'rxjs';
import { Transaction, Sequelize } from 'sequelize';
import { ProtocolType } from '../helpers/protocol.helper';
import { InjectLogger, InjectSequelize } from '../modules';
import { DISABLE_DATABASE_TRANSACTION } from '../decorators/repository.decorator';
import { NotImplementedException, DatabaseException } from '../exceptions';

@Injectable()
export class TransactionInterceptor implements NestInterceptor {
  constructor(
    @InjectSequelize() private readonly sequelize: Sequelize,
    @InjectLogger() private readonly logger: Logger,
    private readonly reflector: Reflector,
  ) {}

  async intercept(
    context: ExecutionContext,
    next: CallHandler,
  ): Promise<Observable<any>> {
    let request: any = null;
    const protocol = context.getType();
    if (protocol === ProtocolType.HTTP) {
      const ctx = context.switchToHttp();
      request = ctx.getRequest();
    } else if (protocol === ProtocolType.RPC) {
      const ctx = context.switchToRpc();
      request = ctx.getContext();
    } else {
      throw new NotImplementedException(
        `Protocol ${protocol} is not implemented.`,
      );
    }

    const logger: Logger = (request.logger ?? this.logger).child({
      context: TransactionInterceptor.name,
    });

    // Check if requested controller or handler has disable database transaction
    // protection.
    // Controller or handler decorated with @DisableDatabaseTransaction goes
    // around without creating a database transaction.
    const disableTransaction = this.reflector.getAllAndOverride<boolean>(
      DISABLE_DATABASE_TRANSACTION,
      [context.getHandler(), context.getClass()],
    );

    if (disableTransaction) {
      logger.debug('Transaction creation skipped.');
      return next.handle();
    }

    let transaction: Transaction = null;

    try {
      transaction = await this.sequelize.transaction();

      logger.debug('Transaction created.');
    } catch (error) {
      logger.error('Error to create transaction.', error);

      throw new DatabaseException(error);
    }

    request.transaction = transaction;
    request.sequelize = this.sequelize;

    return next.handle().pipe(
      tap(async () => {
        await transaction.commit();
        logger.debug('Transaction committed.');
      }),
      catchError(async (err) => {
        await transaction.rollback();
        logger.debug('Transaction rolled back.');
        throw err;
      }),
    );
  }
}
