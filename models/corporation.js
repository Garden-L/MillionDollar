const { Model, DataTypes } = require('sequelize');

class Corporation extends Model {
    static init(sequelize) {
        return super.init({
            stock_code : {
                type: DataTypes.STRING(6),
                allowNull: true,
                unique: true,
            },
            name : {
                type: DataTypes.STRING(100),
                allowNull: false,
                unique: false,
            },
            listed_date : {
                type : DataTypes.DATEONLY,
                allowNull: false,
            },
            market : {
                type: DataTypes.STRING(30),
                unique: false,
            },
        },
        {
            sequelize,
            timestamps: false,
            freezeTableName: true,
        })
    }
}

module.exports = { Corporation };