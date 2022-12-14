import os
import re
import pandas as pd
import requests

class NaverRequestURL:
    '''
    * class : 요청 URL 정의 클래스
    '''
    url = 'https://api.finance.naver.com/siseJson.naver?'

    @staticmethod
    def getURL() -> str:
        return NaverRequestURL.url


class NaverReqeustHeader:
    '''
    * class : 요청 헤더 정의 클래스
    '''
    header ={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", }

    @staticmethod
    def getHeaders() -> str:
        return NaverReqeustHeader.header


class NaverRequestFormData:
    '''
    * class :reqeust body
    '''

    def __init__(self):
        self.formData = {}

    def getData(self):
        return self.formData

    def setFormData(self, key: str, value: str):
        self.formData[key] = value
        return self
    
    def setSymbol(self, symbol: str):
        return self.setFormData('symbol', symbol)

    def setRequestType(self, requsetType):
        return self.setFormData('requestType', requsetType)

    def setStartTime(self, startTime: str):
        return self.setFormData('startTime', startTime)

    def setEndTime(self, endTime: str):
        return self.setFormData('endTime', endTime)
    
    def setTimeFrame(self, timeFrame: str):
        return self.setFormData('timeframe', timeFrame)

class NaverRequest:
    '''
    * class : krx 요청 클래스
    '''
    @staticmethod
    def post(formData: NaverRequestFormData):
        return requests.post(url=NaverRequestURL.getURL(), data=formData.getData(), headers=NaverReqeustHeader.getHeaders())

class naverAPI:

    @staticmethod
    def getKrxMarketPrice(stkCode: str, startDate: str, endDate: str) -> pd.DataFrame:
        '''
        * function : 개별종목 시세 추이
        '''
        formData: NaverRequestFormData = NaverRequestFormData().setSymbol(stkCode)\
                                                                .setRequestType("1")\
                                                                .setStartTime(startDate)\
                                                                .setEndTime(endDate)\
                                                                .setTimeFrame('day')

        response = NaverRequest.post(formData)

        #naver 데이터 가공
        data_array = re.sub(pattern='[\s\n\t\]\[\"\']', repl='', string=response.text).split(',')
        naver_data = {'날짜': list(), '시가': list(), '고가': list(), '저가': list(), '종가': list(), '거래량': list(), '외국인소진율': list()}

        for i in range(len(data_array)-1, 6, -1):
            if(i % 7 == 0):
                naver_data['날짜'].append(data_array[i])
            elif(i % 7 == 1):
                naver_data['시가'].append(data_array[i])
            elif(i % 7 == 2):
                naver_data['고가'].append(data_array[i])
            elif(i % 7 == 3):
                naver_data['저가'].append(data_array[i])
            elif(i % 7 == 4):
                naver_data['종가'].append(data_array[i])
            elif(i % 7 == 5):
                naver_data['거래량'].append(data_array[i])
            elif(i % 7 == 6):
                naver_data['외국인소진율'].append(data_array[i])

        return pd.DataFrame(naver_data)
        
if __name__ == '__main__':
    print(naverAPI.getKrxMarketPrice("005930", "20101010", "20111010"))