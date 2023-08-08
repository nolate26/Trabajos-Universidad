const {
  Model,
} = require('sequelize');

module.exports = (sequelize, DataTypes) => {
  class playerObjective extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      this.belongsTo(models.Player, {
        foreignKey: 'id',
      });
      // define association here
    }
  }
  playerObjective.init({
    playerId: DataTypes.INTEGER,
    type: DataTypes.INTEGER,
    objectiveId: DataTypes.INTEGER,
  }, {
    sequelize,
    modelName: 'playerObjective',
  });
  return playerObjective;
};
