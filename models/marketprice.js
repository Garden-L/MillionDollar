const { Model, DataTypes } = require('sequelize');

class Marketprice extends Model{
    static init(sequelize){
        super.init({
            trade_date:{
                type: DataTypes.DATEONLY,
            },
            stk_code: {
                type: DataTypes.STRING(6),
                unique: true,
                allowNull: false,
            },
            trade_open_price: {
                type: DataTypes.INTEGER,
            },
            trade_high_price: {
                type: DataTypes.INTEGER,
            },
            trade_low_price: {
                type: DataTypes.INTEGER,
            },
            trade_close_price: {
                type: DataTypes.INTEGER,
            },
            trade_fruc_rate: {
                type: DataTypes.FLOAT,
            },
            trade_volume: {
                type: DataTypes.BIGINT,
            },
            trade_value: {
                type: DataTypes.BIGINT,
            },
            list_shares: {
                type: DataTypes.BIGINT,
            },
            mkt_capital: {
                type: DataTypes.BIGINT,
            },
            flow_rate: {
                type: DataTypes.FLOAT,
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