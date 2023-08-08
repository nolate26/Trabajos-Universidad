/** @type {import('sequelize-cli').Migration} */
module.exports = {
  async up(queryInterface, Sequelize) {
    await queryInterface.addColumn('Territories', 'gameId', {
      type: Sequelize.INTEGER,
      references: { model: 'Games', key: 'id' },
    });
    await queryInterface.removeColumn('Territories', 'mapId');
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
