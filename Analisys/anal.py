from library.dataAPI.api import dbPandas as db, engine
import pandas as pd

def algorithm():
 
        jump = [10,20,30,40,50,60,70,80]
        for rate in range(12, 13):
            priceOfmarket = db.getOverHighPriceRate(rate, 'close', "20170101")
            try:
                if(not priceOfmarket.empty):
                    for index in range(0, len(priceOfmarket.index)):
                        tempdata = priceOfmarket.iloc[index]
                        for cnt in jump:
                                try:
                                    investor = db.getComparePrefixSum(tempdata[0],tempdata[1].strftime("%Y%m%d"), cnt)
                                    check = db.getMax(tempdata[0],tempdata[1].strftime("%Y%m%d"), cnt,15)
                                    if(not investor.empty and check.empty):
                                        capital = ((float)(investor['capital']))*(tempdata[2]/100)
                                        if(not investor.empty):
                                            fund = (float)((investor['finance'] + investor['insurance'] + investor['investortrust'] + investor['otherfinance'] + investor['bank'] +investor['otherfund'])/capital*100)
                                            cor = (float)((investor['othercorporation'])/capital*100)
                                            indi = (float)((investor['individual'])/capital*100)
                                            fore = (float)((investor['foreigner'] + investor['otherforigner'])/capital*100)
                                            data = priceOfmarket.iloc[[index]][['STK_CODE', 'TRADE_DATE']]
                                            data['stdRate'] = rate
                                            data['period'] = cnt
                                            data['corporation'] = cor
                                            data['fund'] = fund
                                            data['individual'] = indi
                                            data['foreigner'] = fore
                                            data.to_sql('result3', engine.connect(), if_exists='append', index=False)
                                            print('성공')
                                except:
                                    print('error')        
            except:
                print('error')

            

algorithm();
