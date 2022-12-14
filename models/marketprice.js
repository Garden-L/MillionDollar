const { Model, DataTypes } = require('sequelize');

class Marketprice extends Model{
    static init(sequelize){
        super.init({
            stk_code: {
                type: DataTypes.STRING(6),
                primaryKey: true,
            },
            tr_date:{
                type: DataTypes.DATEONLY,
                primaryKey: true,
            },
            tr_opnprc: {
                type: DataTypes.INTEGER,
            },
            tr_hgprc: {
                type: DataTypes.INTEGER,
            },
            tr_lwprc: {
                type: DataTypes.INTEGER,
            },
            tr_clsprc: {
                type: DataTypes.INTEGER,
            },
            tr_volume: {
                type: DataTypes.BIGINT,
            },
            tr_value: {
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
            tableName: 'marketprices',
        })
    }
}
module.exports = { Marketprice };