require('dotenv').config();

const options = {
  port: process.env.APP_DATABASE_PORT,
  schema: process.env.APP_DATABASE_SCHEMA,
  database: process.env.APP_DATABASE_DATABASE,
  host: process.env.APP_DATABASE_HOST,
  password: process.env.APP_DATABASE_PASSWORD,
  username: process.env.APP_DATABASE_USERNAME,
  dialect: 'postgres',
  migrationStorageTableName: process.env.APP_DATABASE_MIGRATION_TABLE,
  seederStorage: 'sequelize',
  seederStorageTableName: process.env.APP_DATABASE_SEEDERS_TABLE,
  logging: process.env.APP_DATABASE_LOG === 'true',
  dialectOptions: {
    ssl:
      process.env.APP_DATABASE_SSL === 'true'
        ? { rejectUnauthorized: false }
        : false,
  },
};

module.exports = options;
