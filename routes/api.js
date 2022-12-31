const express = require('express');
const { StockInIndex, PrefixSumNetPurchase, Marketprice, sequelize} = require('../models');
const router = express.Router();

router.post('/total', async (req, res) => {
    date = req.body.date;
    prefixSum = req.body.prefixSum;
    let data;
    try{
        data = await sequelize.query(sql=`  SELECT 
                                                i.sctNm AS 섹터, I.mktNm AS 마켓,
                                                sum(vol_indi_${prefixSum}) / sum(avg_shrs_${prefixSum}) * 100 AS "IND(${prefixSum}) S ",
                                                sum(vol_inst_${prefixSum}) / sum(avg_shrs_${prefixSum}) * 100 AS "INS(${prefixSum}) S ",
                                                sum(vol_corp_${prefixSum}) / sum(avg_shrs_${prefixSum}) * 100 AS "COR(${prefixSum}) S ",
                                                sum(vol_fore_${prefixSum}) / sum(avg_shrs_${prefixSum}) * 100 AS "FOR(${prefixSum}) S ",
                                                sum(trans_indi_${prefixSum}) / sum(avg_mktcap_${prefixSum}) * 100 AS "IND(${prefixSum}) C ",
                                                sum(trans_inst_${prefixSum}) / sum(avg_mktcap_${prefixSum}) * 100 AS "INS(${prefixSum}) C ",
                                                sum(trans_corp_${prefixSum}) / sum(avg_mktcap_${prefixSum}) * 100 AS "COR(${prefixSum}) C ",
                                                sum(trans_fore_${prefixSum}) / sum(avg_mktcap_${prefixSum}) * 100 AS "FOR(${prefixSum}) C "
                                            FROM
                                                indexinfo I 
                                            INNER JOIN 
                                                stockOfIndex S ON I.mktCd = S.mktCd AND I.sctCd=S.sctCd
                                            INNER JOIN
                                                PrefixSumNetPurchase P ON S.stkCd = P.stkCd AND S.atDt = P.bsDt
                                            WHERE 
                                                P.bsDt = '${date}'
                                            GROUP BY 
                                                I.mktCd, I.sctCd, I.sctNm;`,
                                { type: sequelize.SELECT,
                                raw: true});
        
        res.send(data[0]);
    } catch(err){
        console.error(err);
        res.send('err');
    }
});

router.post('/stock', async (req, res) =>{
    date = req.body.date;
    prefixSum = req.body.prefixSum;

    data = await PrefixSumNetPurchase.findAll({
        attributes: [['stkCd', '종목코드'], ['bsDt', '기준일'], 
                    [sequelize.literal('vol_indi_'+prefixSum+'/avg_shrs_'+prefixSum+'*100'), 'IND('+prefixSum+') S'], [sequelize.literal('vol_inst_'+prefixSum+'/avg_shrs_'+prefixSum+'*100'), 'INS('+prefixSum+') S'], 
                    [sequelize.literal('vol_corp_'+prefixSum+'/avg_shrs_'+prefixSum+'*100'), 'COR('+prefixSum+') S'], [sequelize.literal('vol_fore_'+prefixSum+'/avg_shrs_'+prefixSum+'*100'), 'FOR('+prefixSum+') S'],
                    [sequelize.literal('trans_indi_'+prefixSum+'/avg_mktcap_'+prefixSum+'*100'), 'IND('+prefixSum+') C'], [sequelize.literal('trans_inst_'+prefixSum+'/avg_mktcap_60*100'), 'INS('+prefixSum+') C'], 
                    [sequelize.literal('trans_corp_'+prefixSum+'/avg_mktcap_'+prefixSum+'*100'), 'COR('+prefixSum+') C'], [sequelize.literal('trans_fore_'+prefixSum+'/avg_mktcap_60*100'), 'FOR('+prefixSum+') C']],
        where: {
            bsDt: date,
        },
        raw: true,
    });
    
    res.send(data);
})

router.post('/chart', async (req, res) =>{
    code = req.body.code;
    data = await Marketprice.findAll({
        attributes: ['trDt', 'trClsPrc'],
        where: { 
            stkCd: code
        },
        order: [['trDt','DESC']],
        limit: 500,
        raw: true,
    });
    res.send(data);
})

module.exports = router;