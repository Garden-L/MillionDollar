const { Model, DataTypes } = require('sequelize');

class Marketprice extends Model{
    static init(sequelize){
        return super.init({
            stkCd: {
                type: DataTypes.STRING(6),
                primaryKey: true,
            },
            trDt:{
                type: DataTypes.DATEONLY,
                primaryKey: true,
            },
            trOpnPrc: {
                type: DataTypes.INTEGER,
            },
            trHgPrc: {
                type: DataTypes.INTEGER,
            },
            trLwPrc: {
                type: DataTypes.INTEGER,
            },
            trClsPrc: {
                type: DataTypes.INTEGER,
            },
            trVol: {
                type: DataTypes.INTEGER,
            },
            trTrans: {
                type: DataTypes.BIGINT,
            },
            lstShrs: {
                type: DataTypes.BIGINT,
            },
            mktCap: {
                type: DataTypes.BIGINT,
            },
            flwRt: {
                type: DataTypes.FLOAT,
            }
        },
        {
            sequelize,
            timestamps: false,
            tableName: 'marketprice',
        })
    }
}
module.exports = { Marketprice };