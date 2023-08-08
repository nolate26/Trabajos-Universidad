/** @type {import('sequelize-cli').Migration} */
module.exports = {
  async up(queryInterface, Sequelize) {
    await queryInterface.createTable('Territories', {
      id: {
        allowNull: false,
        autoIncrement: true,
        primaryKey: true,
        type: Sequelize.INTEGER,
      },
      armies: {
        type: Sequelize.INTEGER,
      },
      mapId: {
        type: Sequelize.INTEGER,
        references: { model: 'Maps', key: 'id' },
      },
      name: {
        type: Sequelize.STRING,
      },
      faculty: {
        type: Sequelize.STRING,
      },
      neighbours: {
        type: Sequelize.ARRAY(Sequelize.INTEGER),
      },
      createdAt: {
        allowNull: false,
        type: Sequelize.DATE,
      },
      updatedAt: {
        allowNull: false,
        type: Sequelize.DATE,
      },
    });
  },
  async down(queryInterface, Sequelize) {
    await queryInterface.dropTable('Territories');
  },
};
