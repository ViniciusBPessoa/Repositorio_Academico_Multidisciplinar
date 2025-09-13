#!/bin/sh

env

cat /etc/hosts

if [[ "${APP_DATABASE_MIGRATION_HOST}" ]]; then
  npx sequelize db:migrate
  npx sequelize db:seed:all
fi

node $1
