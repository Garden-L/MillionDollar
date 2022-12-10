from krxCore import krxAPI, Code
from naverCore import naverAPI
from fnguideCore import fnguideCore
from columnsNaming import naming
import numpy as np
import pandas as pd
from time import sleep
from datetime import datetime, timedelta

class stockAPI:
    @staticmethod
    def getHollydays(year: int) -> list:
        '''
        * function : 모든 공휴일, 토요일, 일요일 반환
        '''
        days = krxAPI.getHolidays(year)
        start = datetime(int(year), 1, 1)        
        end   = datetime(int(year), 12, 31)
        hollydays = {}

        while start < end:
            date = start.strftime('%Y%m%d')
            hollydays[date] = False
            if start.weekday() > 4:
                hollydays[date] = True;
            start += timedelta(days= 1)

        for date in days['calnd_dd']:
            hollydays[datetime.strptime(date, '%Y-%m-%d').strftime('%Y%m%d')] = True
        
        return hollydays

    @staticmethod
    def getAllStockCode() -> pd.Series:
        '''
        * function : 모든 종목 stk_code 반환
        '''
        return Code().getAllCodes();

    @staticmethod
    def getMarketPrice(stkCode: str, startDate: str, endDate: str) -> pd.DataFrame:
        '''
        * function : 개별 종목 시세 요청
        '''
        krxData: pd.DataFrame   = krxAPI.getKrxMarketPrice(stkCode, startDate, endDate, 1)
        naverData: pd.DataFrame = naverAPI.getKrxMarketPrice(stkCode, startDate, endDate)
        fnguideData: pd.DataFrame = fnguideCore.getShares_flow_rate(stkCode)

        krxData = naming.setColumnsNaming(krxData)
        naverData = naming.setColumnsNaming(naverData)
   
        naverData.drop(columns=['tr_foreiner_rt'], inplace= True)
        krxData.drop(columns=['fluc_code', 'tr_prevcomp', 'tr_opnprc', 'tr_hgprc', 'tr_lwprc', 'fluc_rt', 'tr_volume'], inplace=True)
        
        totalData = naverData.merge(right=krxData, on=['tr_date'],suffixes=("", "_krx"))

        totalData['tr_volume'] = np.int64(totalData['tr_clsprc_krx'] / totalData['tr_clsprc'] * totalData['tr_volume'])  #수정거래량
        totalData['list_shares'] =  np.int64(totalData['mkt_capital'] / totalData['tr_clsprc'])                           #수정 상장 주식수
        totalData.drop(columns=['tr_clsprc_krx'], inplace=True)
        
        totalData['stk_code'] = np.str_(stkCode)
        totalData['flow_rate'] = np.float32(fnguideData)

        return totalData

    @staticmethod
    def getTransactionOfInvestors_(stkCode: str, startDate: str, endDate: str, trdVolVal: int=1, askBid: int=1) -> pd.DataFrame:
        '''
        * function  :   투자자별 거래실적
        * parameter :   trdVolVal   1: 거래량    2: 거래대금
                        askBid      1: 매도      2:매수      3:매도
        '''
        TRADE = ['volume_', 'value_']
        BID = ['_buy', '_buy', '_net']

        invData = krxAPI.getTransactionOfInvestor_days(stkCode, startDate, endDate, trdVolVal, askBid)
        invData = naming.setColumnsNaming(invData)
        
        invData.drop(columns=['total'], inplace=True)

        cols = {}
        # 세부 열 수정
        for column in invData.columns:
            if(column != 'tr_date'):
                cols[column] = TRADE[trdVolVal-1] + column + BID[askBid-1]
        
        invData.rename(columns=cols, inplace=True)

        return invData

    @staticmethod
    def getTransactionOfInvestors(stkCode: str, startDate: str, endDate: str) -> pd.DataFrame:
        datas = []
        for trdVolVal in range(1, 3):
            for askBid in range(1, 4):
                datas.append(stockAPI.getTransactionOfInvestors_(stkCode, startDate, endDate, trdVolVal, askBid))
                sleep(2)

        invData: pd.DataFrame = datas[0]
        for data in datas[1:]:
            invData = invData.merge(right=data, on=['tr_date'])
    
        invData['stk_code']= np.str_(stkCode)
        return invData

    @staticmethod
    def getTransactionOfIvestor_PeriodPrefixSum(stkCode: str, startDate: str, endDate: str, ):
        invData=krxAPI.getTransactionOfIvestor_PeriodPrefixSum(stkCode, startDate, endDate)

        invData.drop(index=[12, 7], inplace=True) #기관합계, 전체 합계 
        invData.drop(columns=['CONV_OBJ_TP_CD'], inplace=True) 

        columns = ['TRDVAL1', 'TRDVAL2', 'TRDVAL3', 'TRDVAL4', 'TRDVAL5', 'TRDVAL6', 'TRDVAL7', 'TRDVAL8', 'TRDVAL9', 'TRDVAL10','TRDVAL11']
        
        BID = ['_sell', '_buy', '_net']
        TRADE = ['volume_', 'value_']
        datas=[]

        for col in range(1, len(invData.columns)):
            data = {}

            for i in range(0, len(columns)):
                data[columns[i]] = [invData.iloc[i,col]]

            df = pd.DataFrame(data)
            df = naming.setColumnsNaming(df)

            cols = {}
            for column in df.columns:
                cols[column] = TRADE[(col-1)//3] + column + BID[(col-1)%3]
            
            df = df.rename(columns=cols)
            datas.append(df)
            
        invData: pd.DataFrame = datas[0]

        for data in datas[1:]:
            invData = invData.join(other = data)

        invData['stk_code'] = np.str_(stkCode)
        invData['tr_date'] = np.datetime64(startDate)

        return invData

if __name__=='__main__':
    #print(stockAPI.getMarketPrice('060310', '20221209', '20221209'))
    #print(stockAPI.getTransactionOfInvestors('005930', '20180101', '20180505'))
    print(stockAPI.getTransactionOfIvestor_PeriodPrefixSum('005930', '20180101', '20180505').to_csv('fewfw.csv'))

    #stockAPI.getHollydays(2022)
    pass
