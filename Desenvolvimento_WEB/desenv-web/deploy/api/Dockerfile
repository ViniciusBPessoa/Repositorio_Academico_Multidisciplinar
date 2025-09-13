FROM node:lts-alpine AS builder

ARG SERVICE

RUN apk update && \
    apk upgrade && \
    apk add --no-cache python3 make g++ && \
    rm -rf /var/cache/apk/*

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
COPY --from=builder /home/node/dist/apps/${SERVICE} ./dist/

CMD ["node", "dist/main.js"]
