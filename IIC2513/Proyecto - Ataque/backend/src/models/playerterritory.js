const {
  Model,
} = require('sequelize');

module.exports = (sequelize, DataTypes) => {
  class PlayerTerritory extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      this.belongsTo(models.Player, {
        foreignKey: 'id',
      });
      this.belongsTo(models.Game, {
        foreignKey: 'id',
      });
      this.belongsTo(models.Territory, {
        foreignKey: 'id',
      });
      // define association here
    }
  }
  PlayerTerritory.init({
    owner: DataTypes.INTEGER,
    armies: DataTypes.INTEGER,
    gameId: DataTypes.INTEGER,
    territoryId: DataTypes.INTEGER,
  }, {
    sequelize,
    modelName: 'PlayerTerritory',
  });
  return PlayerTerritory;
};
