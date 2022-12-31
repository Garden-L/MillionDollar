const { Model, DataTypes } = require('sequelize');

class User extends Model{
    static init(sequelize){
        return super.init({
            id: {
                type: DataTypes.STRING(20),
                allowNull: false,
                primaryKey: true,
            },
            password: {
                type: DataTypes.STRING(128),
                allowNull: false,
            },
            email: {
                type: DataTypes.STRING(100),
                allowNull: false,
            },
            salt: {
                type: DataTypes.STRING(128),
                allowNull: false,
            },
        },
        {
            sequelize: sequelize,
            timestamps: true,
            createdAt: 'createAt',
            updatedAt: 'updateAt',
            tableName: 'Users',
        });
    }
}

module.exports = User;