const { Model, DataTypes } = require('sequelize');

class Investor extends Model{
    static init(sequelize){
        super.init({
            stock_code: {
                type: DataTypes.STRING(6),
                unique: true,
                allowNull: false,
            },
            volume_finance_buy: {
                type: DataTypes.BIGINT,
            },
            volume_finance_sell: {
                type: DataTypes.BIGINT
            },
            volume_finance_net: {
                type: DataTypes.BIGINT
            },
            volume_insurance_buy: {
                type: DataTypes.BIGINT
            },
            volume_insurance_sell: {
                type: DataTypes.BIGINT
            },
            volume_insurance_net: {
                type: DataTypes.BIGINT
            },
            volume_investortrust_buy: {
                type: DataTypes.BIGINT
            },
            volume_investortrust_sell: {
                type: DataTypes.BIGINT
            },
            volume_investortrust_net: {
                type: DataTypes.BIGINT
            },
            volume_private_buy: {
                type: DataTypes.BIGINT
            },
            volume_private_sell: {
                type: DataTypes.BIGINT
            },
            volume_private_net: {
                type: DataTypes.BIGINT
            },
            volume_bank_buy: {
                type: DataTypes.BIGINT
            },
            volume_bank_sell: {
                type: DataTypes.BIGINT
            },
            volume_bank_net: {
                type: DataTypes.BIGINT
            },
            volume_otherfinance_buy: {
                type: DataTypes.BIGINT
            },
            volume_otherfinance_sell: {
                type: DataTypes.BIGINT
            },
            volume_otherfinance_net: {
                type: DataTypes.BIGINT
            },
            volume_otherfund_buy: {
                type: DataTypes.BIGINT
            },
            volume_otherfund_sell: {
                type: DataTypes.BIGINT
            },
            volume_otherfund_net: {
                type: DataTypes.BIGINT
            },
            volume_totalinstitution_buy: {
                type: DataTypes.BIGINT
            },
            volume_totalinstitution_sell: {
                type: DataTypes.BIGINT
            },
            volume_totalinstitution_net: {
                type: DataTypes.BIGINT
            },
            volume_othercorporation_buy: {
                type: DataTypes.BIGINT
            },
            volume_othercorporation_sell: {
                type: DataTypes.BIGINT
            },
            volume_othercorporation_net: {
                type: DataTypes.BIGINT
            },
            volume_individual_buy: {
                type: DataTypes.BIGINT
            },
            volume_individual_sell: {
                type: DataTypes.BIGINT
            },
            volume_individual_net: {
                type: DataTypes.BIGINT
            },
            volume_foreigner_buy: {
                type: DataTypes.BIGINT
            },
            volume_foreigner_sell: {
                type: DataTypes.BIGINT
            },
            volume_foreigner_net: {
                type: DataTypes.BIGINT
            },
            volume_otherforeigner_buy: {
                type: DataTypes.BIGINT
            },
            volume_otherforeigner_sell: {
                type: DataTypes.BIGINT
            },
            volume_otherforeigner_net: {
                type: DataTypes.BIGINT
            },
            volume_total_buy: {
                type: DataTypes.BIGINT,
            },
            volume_total_sell: {
                type: DataTypes.BIGINT,
            },
            volume_total_net: {
                type: DataTypes.BIGINT,
            },

            tranprice_finance_buy: {
                type: DataTypes.BIGINT,
            },
            tranprice_finance_sell: {
                type: DataTypes.BIGINT
            },
            tranprice_finance_net: {
                type: DataTypes.BIGINT
            },
            tranprice_insurance_buy: {
                type: DataTypes.BIGINT
            },
            tranprice_insurance_sell: {
                type: DataTypes.BIGINT
            },
            tranprice_insurance_net: {
                type: DataTypes.BIGINT
            },
            tranprice_investortrust_buy: {
                type: DataTypes.BIGINT
            },
            tranprice_investortrust_sell: {
                type: DataTypes.BIGINT
            },
            tranprice_investortrust_net: {
                type: DataTypes.BIGINT
            },
            tranprice_private_buy: {
                type: DataTypes.BIGINT
            },
            tranprice_private_sell: {
                type: DataTypes.BIGINT
            },
            tranprice_private_net: {
                type: DataTypes.BIGINT
            },
            tranprice_bank_buy: {
                type: DataTypes.BIGINT
            },
            tranprice_bank_sell: {
                type: DataTypes.BIGINT
            },
            tranprice_bank_net: {
                type: DataTypes.BIGINT
            },
            tranprice_otherfinance_buy: {
                type: DataTypes.BIGINT
            },
            tranprice_otherfinance_sell: {
                type: DataTypes.BIGINT
            },
            tranprice_otherfinance_net: {
                type: DataTypes.BIGINT
            },
            tranprice_otherfund_buy: {
                type: DataTypes.BIGINT
            },
            tranprice_otherfund_sell: {
                type: DataTypes.BIGINT
            },
            tranprice_otherfund_net: {
                type: DataTypes.BIGINT
            },
            tranprice_totalinstitution_buy: {
                type: DataTypes.BIGINT
            },
            tranprice_totalinstitution_sell: {
                type: DataTypes.BIGINT
            },
            tranprice_totalinstitution_net: {
                type: DataTypes.BIGINT
            },
            tranprice_othercorporation_buy: {
                type: DataTypes.BIGINT
            },
            tranprice_othercorporation_sell: {
                type: DataTypes.BIGINT
            },
            tranprice_othercorporation_net: {
                type: DataTypes.BIGINT
            },
            tranprice_individual_buy: {
                type: DataTypes.BIGINT
            },
            tranprice_individual_sell: {
                type: DataTypes.BIGINT
            },
            tranprice_individual_net: {
                type: DataTypes.BIGINT
            },
            tranprice_foreigner_buy: {
                type: DataTypes.BIGINT
            },
            tranprice_foreigner_sell: {
                type: DataTypes.BIGINT
            },
            tranprice_foreigner_net: {
                type: DataTypes.BIGINT
            },
            tranprice_otherforeigner_buy: {
                type: DataTypes.BIGINT
            },
            tranprice_otherforeigner_sell: {
                type: DataTypes.BIGINT
            },
            tranprice_otherforeigner_net: {
                type: DataTypes.BIGINT
            },
            tranprice_total_buy: {
                type: DataTypes.BIGINT,
            },
            tranprice_total_sell: {
                type: DataTypes.BIGINT,
            },
            tranprice_total_net: {
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