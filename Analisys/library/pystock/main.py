from stockAPI import stockAPI
from sqlalchemy import create_engine
from datetime import datetime
from time import sleep
import pandas as pd

engine = create_engine('mysql://root@localhost/stock')

holly = stockAPI.getHollydays(int(datetime.now().strftime('%Y')))

def getIndex () :
    codes = stockAPI.getIndexCodes();
    try:
        codes.to_sql('indexs', engine.connect(), if_exists='append', index=False)
    except:
        pass

def getIndexOfCor(date, idx1, idx2):
    cor = stockAPI.getStocksInIndex(date, idx1, idx2)
    cor['idx1'] = idx1
    cor['idx2'] = idx2
    cor['date'] = date

    return cor

def crawlerIndexAndCor(date):
    codes = stockAPI.getIndexCodes();
    
    idx1 = codes['idx1']
    idx2 = codes['idx2']

    for idx in range(0, len(idx1)):
        try:
            cor = getIndexOfCor(date, idx1[idx], idx2[idx])
            cor.to_sql('index_stock', engine.connect(), if_exists='append', index=False)
            print(cor)
        except:
            print('crawlerIndexAndCor 실패')
            pass
        
        sleep(2)


def crawlerMarketPrice(nowDate):
    allCode = stockAPI.getAllStockCode()
    
    for code in allCode:
        try: 
            marketPrice: pd.DataFrame = stockAPI.getMarketPrice(code, nowDate, nowDate)
            investor: pd.DataFrame = stockAPI.getTransactionOfIvestor_PeriodPrefixSum(code, nowDate, nowDate) 
            marketPrice.to_sql('marketprices', engine.connect(), if_exists='append', index=False)
            investor.to_sql('investors', engine.connect(), if_exists='append', index=False)
            print(code, '성공')
        except:
            print(code, '실패')
        sleep(2)

def todayDataAnal(date, on= False):
    codes = stockAPI.getAllStockCode()

    for code in codes:
        try:
            sql = f"select * from prefixsum_investor_view where stk_code ='{code}'"

            if(on):
                sql = sql + " and tr_date = '{date}'"
            
            sql = "insert into prefixsum_stock ( " + sql +") "

            engine.connect().execute(sql)
 
        except:
            print('todayDataAnal 실패')



def isHolly(date: str):
    return holly[date]


def run():
    nowDate = datetime.now().strftime('%Y%m%d')

    #공휴일이면 크롤링 x
    if (isHolly(nowDate)):
        print("Today is holly day")
        return 

    crawlerMarketPrice(nowDate)
    crawlerIndexAndCor(nowDate)

    todayDataAnal(nowDate, True)

    engine.connect().close()


if __name__ == '__main__':
    #run()
    #getIndex()
    #getIndexOfCor('20221212', '1', '001')
    pass