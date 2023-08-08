/** @type {import('sequelize-cli').Migration} */
module.exports = {
  async up(queryInterface, Sequelize) {
    await queryInterface.bulkInsert('Territories', [
      {
        value: 1, name: 'Centro de innovación', faculty: 'rosado', neighbours: [2, 3, 25], createdAt: new Date(), updatedAt: new Date(),
      },
      {
        value: 2, name: 'Facultad de educación', faculty: 'rosado', neighbours: [1, 3, 4, 26], createdAt: new Date(), updatedAt: new Date(),
      },
      {
        value: 3, name: 'UC CHRISTUS', faculty: 'rosado', neighbours: [1, 2, 4], createdAt: new Date(), updatedAt: new Date(),
      },
      {
        value: 4, name: 'Facultad de letras', faculty: 'rosado', neighbours: [2, 3, 5], createdAt: new Date(), updatedAt: new Date(),
      },
      {
        value: 5, name: 'Facultad de economía y administración', faculty: 'azul', neighbours: [4, 6, 10], createdAt: new Date(), updatedAt: new Date(),
      },
      {
        value: 6, name: 'Facultad de teología', faculty: 'azul', neighbours: [5, 8, 9], createdAt: new Date(), updatedAt: new Date(),
      },
      {
        value: 7, name: 'Facultad de física', faculty: 'azul', neighbours: [8, 9, 20], createdAt: new Date(), updatedAt: new Date(),
      },
      {
        value: 8, name: 'Facultad de historia, geografia y ciencias políticas', faculty: 'azul', neighbours: [6, 7, 10, 15], createdAt: new Date(), updatedAt: new Date(),
      },
      {
        value: 9, name: 'Facultad de quimica', faculty: 'azul', neighbours: [6, 7, 20, 23], createdAt: new Date(), updatedAt: new Date(),
      },
      {
        value: 10, name: 'Edificio centro de medición MIDE UC', faculty: 'naranjo', neighbours: [5, 8, 11], createdAt: new Date(), updatedAt: new Date(),
      },
      {
        value: 11, name: 'Facultad de agronomía', faculty: 'naranjo', neighbours: [10, 12, 15], createdAt: new Date(), updatedAt: new Date(),
      },
      {
        value: 12, name: 'DECON', faculty: 'naranjo', neighbours: [11, 13], createdAt: new Date(), updatedAt: new Date(),
      },
      {
        value: 13, name: 'Servicios administracion campus', faculty: 'naranjo', neighbours: [12, 14], createdAt: new Date(), updatedAt: new Date(),
      },
      {
        value: 14, name: 'Punto Limpio Sibico', faculty: 'naranjo', neighbours: [13, 15, 16], createdAt: new Date(), updatedAt: new Date(),
      },
      {
        value: 15, name: 'Aulas Helen Lee Lassen', faculty: 'naranjo', neighbours: [8, 11, 14, 16], createdAt: new Date(), updatedAt: new Date(),
      },
      {
        value: 16, name: 'Piscina y camarines', faculty: 'verde', neighbours: [14, 15, 17], createdAt: new Date(), updatedAt: new Date(),
      },
      {
        value: 17, name: 'Canchas deporte', faculty: 'verde', neighbours: [16, 18, 19, 20], createdAt: new Date(), updatedAt: new Date(),
      },
      {
        value: 18, name: 'Escuela de medicina veterinaria', faculty: 'verde', neighbours: [2, 3, 25], createdAt: new Date(), updatedAt: new Date(),
      },
      {
        value: 19, name: 'Gimnasio Multipropósito', faculty: 'verde', neighbours: [17, 18], createdAt: new Date(), updatedAt: new Date(),
      },
      {
        value: 20, name: 'Facultad de matemática', faculty: 'amarillo', neighbours: [7, 9, 17, 21, 22], createdAt: new Date(), updatedAt: new Date(),
      },
      {
        value: 21, name: 'College UC', faculty: 'amarillo', neighbours: [20, 22], createdAt: new Date(), updatedAt: new Date(),
      },
      {
        value: 22, name: 'Facultad de Ingeniería', faculty: 'amarillo', neighbours: [20, 21, 23, 24], createdAt: new Date(), updatedAt: new Date(),
      },
      {
        value: 23, name: 'Edificio centro de excelencia docente', faculty: 'amarillo', neighbours: [9, 22], createdAt: new Date(), updatedAt: new Date(),
      },
      {
        value: 24, name: 'Edificio Andrónico Luksic Abaroa', faculty: 'amarillo', neighbours: [22, 25, 26], createdAt: new Date(), updatedAt: new Date(),
      },
      {
        value: 25, name: 'Edificio San agustin', faculty: 'amarillo', neighbours: [1, 24, 26], createdAt: new Date(), updatedAt: new Date(),
      },
      {
        value: 26, name: 'Escuela de construcción civil', faculty: 'amarillo', neighbours: [2, 24, 25], createdAt: new Date(), updatedAt: new Date(),
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
