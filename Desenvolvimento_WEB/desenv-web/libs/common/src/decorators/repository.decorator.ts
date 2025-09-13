import type { Logger } from 'winston';
import type { Sequelize, Transaction } from 'sequelize';
import type { ExecutionContext } from '@nestjs/common';
import { createParamDecorator, SetMetadata } from '@nestjs/common';
import { NotImplementedException } from '../exceptions/not_implemented.exception';
import { DatabaseRepository } from '../modules/sequelize.module';
import { ProtocolType } from '../helpers/protocol.helper';
import { InvalidRepositoryException } from '../exceptions/invalid_repository.exception';

type SequelizePacket = {
  transaction: Transaction;
  sequelize: Sequelize;
  logger: Logger;
};

function getTransaction(context: ExecutionContext): SequelizePacket {
  const protocol = context.getType();
  if (protocol === ProtocolType.HTTP) {
    const ctx = context.switchToHttp();
    const request = ctx.getRequest();
    return {
      transaction: request.transaction,
      sequelize: request.sequelize,
      logger: request.logger,
    };
  }
  if (protocol === ProtocolType.RPC) {
    const ctx = context.switchToRpc();
    const request = ctx.getContext();
    return {
      transaction: request.transaction,
      sequelize: request.sequelize,
      logger: request.logger,
    };
  }
  throw new NotImplementedException(`Protocol ${protocol} is not implemented.`);
}
/**
 * Database transaction decorator for Nest controller classes.
 */
export const TransactionParam = createParamDecorator(
  (data: any, context: ExecutionContext): Transaction => {
    const { transaction } = getTransaction(context);
    return transaction;
  },
);

/**
 * Database repository decorator for Nest controller classes.
 */
export const RepositoryParam = createParamDecorator(
  (Repository: any, context: ExecutionContext): DatabaseRepository => {
    if (!(Repository.prototype instanceof DatabaseRepository)) {
      throw new InvalidRepositoryException(Repository.name);
    }

    const { transaction, sequelize, logger } = getTransaction(context);
    const repLogger = logger.child({ context: Repository.name });

    return new Repository(transaction, sequelize, repLogger);
  },
);

/**
 * Disable database transaction.
 */
export const DISABLE_DATABASE_TRANSACTION = 'DISABLE_DATABASE_TRANSACTION';
export const DisableDatabaseTransaction = () =>
  SetMetadata(DISABLE_DATABASE_TRANSACTION, true);
