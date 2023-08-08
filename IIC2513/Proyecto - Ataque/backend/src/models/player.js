const {
  Model,
} = require('sequelize');

module.exports = (sequelize, DataTypes) => {
  class Player extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      this.belongsTo(models.User, {
        foreignKey: 'id',
      });
      this.belongsTo(models.Game, {
        foreignKey: 'id',
      });
      this.hasOne(models.playerObjective, {
        foreignKey: 'id',
      });
      this.hasMany(models.PlayerTerritory, {
        foreignKey: 'id',
      });
    }
  }
  Player.init({
    color: DataTypes.STRING,
    userId: DataTypes.INTEGER,
    gameId: DataTypes.INTEGER,
  }, {
    sequelize,
    modelName: 'Player',
  });
  return Player;
};
