const { Model, DataTypes } = require('sequelize');

class Investor extends Model{
    static init(sequelize){
        return super.init({
            stkCd: {
                type: DataTypes.STRING(6),
                primaryKey: true,
                allowNull: false,
                unique: true,
            },
            trDt: {
                type: DataTypes.DATEONLY,
                primaryKey: true,
                allowNull: false,
                unique: true,
            },
            vol_fin_sell: {
                type: DataTypes.INTEGER,
            },
            vol_insur_sell: {
                type: DataTypes.INTEGER,
            },
            vol_inves_sell: {
                type: DataTypes.INTEGER,
            },
            vol_priv_sell: {
                type: DataTypes.INTEGER,
            },
            vol_bank_sell: {
                type: DataTypes.INTEGER,
            },
            vol_othFin_sell: {
                type: DataTypes.INTEGER,
            },
            vol_othFund_sell: {
                type: DataTypes.INTEGER,
            },
            vol_othCorp_sell: {
                type: DataTypes.INTEGER,
            },
            vol_indi_sell: {
                type: DataTypes.INTEGER,
            },
            vol_fore_sell: {
                type: DataTypes.INTEGER,
            },
            vol_othFore_sell: {
                type: DataTypes.INTEGER,
            },

            // vol_name_buy
            vol_fin_buy: {
                type: DataTypes.INTEGER,
            },
            vol_insur_buy: {
                type: DataTypes.INTEGER,
            },
            vol_inves_buy: {
                type: DataTypes.INTEGER,
            },
            vol_priv_buy: {
                type: DataTypes.INTEGER,
            },
            vol_bank_buy: {
                type: DataTypes.INTEGER,
            },
            vol_othFin_buy: {
                type: DataTypes.INTEGER,
            },
            vol_othFund_buy: {
                type: DataTypes.INTEGER,
            },
            vol_othCorp_buy: {
                type: DataTypes.INTEGER,
            },
            vol_indi_buy: {
                type: DataTypes.INTEGER,
            },
            vol_fore_buy: {
                type: DataTypes.INTEGER,
            },
            vol_othFore_buy: {
                type: DataTypes.INTEGER,
            },


            // vol_name_net
            vol_fin_net: {
                type: DataTypes.INTEGER,
            },
            vol_insur_net: {
                type: DataTypes.INTEGER,
            },
            vol_inves_net: {
                type: DataTypes.INTEGER,
            },
            vol_priv_net: {
                type: DataTypes.INTEGER,
            },
            vol_bank_net: {
                type: DataTypes.INTEGER,
            },
            vol_othFin_net: {
                type: DataTypes.INTEGER,
            },
            vol_othFund_net: {
                type: DataTypes.INTEGER,
            },
            vol_othCorp_net: {
                type: DataTypes.INTEGER,
            },
            vol_indi_net: {
                type: DataTypes.INTEGER,
            },
            vol_fore_net: {
                type: DataTypes.INTEGER,
            },
            vol_othFore_net: {
                type: DataTypes.INTEGER,
            },

            // trans_name_sell
            trans_fin_sell: {
                type: DataTypes.BIGINT,
            },
            trans_insur_sell: {
                type: DataTypes.BIGINT,
            },
            trans_inves_sell: {
                type: DataTypes.BIGINT,
            },
            trans_priv_sell: {
                type: DataTypes.BIGINT,
            },
            trans_bank_sell: {
                type: DataTypes.BIGINT,
            },
            trans_othFin_sell: {
                type: DataTypes.BIGINT,
            },
            trans_othFund_sell: {
                type: DataTypes.BIGINT,
            },
            trans_othCorp_sell: {
                type: DataTypes.BIGINT,
            },
            trans_indi_sell: {
                type: DataTypes.BIGINT,
            },
            trans_fore_sell: {
                type: DataTypes.BIGINT,
            },
            trans_othFore_sell: {
                type: DataTypes.BIGINT,
            },

            // trans_name_buy
            trans_fin_buy: {
                type: DataTypes.BIGINT,
            },
            trans_insur_buy: {
                type: DataTypes.BIGINT,
            },
            trans_inves_buy: {
                type: DataTypes.BIGINT,
            },
            trans_priv_buy: {
                type: DataTypes.BIGINT,
            },
            trans_bank_buy: {
                type: DataTypes.BIGINT,
            },
            trans_othFin_buy: {
                type: DataTypes.BIGINT,
            },
            trans_othFund_buy: {
                type: DataTypes.BIGINT,
            },
            trans_othCorp_buy: {
                type: DataTypes.BIGINT,
            },
            trans_indi_buy: {
                type: DataTypes.BIGINT,
            },
            trans_fore_buy: {
                type: DataTypes.BIGINT,
            },
            trans_othFore_buy: {
                type: DataTypes.BIGINT,
            },


            // trans_name_net
            trans_fin_net: {
                type: DataTypes.BIGINT,
            },
            trans_insur_net: {
                type: DataTypes.BIGINT,
            },
            trans_inves_net: {
                type: DataTypes.BIGINT,
            },
            trans_priv_net: {
                type: DataTypes.BIGINT,
            },
            trans_bank_net: {
                type: DataTypes.BIGINT,
            },
            trans_othFin_net: {
                type: DataTypes.BIGINT,
            },
            trans_othFund_net: {
                type: DataTypes.BIGINT,
            },
            trans_othCorp_net: {
                type: DataTypes.BIGINT,
            },
            trans_indi_net: {
                type: DataTypes.BIGINT,
            },
            trans_fore_net: {
                type: DataTypes.BIGINT,
            },
            trans_othFore_net: {
                type: DataTypes.BIGINT,
            },
        },
        {
            sequelize,
            tableName: "Investor",
            timestamps: false,
        })
    }
}

module.exports = { Investor };