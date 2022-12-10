import pandas as pd
from random import *
import requests

class Code(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Code, cls).__new__(cls, *args, **kwargs)
        return cls.instance

    def __init__(self):
        self.data = krxAPI.getCodeInformation()

    def getIsuCode(self, stkCode: str) -> str:
        return self.data.loc[self.data['short_code'] == stkCode].iloc[0][0]
    
    def getAllCodes(self) -> pd.Series:
        return self.data['short_code']


class KrxRequestURL():
    '''
    * class : krx 요청 URL 정의 클래스
    '''
    KRX_URL = 'http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd'

    @staticmethod
    def getKrxUrl():
        return KrxRequestURL.KRX_URL


class KrxReqeustHeader:
    '''
    * class : krx 요청 헤더 정의 클래스
    '''
    REQUEST_HEADERS = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
         }

    @staticmethod
    def getHeaders():
        return KrxReqeustHeader.REQUEST_HEADERS


class KrxRequesFormData:
    '''
    * class : krx reqeust body
    '''
    MKTID = ['', 'ALL', 'STK', 'KSQ', 'KSQ', 'KNX']

    def __init__(self):
        self.formData = {}

    def setFormData(self, key: str, value: str):
        self.formData[key] = value
        return self

    def setBld(self, bld: str):
        return self.setFormData('bld', 'dbms/MDC/STAT/standard/' + bld)

    def setMktId(self, mktid: str):
        if (mktid == 3):  # KOSDAQ 전체
            self.setSegTpCd('ALL')
        if (mktid == 4):  # KOSDAQ GLOBAL
            self.setSegTpCd('1')

        return self.setFormData('mktId', KrxRequesFormData.MKTID[mktid])

    def setIsuCd(self, stkCode: str):
        return self.setFormData('isuCd', Code().getIsuCode(stkCode=stkCode))

    def setTrdDd(self, date: str):
        return self.setFormData('trdDd', date)

    def setStrtDd(self, date: str):
        return self.setFormData('strtDd', date)

    def setEndDd(self, date: str):
        return self.setFormData('endDd', date)

    def setSegTpCd(self, segtpcd):
        return self.setFormData('segTpCd', segtpcd)

    def setShare(self, share):
        return self.setFormData('share', share)

    def setMoney(self, money):
        return self.setFormData('money', money)

    def setCsvxls_isNo(self, csvsls_isno):
        return self.setFormData('csvxls_isNo', csvsls_isno)

    def setMktsel(self, mktsel):
        return self.setFormData('mktsel', mktsel)

    def setDetailView(self, view):
        return self.setFormData('detailView', view)

    def setTrdVolVal(self, trd):
        return self.setFormData('trdVolVal', trd)

    def setAskBid(self, bid):
        return self.setFormData('askBid', bid)

    def setTypeNo(self, typeno):
        return self.setFormData('typeNo', typeno)

    def setAdjStkPrc(self, adjStkPrc):
        return self.setFormData('adjStkPrc', adjStkPrc)

    def getData(self) -> dict:
        return self.formData

    def setSearch_bas_yy(self, y):
        return self.setFormData('search_bas_yy', y)

    def setPagePath(self, path):
        return self.setFormData('pagePath', path)
    
    def setGridTp(self, grid):
        return self.setFormData('gridTp', grid)

    def setCode(self, code):
        return self.setFormData('code', code)
    



class krxRequest:
    '''
    * class : krx 요청 클래스
    '''
    @staticmethod
    def post(formData: KrxRequesFormData):
        return requests.post(url=KrxRequestURL.getKrxUrl(), data=formData.getData(), headers=KrxReqeustHeader.getHeaders())


class krxAPI:

    @staticmethod
    def getHolidays(year: str, ):
        '''
        * function : 휴장일
        * return : 공휴일만 리턴
        '''
        formData = KrxRequesFormData().setFormData('bld', 'MKD/01/0110/01100305/mkd01100305_01')\
                                        .setFormData('name', 'bld').getData()
                                    
        opt = requests.get(url='https://open.krx.co.kr/contents/COM/GenerateOTP.jspx',
                            params=formData,
                            headers=KrxReqeustHeader.getHeaders()
        )

        formData = KrxRequesFormData().setCode(opt.text)\
                                        .setSearch_bas_yy(year)\
                                        .setGridTp('KRX')\
                                        .setPagePath('/contents/MKD/01/0110/01100305/MKD01100305.jsp')\
                                        .setFormData('pageFirstCall', 'Y')\
                                        .getData()
                                        
        response = requests.post(url='https://open.krx.co.kr/contents/OPN/99/OPN99000001.jspx',
                                data = formData,
                                headers=KrxReqeustHeader.getHeaders()
                                )
        
        return pd.DataFrame(response.json()['block1'])

    @staticmethod
    def getCodeInformation() -> pd.DataFrame:
        '''
        * function : 주식 코드 정보 가져오기
        '''
        formData = KrxRequesFormData().setFormData('bld', 'dbms/comm/finder/finder_stkisu')\
            .setMktsel('ALL')\
            .setTypeNo('0')

        response = krxRequest.post(formData=formData)

        return pd.DataFrame(response.json()['block1'])

    @staticmethod
    def getTransactionOfIvestor_PeriodPrefixSum(stkCode: str, startDate: str, endDate: str) -> pd.DataFrame:
        '''
        * function : 투자자별 거래실적 (기간합계)
        '''
        formData = KrxRequesFormData().setBld('MDCSTAT02301')\
                                    .setIsuCd(stkCode)\
                                    .setStrtDd(startDate)\
                                    .setEndDd(endDate)\

        response = krxRequest.post(formData=formData)

        return pd.DataFrame(response.json()['output'])

    @staticmethod
    def getTransactionOfInvestor_days(stkCode: str, startDate: str, endDate: str, trdVolVal: int = 1, askBid: int = 1) -> pd.DataFrame:
        '''
        * function  :   투자자별 거래실적 (일별추이)
        * parameter :   trdVolVal   1: 거래량    2: 거래대금
                        askBid      1: 매도      2:매수      3:순매수
        '''

        formData: KrxRequesFormData = KrxRequesFormData().setBld('MDCSTAT02303')\
            .setIsuCd(stkCode)\
            .setStrtDd(startDate)\
            .setEndDd(endDate)\
            .setDetailView('1')\
            .setTrdVolVal(trdVolVal)\
            .setAskBid(askBid)
        response = krxRequest.post(formData=formData)

        return pd.DataFrame(response.json()['output'])

    @staticmethod
    def getAllStockInformation(mktid: int = 1) -> pd.DataFrame:
        '''
        * function  : 전종목 기본정보
        * parameter : mktld - 시장전체 : 1 (defualt)
                            - KOSPI  : 2
                            - KOSDAQ
                                - 전체           : 3
                                - KOSDAQ GLOBAL : 4
                            - KONEX  : 5
        '''

        formData: KrxRequesFormData = KrxRequesFormData().setBld('MDCSTAT01901')\
            .setMktId(mktid)

        response = krxRequest.post(formData=formData)

        return pd.DataFrame(response.json()['OutBlock_1'])

    ########################
    ##### 종목시세 카테고리 #####
    ########################

    @staticmethod
    def getAllStockMarketPrice(date: str, mktid: int = 1) -> pd.DataFrame:
        '''
        * function  : 전종목 시세
        * parameter : date: 날짜
                      mktld - 시장전체 : 1 (defualt)
                            - KOSPI  : 2
                            - KOSDAQ
                                - 전체           : 3
                                - KOSDAQ GLOBAL : 4
                            - KONEX  : 5
        '''
        formData: KrxRequesFormData = KrxRequesFormData().setBld('MDCSTAT01501')\
            .setMktId(mktid)\
            .setTrdDd(date)\
            .setShare('1')\
            .setMoney('1')

        response = krxRequest.post(formData=formData)

        return pd.DataFrame(response.json()['OutBlock_1'])

    @staticmethod
    def getKrxMarketPrice(stkCode: str, startDate: str, endDate: str, adjStkPrc: int) -> pd.DataFrame:
        '''
        * function  : 개별종목 시세 추이
        * parameter : adjStkPrc- 수정주가 미적용 : 1,  수정주가 적용 2
        '''
        formData = KrxRequesFormData().setBld('MDCSTAT01701')\
                                    .setIsuCd(stkCode)\
                                    .setStrtDd(startDate)\
                                    .setEndDd(endDate)\
                                    .setAdjStkPrc(adjStkPrc)

        response = krxRequest.post(formData=formData)

        return pd.DataFrame(response.json()['output'])

if __name__ =='__main__':
    #print(krxAPI.getKrxMarketPrice('005930', '20170101', '20200202', 1))
    print(krxAPI.getHolidays('2022'))
