from stockAPI import stockAPI
from sqlalchemy import create_engine
from datetime import datetime
from time import sleep

#engine = create_engine()

holly = stockAPI.getHollydays(int(datetime.now().strftime('%Y')))
def isHolly(date: str):
    return holly[date]


def run():
    allCode = stockAPI.getAllStockCode()

    nowDate = datetime.now().strftime('%Y%m%d')

    #공휴일이면 크롤링 x
    if (isHolly(nowDate)):
        print("Today is holly day")
        return 

    for code in allCode:    
        marketPrice = stockAPI.getMarketPrice(code, nowDate, nowDate)
        investor = stockAPI.getTransactionOfIvestor_PeriodPrefixSum(code, nowDate, nowDate) 
        print(marketPrice)
        print(investor)

        sleep(2)
       


if __name__ == '__main__':
    run()