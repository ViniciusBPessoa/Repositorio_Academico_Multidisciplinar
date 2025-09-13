import validator from 'validator';

export const isEmail = (email: string): boolean => {
  return email && validator.isEmail(email);
};
