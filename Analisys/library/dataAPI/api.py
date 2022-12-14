from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('mysql://root@localhost/stock');

class dbCore:
    @staticmethod
    def getDays():
        sql: str = 'SEL'
        return pd.read_sql("select * from investor where stk_code='005930'", engine.connect())

    @staticmethod
    def getCode():
        sql: str = 'SELECT STK_CODE FROM MARKETPRICE GROUP BY STK_CODE'
        return pd.read_sql(sql, engine.connect())
    
    @staticmethod
    def getMKIS():
        sql: str ="SELECT IVS.STK_CODE, IVS.TRADE_DATE, FLOW_RATE, \
		volume_finance_net,volume_insurance_net,volume_investortrust_net,volume_private_net,volume_bank_net,volume_otherfinance_net,volume_otherfund_net,volume_othercorporation_net,volume_individual_net,volume_foreigner_net,volume_otherforigner_net, \
        tradevalue_otherfinance_net,tradevalue_otherfund_net,tradevalue_othercorporation_net,tradevalue_individual_net,tradevalue_foreigner_net,tradevalue_otherforigner_net,tradevalue_bank_net,tradevalue_private_net,tradevalue_investortrust_net,tradevalue_insurance_net,tradevalue_finance_net \
		FROM investor AS IVS INNER JOIN marketprice AS MKP \
							  on IVS.stk_code = MKP.stk_code and IVS.trade_date = MKP.trade_date \
                              where IVS.stk_code = '002140' and mkt.trade >= 15"

        return pd.read_sql(sql, engine.connect())

    def getOverHighPriceRate(standardRate: float, standarPrice: str, standarDate: str) -> pd.DataFrame:
        sql: str = f"select STK_CODE, TRADE_DATE, FLOW_RATE from marketprice\
                    where (trade_{standarPrice}_price-trade_open_price)/(trade_open_price) *100 >= {standardRate} and trade_date >= date('{standarDate}')"
        return pd.read_sql(sql, engine.connect())

    def getComparePrefixSum(stkCode: str, standardDate: str, compNumber: int) -> pd.DataFrame:
        '''
        * function : 기준일 하루 전부터 compNumer 칠만큼 누적 투자자별 누적 거래대금을 가져온다.
        ''' 
        sql: str = f"select  stk_code,(select mkt_capital from  marketprice where stk_code = a.stk_code and trade_date <= date_add(date('{standardDate}') , INTERVAL -1 day) order by trade_date desc limit 1)as capital  ,sum(tradevalue_finance_net) as finance, sum(tradevalue_insurance_net) as insurance, sum(tradevalue_investortrust_net) as investortrust,\
				 sum(tradevalue_otherfinance_net) as otherfinance,sum(tradevalue_bank_net) as bank,sum(tradevalue_otherfund_net) as otherfund,sum(tradevalue_othercorporation_net) as othercorporation,\
				 sum(tradevalue_individual_net) as individual,sum(tradevalue_foreigner_net) as foreigner,sum(tradevalue_otherforigner_net) as otherforigner\
                                                from (select * from investor\
                                                where stk_code ='{stkCode}' and trade_date<= date_add(date('{standardDate}'), INTERVAL -1 DAY)\
                                                order by trade_date desc limit {compNumber})as a\
                                                group by stk_code"
        return pd.read_sql(sql, engine.connect())

    def getMax(stk_code, date, number, rate):
        sql: str = f"select STK_CODE from (select * from marketprice\
                    where stk_code='{stk_code}' and trade_date <= date_add(date('{date}'), INTERVAL -1 DAY) order by trade_date desc limit {number})  as a\
                    where (trade_close_price-trade_open_price)/(trade_open_price) *100 >= {rate}"
        return pd.read_sql(sql, engine.connect())
#print(db.getDays())
#print(dbPandas.getCode())


#print(dbPandas.getOverHighPriceRate(15, "close", "20170101"))
#print(dbPandas.getComparePrefixSum('294140', '20221205', 60))

#print(dbPandas.getMax("030350", "20211125", 30, 15))