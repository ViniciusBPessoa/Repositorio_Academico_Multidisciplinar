'use strict';

const bcrypt = require('bcrypt');

const ID = '75b76701-3bb7-465d-9d23-ebecfde98bee';
const PASSWORD = '007GoldenEye';
const APP_API_USERS_SALT_ROUNDS = 10;
const CREATED_AT = new Date();
const UPDATED_AT = CREATED_AT;  

/** @type {import('sequelize-cli').Migration} */
module.exports = {
  async up (queryInterface, Sequelize) {
    const transaction = await queryInterface.sequelize.transaction(); 

    try {
      await queryInterface.bulkInsert(
        'users', 
        [{
          id: ID,
          name: 'John Doe',
          email: 'john.doe@example.com',  
          password: bcrypt.hashSync(PASSWORD, APP_API_USERS_SALT_ROUNDS),
          createdAt: CREATED_AT,
          updatedAt: UPDATED_AT,
        }], 
        { transaction }
      );

      await transaction.commit();
    } catch (error) {
      await transaction.rollback();
      console.error(error);
      throw error;
    }
  },

  async down (queryInterface, Sequelize) {
    const transaction = await queryInterface.sequelize.transaction();

    try {
      await queryInterface.bulkDelete('users', { id: ID }, { transaction });
      await transaction.commit();
    } catch (error) {
      await transaction.rollback();
      console.error(error);
      throw error;
    }
  }
};
