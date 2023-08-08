/** @type {import('sequelize-cli').Migration} */
module.exports = {
  async up(queryInterface, Sequelize) {
    await queryInterface.bulkInsert('Games', [
      {
        state: 'en juego', turn: 1, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        state: 'en juego', turn: 1, createdAt: new Date(), updatedAt: new Date(),
      },
    ], {});
    await queryInterface.bulkInsert('Players', [
      {
        userId: 1, gameId: 1, color: 'red', objectiveId: 1, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        userId: 2, gameId: 1, color: 'blue', objectiveId: 2, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        userId: 3, gameId: 1, color: 'green', objectiveId: 3, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        userId: 4, gameId: 1, color: 'orange', objectiveId: 4, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        userId: 1, gameId: 2, color: 'red', objectiveId: 1, createdAt: new Date(), updatedAt: new Date(),
      },
    ], {});
    await queryInterface.bulkInsert('playerObjectives', [
      {
        objectiveId: 1, playerId: 1, type: 1, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        objectiveId: 2, playerId: 2, type: 1, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        objectiveId: 3, playerId: 3, type: 1, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        objectiveId: 3, playerId: 4, type: 2, createdAt: new Date(), updatedAt: new Date(),
      },
    ], {});
    await queryInterface.bulkInsert('ConquerObjectives', [
      {
        description: 'conquistar Deportes', to_attack: [16, 17, 18, 19], createdAt: new Date(), updatedAt: new Date(),
      },
      {
        description: 'conquistar Humanidades', to_attack: [5, 6, 7, 8, 9], createdAt: new Date(), updatedAt: new Date(),
      },
      {
        description: 'conquistar Ingenieria', to_attack: [20, 21, 22, 23, 24, 25], createdAt: new Date(), updatedAt: new Date(),
      },
      {
        description: 'conquistar Innovación', to_attack: [1, 2, 3, 4], createdAt: new Date(), updatedAt: new Date(),
      },
    ], {});
  },

  async down(queryInterface, Sequelize) {
    /**
     * Add commands to revert seed here.
     *
     * Example:
     * await queryInterface.bulkDelete('People', null, {});
     */
  },
};
