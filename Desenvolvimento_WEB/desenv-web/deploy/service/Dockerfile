FROM node:lts-alpine AS builder

ARG SERVICE

RUN apk add --update python3 make g++ && rm -rf /var/cache/apk/*

USER node

WORKDIR /home/node

COPY package*.json ./

RUN npm ci

COPY . .

RUN echo 'Compiling ${SERVICE} microservice' && npm run build ${SERVICE}

# ---

FROM node:lts-alpine

ARG SERVICE

USER node

WORKDIR /home/node

RUN echo 'Building ${SERVICE} image'

COPY --from=builder /home/node/node_modules ./node_modules
COPY --from=builder /home/node/dist/apps/${SERVICE} ./dist

COPY config/database.js ./config/database.js
COPY apps/${SERVICE}/src/infrastructure/sequelize ./sequelize

COPY deploy/service/run-service.sh ./
COPY deploy/service/.sequelizerc ./

CMD ["./run-service.sh", "dist/main.js"]
