const { Model, DataTypes } = require('sequelize');

class Investor extends Model{
    static init(sequelize){
        super.init({
            stk_code: {
                type: DataTypes.STRING(6),
                primaryKey: true,
                allowNull: false,
                unique: true,
            },
            tr_date: {
                type: DataTypes.DATEONLY,
                primaryKey: true,
                allowNull: false,
                unique: true,
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
            volume_othercor_sell: {
                type: DataTypes.BIGINT,
            },
            volume_individual_sell: {
                type: DataTypes.BIGINT,
            },
            volume_foreigner_sell: {
                type: DataTypes.BIGINT,
            },
            volume_otherforeigner_sell: {
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
            volume_othercor_buy: {
                type: DataTypes.BIGINT,
            },
            volume_individual_buy: {
                type: DataTypes.BIGINT,
            },
            volume_foreigner_buy: {
                type: DataTypes.BIGINT,
            },
            volume_otherforeigner_buy: {
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
            volume_othercor_net: {
                type: DataTypes.BIGINT,
            },
            volume_individual_net: {
                type: DataTypes.BIGINT,
            },
            volume_foreigner_net: {
                type: DataTypes.BIGINT,
            },
            volume_otherforeigner_net: {
                type: DataTypes.BIGINT,
            },

            // value_name_sell
            value_finance_sell: {
                type: DataTypes.BIGINT,
            },
            value_insurance_sell: {
                type: DataTypes.BIGINT,
            },
            value_investortrust_sell: {
                type: DataTypes.BIGINT,
            },
            value_private_sell: {
                type: DataTypes.BIGINT,
            },
            value_bank_sell: {
                type: DataTypes.BIGINT,
            },
            value_otherfinance_sell: {
                type: DataTypes.BIGINT,
            },
            value_otherfund_sell: {
                type: DataTypes.BIGINT,
            },
            value_othercor_sell: {
                type: DataTypes.BIGINT,
            },
            value_individual_sell: {
                type: DataTypes.BIGINT,
            },
            value_foreigner_sell: {
                type: DataTypes.BIGINT,
            },
            value_otherforeigner_sell: {
                type: DataTypes.BIGINT,
            },

            // value_name_buy
            value_finance_buy: {
                type: DataTypes.BIGINT,
            },
            value_insurance_buy: {
                type: DataTypes.BIGINT,
            },
            value_investortrust_buy: {
                type: DataTypes.BIGINT,
            },
            value_private_buy: {
                type: DataTypes.BIGINT,
            },
            value_bank_buy: {
                type: DataTypes.BIGINT,
            },
            value_otherfinance_buy: {
                type: DataTypes.BIGINT,
            },
            value_otherfund_buy: {
                type: DataTypes.BIGINT,
            },
            value_othercor_buy: {
                type: DataTypes.BIGINT,
            },
            value_individual_buy: {
                type: DataTypes.BIGINT,
            },
            value_foreigner_buy: {
                type: DataTypes.BIGINT,
            },
            value_otherforeigner_buy: {
                type: DataTypes.BIGINT,
            },


            // value_name_net
            value_finance_net: {
                type: DataTypes.BIGINT,
            },
            value_insurance_net: {
                type: DataTypes.BIGINT,
            },
            value_investortrust_net: {
                type: DataTypes.BIGINT,
            },
            value_private_net: {
                type: DataTypes.BIGINT,
            },
            value_bank_net: {
                type: DataTypes.BIGINT,
            },
            value_otherfinance_net: {
                type: DataTypes.BIGINT,
            },
            value_otherfund_net: {
                type: DataTypes.BIGINT,
            },
            value_othercor_net: {
                type: DataTypes.BIGINT,
            },
            value_individual_net: {
                type: DataTypes.BIGINT,
            },
            value_foreigner_net: {
                type: DataTypes.BIGINT,
            },
            value_otherforeigner_net: {
                type: DataTypes.BIGINT,
            },
        },
        {
            sequelize,
            tableName: "Investors",
            timestamps: false,
        })
    }
}

module.exports = { Investor };