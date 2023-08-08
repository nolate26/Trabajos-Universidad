const {
  Model,
} = require('sequelize');

module.exports = (sequelize, DataTypes) => {
  class Territory extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      this.belongsTo(models.Game, {
        foreignKey: 'id',
      });
      this.hasMany(models.PlayerTerritory, {
        foreignKey: 'id',
      });
    }
  }
  Territory.init({
    value: DataTypes.INTEGER,
    name: DataTypes.STRING,
    faculty: DataTypes.STRING,
    neighbours: DataTypes.ARRAY(DataTypes.INTEGER),
  }, {
    sequelize,
    modelName: 'Territory',
  });
  return Territory;
};
