const { Model, DataTypes } = require('sequelize');

class PrefixSumNetPurchase extends Model{
    static init(sequelize){
        return super.init({
            stkCd: {
                type: DataTypes.STRING(6),
                primaryKey: true,
                allowNull: false,
            },
            bsDt:{
                type: DataTypes.DATEONLY,
                primaryKey: true,
                allowNull: false,
            },

            //순매수 5일 누적 거래대금
            trans_indi_5: {
                type: DataTypes.BIGINT,
            },
            trans_inst_5: {
                type: DataTypes.BIGINT,
            },
            trans_corp_5: {
                type: DataTypes.BIGINT,
            },
            trans_fore_5: {
                type: DataTypes.BIGINT,
            },

            //순매수 10일 누적 거래대금
            trans_indi_10: {
                type: DataTypes.BIGINT,
            },
            trans_inst_10: {
                type: DataTypes.BIGINT,
            },
            trans_corp_10: {
                type: DataTypes.BIGINT,
            },
            trans_fore_10: {
                type: DataTypes.BIGINT,
            },
            
            //순매수 20일 누적 거래대금
            trans_indi_20: {
                type: DataTypes.BIGINT,
            },
            trans_inst_20: {
                type: DataTypes.BIGINT,
            },
            trans_corp_20: {
                type: DataTypes.BIGINT,
            },
            trans_fore_20: {
                type: DataTypes.BIGINT,
            },

            //순매수 30일 누적 거래대금
            trans_indi_30: {
                type: DataTypes.BIGINT,
            },
            trans_inst_30: {
                type: DataTypes.BIGINT,
            },
            trans_corp_30: {
                type: DataTypes.BIGINT,
            },
            trans_fore_30: {
                type: DataTypes.BIGINT,
            },

            //순매수 60일 누적 거래대금
            trans_indi_60: {
                type: DataTypes.BIGINT,
            },
            trans_inst_60: {
                type: DataTypes.BIGINT,
            },
            trans_corp_60: {
                type: DataTypes.BIGINT,
            },
            trans_fore_60: {
                type: DataTypes.BIGINT,
            },

            //순매수 5일 누적 거래대금
            trans_indi_120: {
                type: DataTypes.BIGINT,
            },
            trans_inst_120: {
                type: DataTypes.BIGINT,
            },
            trans_corp_120: {
                type: DataTypes.BIGINT,
            },
            trans_fore_120: {
                type: DataTypes.BIGINT,
            },

            //순매수 5일 누적 거래량
            vol_indi_5: {
                type: DataTypes.BIGINT,
            },
            vol_inst_5: {
                type: DataTypes.BIGINT,
            },
            vol_corp_5: {
                type: DataTypes.BIGINT,
            },
            vol_fore_5: {
                type: DataTypes.BIGINT,
            },

            //순매수 10일 누적 거래량
            vol_indi_10: {
                type: DataTypes.BIGINT,
            },
            vol_inst_10: {
                type: DataTypes.BIGINT,
            },
            vol_corp_10: {
                type: DataTypes.BIGINT,
            },
            vol_fore_10: {
                type: DataTypes.BIGINT,
            },
            
            //순매수 20일 누적 거래량
            vol_indi_20: {
                type: DataTypes.BIGINT,
            },
            vol_inst_20: {
                type: DataTypes.BIGINT,
            },
            vol_corp_20: {
                type: DataTypes.BIGINT,
            },
            vol_fore_20: {
                type: DataTypes.BIGINT,
            },

            //순매수 30일 누적 거래량
            vol_indi_30: {
                type: DataTypes.BIGINT,
            },
            vol_inst_30: {
                type: DataTypes.BIGINT,
            },
            vol_corp_30: {
                type: DataTypes.BIGINT,
            },
            vol_fore_30: {
                type: DataTypes.BIGINT,
            },

            //순매수 60일 누적 거래량
            vol_indi_60: {
                type: DataTypes.BIGINT,
            },
            vol_inst_60: {
                type: DataTypes.BIGINT,
            },
            vol_corp_60: {
                type: DataTypes.BIGINT,
            },
            vol_fore_60: {
                type: DataTypes.BIGINT,
            },

            //순매수 120일 누적 거래량
            vol_indi_120: {
                type: DataTypes.BIGINT,
            },
            vol_inst_120: {
                type: DataTypes.BIGINT,
            },
            vol_corp_120: {
                type: DataTypes.BIGINT,
            },
            vol_fore_120: {
                type: DataTypes.BIGINT,
            },

            // 평균 n일 유동 시가총액
            avg_mktcap_5: {
                type: DataTypes.BIGINT,
            },
            avg_mktcap_10: {
                type: DataTypes.BIGINT,
            },
            avg_mktcap_20: {
                type: DataTypes.BIGINT,
            },
            avg_mktcap_30: {
                type: DataTypes.BIGINT,
            },
            avg_mktcap_60: {
                type: DataTypes.BIGINT,
            },
            avg_mktcap_120: {
                type: DataTypes.BIGINT,
            },

            // 평균 n일 유동 주식
            avg_shrs_5: {
                type: DataTypes.BIGINT,
            },
            avg_shrs_10: {
                type: DataTypes.BIGINT,
            },
            avg_shrs_20: {
                type: DataTypes.BIGINT,
            },
            avg_shrs_30: {
                type: DataTypes.BIGINT,
            },
            avg_shrs_60: {
                type: DataTypes.BIGINT,
            },
            avg_shrs_120: {
                type: DataTypes.BIGINT,
            },
        },
        {
            sequelize: sequelize,
            timestamps: false,
            tableName: 'PrefixSumNetPurchase',
        });
    }
}


module.exports = PrefixSumNetPurchase;