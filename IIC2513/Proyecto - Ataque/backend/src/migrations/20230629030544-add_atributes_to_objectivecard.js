/** @type {import('sequelize-cli').Migration} */
module.exports = {
  async up(queryInterface, Sequelize) {
    await queryInterface.addColumn('ObjectiveCards', 'type', {
      type: Sequelize.INTEGER,
    });
    await queryInterface.addColumn('ObjectiveCards', 'to_attack', {
      type: Sequelize.ARRAY(Sequelize.INTEGER),
    });
    /**
     * Add altering commands here.
     *
     * Example:
     * await queryInterface.createTable('users', { id: Sequelize.INTEGER });
     */
  },

  async down(queryInterface, Sequelize) {
    /**
     * Add reverting commands here.
     *
     * Example:
     * await queryInterface.dropTable('users');
     */
  },
};