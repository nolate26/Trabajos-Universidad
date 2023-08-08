/** @type {import('sequelize-cli').Migration} */
module.exports = {
  async up(queryInterface, Sequelize) {
    await queryInterface.bulkInsert('PlayerTerritories', [
      {
        armies: 2, owner: 1, gameId: 1, territoryId: 1, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 1, gameId: 1, territoryId: 2, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 1, gameId: 1, territoryId: 3, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 1, gameId: 1, territoryId: 4, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 1, gameId: 1, territoryId: 5, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 2, gameId: 1, territoryId: 6, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 2, gameId: 1, territoryId: 7, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 2, gameId: 1, territoryId: 8, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 2, gameId: 1, territoryId: 9, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 2, gameId: 1, territoryId: 10, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 2, gameId: 1, territoryId: 11, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 2, gameId: 1, territoryId: 12, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 3, gameId: 1, territoryId: 13, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 3, gameId: 1, territoryId: 14, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 3, gameId: 1, territoryId: 15, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 3, gameId: 1, territoryId: 16, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 3, gameId: 1, territoryId: 17, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 3, gameId: 1, territoryId: 18, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 3, gameId: 1, territoryId: 19, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 4, gameId: 1, territoryId: 20, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 4, gameId: 1, territoryId: 21, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 4, gameId: 1, territoryId: 22, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 4, gameId: 1, territoryId: 23, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 4, gameId: 1, territoryId: 24, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 4, gameId: 1, territoryId: 25, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 4, gameId: 1, territoryId: 26, createdAt: new Date(), updatedAt: new Date(),
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
