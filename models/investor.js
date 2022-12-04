const { Model, DataTypes } = require('sequelize');

class Investor extends Model{
    static init(sequelize){
        super.init({
            stock_code: {
                type: DataTypes.STRING(6),
                allowNull: false,
            },
            trade_date: {
                type: DataTypes.DATEONLY,
                allowNull: false,
            },
            volume_finance_sell: {
                type: DataTypes.BIGINT,
            },
            volume_insurance_sell: {
                type: DataTypes.BIGINT,
            },
            volume_investortrust_sell: {
                type: DataTypes.BIGINT,
            },
            volume_private_sell: {
                type: DataTypes.BIGINT,
            },
            volume_bank_sell: {
                type: DataTypes.BIGINT,
            },
            volume_otherfinance_sell: {
                type: DataTypes.BIGINT,
            },
            volume_otherfund_sell: {
                type: DataTypes.BIGINT,
            },
            volume_othercorporation_sell: {
                type: DataTypes.BIGINT,
            },
            volume_individual_sell: {
                type: DataTypes.BIGINT,
            },
            volume_foreigner_sell: {
                type: DataTypes.BIGINT,
            },
            volume_0therforigner_sell: {
                type: DataTypes.BIGINT,
            },

            // volume_name_buy
            volume_finance_buy: {
                type: DataTypes.BIGINT,
            },
            volume_insurance_buy: {
                type: DataTypes.BIGINT,
            },
            volume_investortrust_buy: {
                type: DataTypes.BIGINT,
            },
            volume_private_buy: {
                type: DataTypes.BIGINT,
            },
            volume_bank_buy: {
                type: DataTypes.BIGINT,
            },
            volume_otherfinance_buy: {
                type: DataTypes.BIGINT,
            },
            volume_otherfund_buy: {
                type: DataTypes.BIGINT,
            },
            volume_othercorporation_buy: {
                type: DataTypes.BIGINT,
            },
            volume_individual_buy: {
                type: DataTypes.BIGINT,
            },
            volume_foreigner_buy: {
                type: DataTypes.BIGINT,
            },
            volume_otherforigner_buy: {
                type: DataTypes.BIGINT,
            },


            // volume_name_net
            volume_finance_net: {
                type: DataTypes.BIGINT,
            },
            volume_insurance_net: {
                type: DataTypes.BIGINT,
            },
            volume_investortrust_net: {
                type: DataTypes.BIGINT,
            },
            volume_private_net: {
                type: DataTypes.BIGINT,
            },
            volume_bank_net: {
                type: DataTypes.BIGINT,
            },
            volume_otherfinance_net: {
                type: DataTypes.BIGINT,
            },
            volume_otherfund_net: {
                type: DataTypes.BIGINT,
            },
            volume_othercorporation_net: {
                type: DataTypes.BIGINT,
            },
            volume_individual_net: {
                type: DataTypes.BIGINT,
            },
            volume_foreigner_net: {
                type: DataTypes.BIGINT,
            },
            volume_otherforigner_net: {
                type: DataTypes.BIGINT,
            },

            // tradevalue_name_sell
            tradevalue_finance_sell: {
                type: DataTypes.BIGINT,
            },
            tradevalue_insurance_sell: {
                type: DataTypes.BIGINT,
            },
            tradevalue_investortrust_sell: {
                type: DataTypes.BIGINT,
            },
            tradevalue_private_sell: {
                type: DataTypes.BIGINT,
            },
            tradevalue_bank_sell: {
                type: DataTypes.BIGINT,
            },
            tradevalue_otherfinance_sell: {
                type: DataTypes.BIGINT,
            },
            tradevalue_otherfund_sell: {
                type: DataTypes.BIGINT,
            },
            tradevalue_othercorporation_sell: {
                type: DataTypes.BIGINT,
            },
            tradevalue_individual_sell: {
                type: DataTypes.BIGINT,
            },
            tradevalue_foreigner_sell: {
                type: DataTypes.BIGINT,
            },
            tradevalue_0therforigner_sell: {
                type: DataTypes.BIGINT,
            },

            // tradevalue_name_buy
            tradevalue_finance_buy: {
                type: DataTypes.BIGINT,
            },
            tradevalue_insurance_buy: {
                type: DataTypes.BIGINT,
            },
            tradevalue_investortrust_buy: {
                type: DataTypes.BIGINT,
            },
            tradevalue_private_buy: {
                type: DataTypes.BIGINT,
            },
            tradevalue_bank_buy: {
                type: DataTypes.BIGINT,
            },
            tradevalue_otherfinance_buy: {
                type: DataTypes.BIGINT,
            },
            tradevalue_otherfund_buy: {
                type: DataTypes.BIGINT,
            },
            tradevalue_othercorporation_buy: {
                type: DataTypes.BIGINT,
            },
            tradevalue_individual_buy: {
                type: DataTypes.BIGINT,
            },
            tradevalue_foreigner_buy: {
                type: DataTypes.BIGINT,
            },
            tradevalue_otherforigner_buy: {
                type: DataTypes.BIGINT,
            },


            // tradevalue_name_net
            tradevalue_finance_net: {
                type: DataTypes.BIGINT,
            },
            tradevalue_insurance_net: {
                type: DataTypes.BIGINT,
            },
            tradevalue_investortrust_net: {
                type: DataTypes.BIGINT,
            },
            tradevalue_private_net: {
                type: DataTypes.BIGINT,
            },
            tradevalue_bank_net: {
                type: DataTypes.BIGINT,
            },
            tradevalue_otherfinance_net: {
                type: DataTypes.BIGINT,
            },
            tradevalue_otherfund_net: {
                type: DataTypes.BIGINT,
            },
            tradevalue_othercorporation_net: {
                type: DataTypes.BIGINT,
            },
            tradevalue_individual_net: {
                type: DataTypes.BIGINT,
            },
            tradevalue_foreigner_net: {
                type: DataTypes.BIGINT,
            },
            tradevalue_otherforigner_net: {
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