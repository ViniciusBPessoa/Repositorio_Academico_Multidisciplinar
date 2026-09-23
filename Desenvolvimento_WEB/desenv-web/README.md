# Desenvolvimento Web: API de Usuários com Microsserviços (NestJS)

Projeto de exemplo da disciplina de **Desenvolvimento Web**, baseado no modelo apresentado pelo professor. É uma API de usuários organizada em **microsserviços** com NestJS, seguindo **Clean Architecture**, com PostgreSQL e comunicação entre os serviços por **NATS**.

## Arquitetura

O repositório é um monorepo NestJS com dois apps e uma biblioteca compartilhada:

| Pasta | Papel |
|---|---|
| `apps/api-users` | **gateway HTTP**: recebe as requisições REST, faz a autenticação (JWT/Passport) e repassa os comandos ao serviço de usuários via NATS |
| `apps/users` | **microsserviço de usuários**: regras de negócio e acesso ao banco com Sequelize |
| `libs/common` | código compartilhado: decorators, interceptors, filtros de exceção, middlewares e módulos comuns |

O serviço `users` segue as camadas `domain` (entidades e repositórios), `application` (casos de uso e serviços), `infrastructure` (NestJS, Sequelize e NATS) e `interface` (controllers e eventos). O `api-users` concentra tudo na camada `infrastructure` (controllers HTTP, autenticação e cliente NATS).

### Casos de uso do serviço de usuários

Criar usuário, atualizar, trocar a senha, buscar por ID, buscar por e-mail e listar todos.

### Rotas HTTP (`api-users`)

| Método | Rota | O que faz |
|---|---|---|
| `POST` | `/auth/signin` | login e geração do token JWT |
| `POST` | `/auth/password` | troca de senha |

O arquivo `endpoint.constants.ts` também já declara as rotas `users` e `users/:id`.

## Infraestrutura

O `docker-compose.yml` sobe:

- **nats**: servidor de mensageria (portas 4222, 6222 e 8222).
- **db**: PostgreSQL (porta 5432).
- **users**: microsserviço de usuários.
- **api-users**: API HTTP na porta **3000**.

As migrations e os seeders do Sequelize ficam em `apps/users/src/infrastructure/sequelize`, e o script `migrate.sh` aplica as migrations para cada arquivo de ambiente no formato `.<nome>.env` (por exemplo, `.local.env`).

## Como executar

1. Crie um arquivo `.env` na raiz com as variáveis do banco e o segredo do JWT:

   ```
   POSTGRES_USER=...
   POSTGRES_PASSWORD=...
   POSTGRES_DB=...
   API_USERS_APP_JWT_TOKEN=...
   ```

2. Suba tudo com Docker:

   ```bash
   docker compose --profile local up --build
   ```

   Para subir só a infraestrutura (NATS e banco) e rodar os apps localmente:

   ```bash
   docker compose --profile infra up
   npm install
   npm run start:dev              # sobe o api-users (projeto padrão)
   npx nest start users --watch   # sobe o serviço de usuários
   ```

   Nesse modo, as variáveis `APP_*` de cada serviço (veja o `docker-compose.yml`) precisam estar definidas no ambiente.

## Tecnologias

TypeScript · NestJS · Sequelize · PostgreSQL · NATS · JWT/Passport · Docker · Biome/ESLint
