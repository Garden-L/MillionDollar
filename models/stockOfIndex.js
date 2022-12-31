const { Model, DataTypes } = require('sequelize');

class StockOfIndex extends Model{
    static init(sequelize){
        return super.init({
            mktCd: {
                type: DataTypes.STRING(2),
            },
            sctCd: {
                type: DataTypes.STRING(5),
            },
            stkCd: {
                type: DataTypes.STRING(6),
            },
            atDt: {
                type: DataTypes.DATEONLY,
            }
        },
        {
            sequelize: sequelize,
            tableName: 'stockinindex',
            timestamps: false,
        });
    }
}

module.exports = StockOfIndex;