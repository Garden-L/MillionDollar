const { Model, DataTypes } = require('sequelize');

class IndexInfo extends Model{
    static init(sequelize){
        return super.init({
            mktCd: {
                type: DataTypes.STRING(2),
            },
            mktNm: {
                type: DataTypes.STRING(10)
            },
            sctCd: {
                type: DataTypes.STRING(5),
            },
            sctNm: {
                type: DataTypes.STRING(100),
            },
            mktSrtNm:{
                type: DataTypes.STRING(5),
            }
        },
        {
            sequelize: sequelize,
            tableName: 'index_information',
            timestamps: false,
        });
    }
}

module.exports = IndexInfo;