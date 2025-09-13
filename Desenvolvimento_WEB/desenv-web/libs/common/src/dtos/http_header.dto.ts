// FIXME: não há necessidade de chamar X_ ... pois já pertence a enumeração.
// FIXME: enumeração está prevista para ser removida do typescript, substituir por tipos
export enum HeaderParam {
  X_REPLAY_PROTECTION_SCHEMA = 'x-include-replay-protection-schema',
  NONCE = 'nonce',
  X_TRANSACTION_ID = 'x-transaction-uuid',
  // FIXME: Remove 'transaction_uuid' value when headers x-transaction-uuid is required.
  LEGACY_TRANSACTION_ID = 'transaction_uuid',
  CF_CONNECTION_IP = 'cf-connecting-ip',
  AUTHORIZATION = 'authorization',
  X_ACCESS_TOKEN = 'x-access-token',
  X_API_KEY = 'x-api-key',
  X_WALLET_ID = 'x-wallet-uuid',
  X_LANG = 'x-lang',
  X_API_ID = 'x-api-id',
  X_DEVICE_ID = 'x-device-id',
  X_ENCRYPTED_BODY = 'x-encrypted-body',
  PRODUCT_ID = 'x-product-uuid',
  PRODUCT_TARGET_USER_ID = 'x-product-target-user-uuid',
}
