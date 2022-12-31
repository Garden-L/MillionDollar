from stockAPI import stockAPI
from sqlalchemy import create_engine
from datetime import datetime
from time import sleep
import pandas as pd

engine = create_engine('mysql://root@localhost/test')

holly = stockAPI.getHollydays(int(datetime.now().strftime('%Y')))

def getIndex ():
    codes = stockAPI.getIndexCodes();
    try:
        codes.to_sql('indexinfo', engine.connect(), if_exists='append', index=False)
    except:
        pass

def getIndexOfCor(date, idx1, idx2):
    cor = stockAPI.getStocksInIndex(date, idx1, idx2)
    cor['mktCd'] = idx1
    cor['sctCd'] = idx2
    cor['atDt'] = date

    return cor

def crawlerIndexAndCor(date):
    codes = stockAPI.getIndexCodes();
    
    idx1 = codes['mktCd']
    idx2 = codes['sctCd']

    for idx in range(0, len(idx1)):
        try:
            cor = getIndexOfCor(date, idx1[idx], idx2[idx])
            cor.to_sql('stockofindex', engine.connect(), if_exists='append', index=False)
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
            marketPrice.to_sql('marketprice', engine.connect(), if_exists='append', index=False)
            investor.to_sql('investor', engine.connect(), if_exists='append', index=False)
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
                sql = sql + f" and tr_date = '{date}'"
            
            sql = "insert into prefixsum_stock ( " + sql +") "
            print(sql)

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

    #crawlerMarketPrice(nowDate)
    crawlerIndexAndCor(nowDate)

    #todayDataAnal(nowDate, True)

    engine.connect().close()



if __name__ == '__main__':
    #run()
    #getIndex() 
    #getIndexOfCor('20221212', '1', '001')
    
    stkdf = pd.read_sql(sql='select stkCd from marketprice group by stkCd', con=engine.connect());
    
    for i in stkdf['stkCd']:
        try:
            sql2=f'''SELECT 	I.stkCd, I.trDt ,
                            #5
                            SUM(trans_indi_net) OVER PREV_5 AS trans_indi_5,
                            SUM(trans_fin_net) 	OVER PREV_5 + SUM(trans_insur_net) OVER PREV_5 + SUM(trans_inves_net) OVER PREV_5 + SUM(trans_priv_net) OVER PREV_5 + SUM(trans_bank_net) OVER PREV_5 + SUM(trans_othFin_net) OVER PREV_5 + SUM(trans_othFund_net) OVER PREV_5 AS trans_inst_5,
                            SUM(trans_othCorp_net) OVER PREV_5 AS trans_corp_5,
                            SUM(trans_fore_net) OVER PREV_5 + SUM(trans_othFore_net) OVER PREV_5 AS trans_fore_5,
                            #10
                            SUM(trans_indi_net) OVER PREV_10 AS trans_indi_10,
                            SUM(trans_fin_net) 	OVER PREV_10 + SUM(trans_insur_net) OVER PREV_10 + SUM(trans_inves_net) OVER PREV_10 + SUM(trans_priv_net) OVER PREV_10 + SUM(trans_bank_net) OVER PREV_10 + SUM(trans_othFin_net) OVER PREV_10 + SUM(trans_othFund_net) OVER PREV_10 AS trans_inst_10,
                            SUM(trans_othCorp_net) OVER PREV_10 AS trans_corp_10,
                            SUM(trans_fore_net) OVER PREV_10 + SUM(trans_othFore_net) OVER PREV_10 AS trans_fore_10,
                            #20
                            SUM(trans_indi_net) OVER PREV_20 AS trans_indi_20,
                            SUM(trans_fin_net) 	OVER PREV_20 + SUM(trans_insur_net) OVER PREV_20 + SUM(trans_inves_net) OVER PREV_20 + SUM(trans_priv_net) OVER PREV_20 + SUM(trans_bank_net) OVER PREV_20 + SUM(trans_othFin_net) OVER PREV_20 + SUM(trans_othFund_net) OVER PREV_20 AS trans_inst_20,
                            SUM(trans_othCorp_net) OVER PREV_20 AS trans_corp_20,
                            SUM(trans_fore_net) OVER PREV_20 + SUM(trans_othFore_net) OVER PREV_20 AS trans_fore_20,
                            #30
                            SUM(trans_indi_net) OVER PREV_30 AS trans_indi_30,
                            SUM(trans_fin_net) 	OVER PREV_30 + SUM(trans_insur_net) OVER PREV_30 + SUM(trans_inves_net) OVER PREV_30 + SUM(trans_priv_net) OVER PREV_30 + SUM(trans_bank_net) OVER PREV_30 + SUM(trans_othFin_net) OVER PREV_30 + SUM(trans_othFund_net) OVER PREV_30 AS trans_inst_30,
                            SUM(trans_othCorp_net) OVER PREV_30 AS trans_corp_30,
                            SUM(trans_fore_net) OVER PREV_30 + SUM(trans_othFore_net) OVER PREV_30 AS trans_fore_30,
                            #60
                            SUM(trans_indi_net) OVER PREV_60 AS trans_indi_60,
                            SUM(trans_fin_net) 	OVER PREV_60 + SUM(trans_insur_net) OVER PREV_60 + SUM(trans_inves_net) OVER PREV_60 + SUM(trans_priv_net) OVER PREV_60 + SUM(trans_bank_net) OVER PREV_60 + SUM(trans_othFin_net) OVER PREV_60 + SUM(trans_othFund_net) OVER PREV_60 AS trans_inst_60,
                            SUM(trans_othCorp_net) OVER PREV_60 AS trans_corp_60,
                            SUM(trans_fore_net) OVER PREV_60 + SUM(trans_othFore_net) OVER PREV_60 AS trans_fore_60,
                            #120
                            SUM(trans_indi_net) OVER PREV_120 AS trans_indi_120,
                            SUM(trans_fin_net) 	OVER PREV_120 + SUM(trans_insur_net) OVER PREV_120 + SUM(trans_inves_net) OVER PREV_120 + SUM(trans_priv_net) OVER PREV_120 + SUM(trans_bank_net) OVER PREV_120 + SUM(trans_othFin_net) OVER PREV_120 + SUM(trans_othFund_net) OVER PREV_120 AS trans_inst_120,
                            SUM(trans_othCorp_net) OVER PREV_120 AS trans_corp_120,
                            SUM(trans_fore_net) OVER PREV_120 + SUM(trans_othFore_net) OVER PREV_120 AS trans_fore_120,
                            
                            #volume
                            SUM(vol_indi_net) OVER PREV_5 AS vol_indi_5,
                            SUM(vol_fin_net) 	OVER PREV_5 + SUM(vol_insur_net) OVER PREV_5 + SUM(vol_inves_net) OVER PREV_5 + SUM(vol_priv_net) OVER PREV_5 + SUM(vol_bank_net) OVER PREV_5 + SUM(vol_othFin_net) OVER PREV_5 + SUM(vol_othFund_net) OVER PREV_5 AS vol_inst_5,
                            SUM(vol_othCorp_net) OVER PREV_5 AS vol_corp_5,
                            SUM(vol_fore_net) OVER PREV_5 + SUM(vol_othFore_net) OVER PREV_5 AS vol_fore_5,
                            #10
                            SUM(vol_indi_net) OVER PREV_10 AS vol_indi_10,
                            SUM(vol_fin_net) 	OVER PREV_10 + SUM(vol_insur_net) OVER PREV_10 + SUM(vol_inves_net) OVER PREV_10 + SUM(vol_priv_net) OVER PREV_10 + SUM(vol_bank_net) OVER PREV_10 + SUM(vol_othFin_net) OVER PREV_10 + SUM(vol_othFund_net) OVER PREV_10 AS vol_inst_10,
                            SUM(vol_othCorp_net) OVER PREV_10 AS vol_corp_10,
                            SUM(vol_fore_net) OVER PREV_10 + SUM(vol_othFore_net) OVER PREV_10 AS vol_fore_10,
                            #20
                            SUM(vol_indi_net) OVER PREV_20 AS vol_indi_20,
                            SUM(vol_fin_net) 	OVER PREV_20 + SUM(vol_insur_net) OVER PREV_20 + SUM(vol_inves_net) OVER PREV_20 + SUM(vol_priv_net) OVER PREV_20 + SUM(vol_bank_net) OVER PREV_20 + SUM(vol_othFin_net) OVER PREV_20 + SUM(vol_othFund_net) OVER PREV_20 AS vol_inst_20,
                            SUM(vol_othCorp_net) OVER PREV_20 AS vol_corp_20,
                            SUM(vol_fore_net) OVER PREV_20 + SUM(vol_othFore_net) OVER PREV_20 AS vol_fore_20,
                            #30
                            SUM(vol_indi_net) OVER PREV_30 AS vol_indi_30,
                            SUM(vol_fin_net) 	OVER PREV_30 + SUM(vol_insur_net) OVER PREV_30 + SUM(vol_inves_net) OVER PREV_30 + SUM(vol_priv_net) OVER PREV_30 + SUM(vol_bank_net) OVER PREV_30 + SUM(vol_othFin_net) OVER PREV_30 + SUM(vol_othFund_net) OVER PREV_30 AS vol_inst_30,
                            SUM(vol_othCorp_net) OVER PREV_30 AS vol_corp_30,
                            SUM(vol_fore_net) OVER PREV_30 + SUM(vol_othFore_net) OVER PREV_30 AS vol_fore_30,
                            #60
                            SUM(vol_indi_net) OVER PREV_60 AS vol_indi_60,
                            SUM(vol_fin_net) 	OVER PREV_60 + SUM(vol_insur_net) OVER PREV_60 + SUM(vol_inves_net) OVER PREV_60 + SUM(vol_priv_net) OVER PREV_60 + SUM(vol_bank_net) OVER PREV_60 + SUM(vol_othFin_net) OVER PREV_60 + SUM(vol_othFund_net) OVER PREV_60 AS vol_inst_60,
                            SUM(vol_othCorp_net) OVER PREV_60 AS vol_corp_60,
                            SUM(vol_fore_net) OVER PREV_60 + SUM(vol_othFore_net) OVER PREV_60 AS vol_fore_60,
                            #120
                            SUM(vol_indi_net) OVER PREV_120 AS vol_indi_120,
                            SUM(vol_fin_net) 	OVER PREV_120 + SUM(vol_insur_net) OVER PREV_120 + SUM(vol_inves_net) OVER PREV_120 + SUM(vol_priv_net) OVER PREV_120 + SUM(vol_bank_net) OVER PREV_120 + SUM(vol_othFin_net) OVER PREV_120 + SUM(vol_othFund_net) OVER PREV_120 AS vol_inst_120,
                            SUM(vol_othCorp_net) OVER PREV_120 AS vol_corp_120,
                            SUM(vol_fore_net) OVER PREV_120 + SUM(vol_othFore_net) OVER PREV_120 AS vol_fore_120,
                            
                            #MKTCAP
                            AVG(mktCap) OVER PREV_5 AS avg_mktCap_5,
                            AVG(mktCap) OVER PREV_10 AS avg_mktCap_10,
                            AVG(mktCap) OVER PREV_20 AS avg_mktCap_20,
                            AVG(mktCap) OVER PREV_30 AS avg_mktCap_30,
                            AVG(mktCap) OVER PREV_60 AS avg_mktCap_60,
                            AVG(mktCap) OVER PREV_120 AS avg_mktCap_120,
                            #SHRS
                            AVG(lstshrs) OVER PREV_5 AS avg_shrs_5,
                            AVG(lstshrs) OVER PREV_10 AS avg_shrs_10,
                            AVG(lstshrs) OVER PREV_20 AS avg_shrs_20,
                            AVG(lstshrs) OVER PREV_30 AS avg_shrs_30,
                            AVG(lstshrs) OVER PREV_60 AS avg_shrs_60,
                            AVG(lstshrs) OVER PREV_120 AS avg_shrs_120
                    FROM INVESTOR I INNER JOIN MARKETPRICE M
                                            ON I.stkCd = M.stkCd AND I.trDt = M.trDt
                    WHERE I.stkCd='{i}'
                    WINDOW 	PREV_5 	AS (PARTITION BY I.stkCd ORDER BY I.trDt ROWS BETWEEN 4 PRECEDING AND 0 PRECEDING),
                            PREV_10 AS (PARTITION BY I.stkCd ORDER BY I.trDt ROWS BETWEEN 9 PRECEDING AND 0 PRECEDING),
                            PREV_20 AS (PARTITION BY I.stkCd ORDER BY I.trDt ROWS BETWEEN 19 PRECEDING AND 0 PRECEDING),
                            PREV_30 AS (PARTITION BY I.stkCd ORDER BY I.trDt ROWS BETWEEN 29 PRECEDING AND 0 PRECEDING),
                            PREV_60 AS (PARTITION BY I.stkCd ORDER BY I.trDt ROWS BETWEEN 59 PRECEDING AND 0 PRECEDING),
                            PREV_120 AS (PARTITION BY I.stkCd ORDER BY I.trDt ROWS BETWEEN 119 PRECEDING AND 0 PRECEDING));'''
            insert= 'insert into PrefixSumNetPurchase ('
            engine.execute(insert+sql2);
            print('성공')
        except:
            print('실패'
            )
    pass