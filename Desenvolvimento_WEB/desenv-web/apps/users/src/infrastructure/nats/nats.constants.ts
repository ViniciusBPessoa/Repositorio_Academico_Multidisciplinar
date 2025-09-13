export const NATS_SERVICES = {
  USER: {
    GET_BY_EMAIL: 'USERS.user.getByEmail',
    UPDATE: 'USERS.user.update',
    CREATE: 'USERS.user.create',
    CHANGE_PASSWORD: 'USERS.user.changePassword',
    GET_BY_ID: 'USERS.user.getById',
    GET_ALL: 'USERS.user.getAll',
  },
};

export const NATS_EVENTS = {
  USER: {
    UPDATED: 'USERS.user.event.updated',
    CREATED: 'USERS.user.event.created',
    UPDATED_PASSWORD: 'USERS.user.event.updatedPassword',
  },
};
