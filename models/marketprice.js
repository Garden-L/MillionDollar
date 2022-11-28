const { Model, DataTypes } = require('sequelize');

class Marketprice extends Model{
    static init(sequelize){
        super.init({
            stock_code: {
                type: DataTypes.STRING(6),
                unique: true,
                allowNull: false,
            },
            market_date:{
                type: DataTypes.DATEONLY,
            },
            open_price: {
                type: DataTypes.INTEGER,
            },
            close_price: {
                type: DataTypes.INTEGER,
            },
            high_price: {
                type: DataTypes.INTEGER,
            },
            low_prive: {
                type: DataTypes.INTEGER,
            },
            volume: {
                type: DataTypes.BIGINT,
            },
            transaction_price: {
                type: DataTypes.BIGINT,
            },
            total_shares: {
                type: DataTypes.BIGINT,
            },
            flow_shares: {
                type: DataTypes.BIGINT,
            }
        },
        {
            sequelize,
            timestamps: false,
            freezeTableName: true,
        })
    }
}
module.exports = { Marketprice };