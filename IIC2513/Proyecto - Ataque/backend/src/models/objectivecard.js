const {
  Model,
} = require('sequelize');

module.exports = (sequelize, DataTypes) => {
  class ObjectiveCard extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      this.belongsTo(models.Player, {
        foreignKey: 'id',
      });
    }
  }
  ObjectiveCard.init({
    descripcion: DataTypes.STRING,
    playerId: DataTypes.INTEGER,
  }, {
    sequelize,
    modelName: 'ObjectiveCard',
  });
  return ObjectiveCard;
};
