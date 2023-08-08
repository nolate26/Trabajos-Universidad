const {
  Model,
} = require('sequelize');

module.exports = (sequelize, DataTypes) => {
  class User extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      this.hasMany(models.Player, {
        foreignKey: 'id',
      });
    }
  }
  User.init({
    name: {
      type: DataTypes.STRING,
      validate: {
        isAlphanumeric: {
          msg: 'Name must be alphanumeric',
        },
      },
    },
    lastName: {
      type: DataTypes.STRING,
      validate: {
        isAlphanumeric: {
          msg: 'Lastname must be alphanumeric',
        },
      },
    },
    mail: {
      type: DataTypes.STRING,
      validate: {
        isEmail: {
          msg: 'mail must have email format',
        },
      },
    },
    password: {
      type: DataTypes.STRING,
      validate: {
        isValidPassword(value) {
          if (!value.match(/[a-z]/) || !value.match(/[0-9]/) || !value.match(/[@$!%*?&]/)) {
            throw new Error('The password must contain at least, one number and one special caracter');
          }
        },
      },
    },
    image: DataTypes.STRING,
    birthday: DataTypes.DATE,
  }, {
    sequelize,
    modelName: 'User',
  });
  return User;
};
