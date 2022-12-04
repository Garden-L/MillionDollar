const axios = require('axios');

stockData = {};

module.exports = stockData;

stockData.url_KRX = 'http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd';

stockData.getRequestURL_KRX = () => stockData.url_KRX;

function time() {
    return new Promise((resolve) => setTimeout(resolve, 3000))
}

stockData.getMarketPrice = async function(){
    var data = axios({
        method: "post",
        url: stockData.getRequestURL_KRX(),
        data:{
            "bld": "dbms/MDC/STAT/standard/MDCSTAT00101",
            "locale": "ko_KR",
            "idxIndMidclssCd": "01",
            "trdDd": "20221129",
            "share": "2",
            "money": "3",
            "csvxls_isNo": "false"
        },
        headers:{
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        }
    }) ;
    console.log("a");
}

async function c () {
    var da = await stockData.getMarketPrice();

    console.log(da);
}
async function t(){
    await time();
}
for(var i = 0; i < 5; i++){
    t().then(stockData.getMarketPrice());
    console.log('a');
}
