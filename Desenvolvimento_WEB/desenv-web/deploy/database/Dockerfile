FROM postgres:16-bookworm


RUN echo 'CREATE EXTENSION "uuid-ossp";' > /docker-entrypoint-initdb.d/1-enable-uuid.sql
