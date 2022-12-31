const express = require('express');
const router = express.Router();


router.get('/data', async (req, res) =>{
    
    a = await Investor.findAll({where:{
        stkCd: '005930',
        trDt: '20221206'
    }})
    
    console.log(a);

    res.send(a);
})

module.exports = router;