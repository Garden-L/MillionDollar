import requests as req
import pandas as pd
import re
import numpy as np
from bs4 import BeautifulSoup
from time import sleep

# Request URL
KRX_URL = 'http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd'
NAVER_URL = 'https://api.finance.naver.com/siseJson.naver?'

# Request Header
REQUEST_HEADERS = { 
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
}

'''
  *** Naming rule ***
    STD = Standard
    STK = Stock
    MKT = Market
'''
NAMING = {
    #KRX Naming
    'ISU_CD'        : 'STD_CODE',               #표준코드
    'ISU_SRT_CD'    : 'STK_CODE',               #종목코드
    'ISU_ABBRV'     : 'COR_NAME',               #회사이름
    'LIST_DD'       : 'LIST_DATE',              #상장일
    'MKT_TP_NM'     : 'MKT_NAME',               #시장구분(코스피, 코스닥, ...)
    'LIST_SHRS'     : 'LIST_SHARES',            #상장 주식수
    'full_code'     : 'STD_CODE',
    'short_code'    : 'STK_CODE',
    'codeName'      : 'COR_NAME',
    'marketCode'    : 'MKT_CODE',
    'marketName'    : 'MKT_NAME',
    'TRD_DD'        : 'TRADE_DATE',             #거래일
    'ACC_TRDVAL'    : 'TRADE_VALUE',            #거래대금
    'ACC_TRDVOL'    : 'TRADE_VOLUME',           #거래량
    'CMPPREVDD_PRC' : 'TRADE_COMPARE',          #전일대비
    'FLUC_RT'       : 'TRADE_FRUC_RATE',        #등락율
    'FLUC_TP_CD'    : 'TRADE_FRUC_CODE',        #등락코드(1: 상승, 2: 하락, 0: 동일)
    'MKTCAP'        : 'MKT_CAPITAL',            #시가총액
    'TDD_CLSPRC'    : 'TRADE_CLOSE_PRICE',      #종가
    'TDD_HGPRC'     : 'TRADE_HIGH_PRICE',       #고가
    'TDD_LWPRC'     : 'TRADE_LOW_PRICE',        #저가
    'TDD_OPNPRC'    : 'TRADE_OPEN_PRICE',       #시가
    
    # Naver Naming
    '날짜'           : 'TRADE_DATE',
    '시가'           : 'TRADE_OPEN_PRICE',
    '고가'           : 'TRADE_HIGH_PRICE',
    '종가'           : 'TRADE_CLOSE_PRICE',
    '저가'           : 'TRADE_LOW_PRICE',
    '거래량'          : 'TRADE_VOLUME',
    '외국인소진율'     : 'TRADE_FORIENER_RATE',

    # Trade Of Investor Naming
    'ASK_TRDVAL'        : 'SELL_TRADE_VALUE',       #매도 거래대금
    'ASK_TRDVOL'        : 'SELL_VOLUME',            #매도 거래량
    'BID_TRDVAL'        : 'BUY_TRADE_VALUE',        #매수 거래대금
    'BID_TRDVOL'        : 'BUY_VOLUME',             #매수 거래량
    'CONV_OBJ_TP_CD'    : 'NONE',                   #NONE
    'INVST_TP_NM'       : 'INVESTOR_NAME',          #투자자이름
    'NETBID_TRDVAL'     : 'BUY_NET_TRADE_VALUE',    #순매수 거래대금
    'NETBID_TRDVOL'     : 'BUY_NET_VOLUME',         #순매수 거래량
}

INVESTOR_NAMING={
    'TRDVAL1'       : 'FINANCE',            #금융투자
    'TRDVAL2'       : 'INSURANCE',          #보험
    'TRDVAL3'       : 'INVESTORTRUST',      #투신
    'TRDVAL4'       : 'PRIVATE',            #사모
    'TRDVAL5'       : 'BANK',               #은행
    'TRDVAL6'       : 'OTHERFINANCE',       #기타금융   
    'TRDVAL7'       : 'OTHERFUND',          #연기금 등
    'TRDVAL8'       : 'OTHERCORPORATION',   #기타법인
    'TRDVAL9'       : 'INDIVIDUAL',         #개인
    'TRDVAL10'      : 'FOREIGNER',          #외국인
    'TRDVAL11'      : 'OTHERFORIGNER',      #기타외국인
    'TRDVAL_TOT'    : 'TOTAL',              #전체
    'TRD_DD'        : 'TRADE_DATE',         #거래일
}

# Set KRX trade of investor data types
KRX_TRADE_OF_INVESTOR_DATA_TYPES={
    'TRDVAL1'       : np.int64,   #금융투자
    'TRDVAL2'       : np.int64,   #보험
    'TRDVAL3'       : np.int64,   #투신
    'TRDVAL4'       : np.int64,   #사모
    'TRDVAL5'       : np.int64,   #은행
    'TRDVAL6'       : np.int64,   #기타금융   
    'TRDVAL7'       : np.int64,   #연기금 등
    'TRDVAL8'       : np.int64,   #기타법인
    'TRDVAL9'       : np.int64,   #개인
    'TRDVAL10'      : np.int64,   #외국인
    'TRDVAL11'      : np.int64,   #기타외국인
    'TRD_DD'        : np.datetime64,   #거래일
}

# set KRX DataFrame data types
KRX_MARKET_PRICE_DATA_TYPES = {
    'STK_CODE'              : np.str_,
    'TRADE_DATE'            : np.datetime64,
    'TRADE_CLOSE_PRICE'	    : np.int64,
    'TRADE_FRUC_CODE'       : np.int32,
	'TRADE_COMPARE'         : np.int64,
    'TRADE_FRUC_RATE'       : np.double,
    'TRADE_OPEN_PRICE'      : np.int64,
    'TRADE_HIGH_PRICE'      : np.int64,
    'TRADE_LOW_PRICE'       : np.int64,
    'TRADE_VOLUME'          : np.int64,
    'TRADE_VALUE'           : np.int64,
    'MKT_CAPITAL'           : np.int64,
    'LIST_SHARES'           : np.int64,
}

# set KRX DataFrame data types
NAVER_MARKET_PRICE_DATA_TYPES = {
    'STK_CODE'              : np.str_,
    'TRADE_DATE'            : np.datetime64,
    'TRADE_CLOSE_PRICE'	    : np.int64,
    'TRADE_OPEN_PRICE'      : np.int64,
    'TRADE_HIGH_PRICE'      : np.int64,
    'TRADE_LOW_PRICE'       : np.int64,
    'TRADE_VOLUME'          : np.int64,
    'TRADE_FORIENER_RATE'   : np.float32,
}


def getCorpoation() -> pd.DataFrame:
    '''
    * function : get all Corporation information
    '''
    krx_data = req.post(url=KRX_URL,
                    data={
                        "bld": "dbms/MDC/STAT/standard/MDCSTAT01901",
                        "locale": "ko_KR",
                        "mktId": "ALL",
                        "share": "1",
                        "csvxls_isNo": "false",
                    },
                    headers=REQUEST_HEADERS,
                    )

    krx_data = krx_data.json()['OutBlock_1']    # to json
    krx_data = pd.DataFrame(krx_data)           # to dataframe

    # 이름 변경
    krx_data.rename(columns=NAMING, inplace=True, errors='ignore') 
    # 일부열만 선택
    krx_data = krx_data[['STD_CODE', 'STK_CODE', 'COR_NAME', 'LIST_DATE', 'MKT_NAME', 'LIST_SHARES']]
    # 인덱스 드랍
    krx_data.reset_index(drop=True, inplace=True)

    return krx_data

def StkcodeToStdcode_():
    '''
    * function : stkCode -> StandardCode
    '''
    krx_data = req.post(KRX_URL,
                        data={
                            "locale": "ko_KR",
                            "mktsel": "ALL",
                            "typeNo": "0",
                            "bld": "dbms/comm/finder/finder_stkisu",
                        },
                        headers=REQUEST_HEADERS
    )

    # KRX 데이터 가공
    krx_data = krx_data.json()['block1']
    krx_data = pd.DataFrame(krx_data)
    krx_data.rename(columns=NAMING, errors='ignore', inplace=True)
    krx_data = krx_data[['STK_CODE', 'STD_CODE']].set_index('STK_CODE')

    return krx_data# 알맞은 표준코드 반환

ticker = StkcodeToStdcode_()

def StkcodeToStdcode(stkcode: str):
    '''
    * function : stkCode -> StandardCode
    '''
    return ticker.loc[stkcode][0]


def removeChar(df: pd.DataFrame, char: str) -> pd.DataFrame:
    for column in df.columns:
        df[column] = df[column].str.replace(char, '')
    
    return df

def getKrxMarketPrice(stkCode: str, startDate: str, endDate: str) -> pd.DataFrame:
    '''
    * function : krx 개별종목 시세 추이
    '''
    krx_data = req.post(KRX_URL,
                        data={
                            "bld": "dbms/MDC/STAT/standard/MDCSTAT01701",
                            "isuCd": StkcodeToStdcode(stkCode),
                            "strtDd": startDate,
                            "endDd": endDate,
                        },
                        headers=REQUEST_HEADERS,
    )
    krx_data = krx_data.json()['output']
    krx_data = pd.DataFrame(krx_data)
    krx_data.rename(columns=NAMING, errors='ignore', inplace=True)
    krx_data['STK_CODE'] = stkCode
    
    krx_data = removeChar(krx_data, ',')        #removeComma
    krx_data = krx_data.astype(dtype=KRX_MARKET_PRICE_DATA_TYPES)

    return krx_data

def getTradingOfInvestors_(stkCode: str, startDate: str, endDate: str, trdVolVal: int=1, askBid: int=1) -> pd.DataFrame:
    '''
    * function  :   개별종목 거래실적
    * parameter :   trdVolVal   1: 거래량    2: 거래대금
                    askBid      1: 매도      2:매수      3:매도
    '''
    TRADE = ['VOLUME_', 'TRADEVALUE_']
    BID = ['_SELL', '_BUY', '_NET']
    investor_data = req.post(KRX_URL,
                            data={
                                'bld'       : 'dbms/MDC/STAT/standard/MDCSTAT02303',
                                'trdVolVal' : trdVolVal,
                                'askBid'    : askBid,
                                'isuCd'     : StkcodeToStdcode(stkCode),
                                'strtDd'    : startDate,
                                'endDd'     : endDate,
                                'detailView': '1',
                            },
                            headers=REQUEST_HEADERS
    )

    naming = INVESTOR_NAMING.copy()
    
    for key,value in naming.items():
        if(value != "TRADE_DATE"):
            naming[key] = TRADE[trdVolVal-1] + value + BID[askBid-1]

    investor_data = investor_data.json()['output']
    investor_data = pd.DataFrame(investor_data)
    investor_data = investor_data.drop(labels='TRDVAL_TOT', axis=1)
    investor_data = removeChar(investor_data, ',')
    investor_data = investor_data.astype(dtype=KRX_TRADE_OF_INVESTOR_DATA_TYPES, errors='ignore')
    investor_data.rename(columns=naming, errors='ignore', inplace=True)
    investor_data['STK_CODE'] = stkCode
    investor_data = investor_data.astype(dtype={'STK_CODE' : np.str_}, errors='ignore')

    return investor_data

def getTradingOfInvestors(stkCode, startDate, endDate):
    '''
    * function : 투자자별 거래실적(개별종목)
    '''
    datas = []
    for trdVolVal in range(1, 3):
        for askBid in range(1, 4):
            datas.append(getTradingOfInvestors_(stkCode, startDate, endDate, trdVolVal, askBid))
            sleep(3)
    
    investor_data: pd.DataFrame = datas[0]
    for data in datas[1:]:
        investor_data = investor_data.merge(right=data, on=['TRADE_DATE', 'STK_CODE'])

    return investor_data


def getNaverMarketPrice(stkCode: str, startDate: str, endDate: str) -> pd.DataFrame:
    '''
    * function : naver 개별종목 시세 추이
    '''
    naver_data = req.post(NAVER_URL,
                        data={
                            "symbol": stkCode,
                            "requestType": "1",
                            "startTime": startDate,
                            "endTime": endDate,
                            "timeframe": "day",
                        },
                        headers=REQUEST_HEADERS,
    )

    naver_temp = re.sub(pattern='[\s\n\t\]\[\"\']', repl='', string=naver_data.text).split(',')
    naver_data = {'날짜': list(), '시가': list(), '고가': list(), '저가': list(), '종가': list(), '거래량': list(), '외국인소진율': list()}
    
    for i in range(len(naver_temp)-1, 6, -1):
        if(i % 7 == 0):
            naver_data['날짜'].append(naver_temp[i])
        elif(i % 7 == 1):
            naver_data['시가'].append(naver_temp[i])
        elif(i % 7 == 2):
            naver_data['고가'].append(naver_temp[i])
        elif(i % 7 == 3):
            naver_data['저가'].append(naver_temp[i])
        elif(i % 7 == 4):
            naver_data['종가'].append(naver_temp[i])
        elif(i % 7 == 5):
            naver_data['거래량'].append(naver_temp[i])
        elif(i % 7 == 6):
            naver_data['외국인소진율'].append(naver_temp[i])

    naver_data = pd.DataFrame(data=naver_data)
    naver_data.rename(columns=NAMING, errors='ignore', inplace=True)
    naver_data['STK_CODE'] = stkCode

    naver_data = naver_data.astype(dtype=NAVER_MARKET_PRICE_DATA_TYPES)

    return naver_data


def getShares_flow_rate(stkCode: str) -> float:
    '''
    * function : 주식 유동비율
    '''

    fnguide_data = req.get("https://asp01.fnguide.com/SVO2/ASP/SVD_main.asp?pGB=1&gicode=A{stkCode}&cID=&MenuYn=Y&ReportGB=&NewMenuID=11&stkGb=&strResearchYN=",
                            headers=REQUEST_HEADERS,
    )

    # FnGuide 데이터 가공
    soup = BeautifulSoup(fnguide_data.text, 'html.parser')
    extraction = soup.find('table', attrs={'class':'us_table_ty1 table-hb thbg_g h_fix zigbg_no'}).findAll('tr')[-1].find('td', attrs={'class':'cle r'}).text
    flowRate = float(re.sub(pattern='\s', repl='', string=extraction).split('/')[1]);

    return flowRate


def getMarketPrice(stkCode: str, startDate:str, endDate:str) -> pd.DataFrame:
    '''
    * function : 개별 종목 시세 요청
    '''

    krx_data: pd.DataFrame = getKrxMarketPrice(stkCode, startDate, endDate)
    naver_data: pd.DataFrame = getNaverMarketPrice(stkCode, startDate, endDate)

    krx_data = krx_data[['STK_CODE', 'TRADE_DATE', 'LIST_SHARES', 'MKT_CAPITAL', 'TRADE_VALUE', 'TRADE_FRUC_RATE']]
    naver_data = naver_data.merge(right=krx_data, on=['TRADE_DATE','STK_CODE'])
    
    naver_data['FLOW_RATE'] = getShares_flow_rate(stkCode)
    naver_data = naver_data.astype(dtype={'FLOW_RATE' : np.float32})

    return naver_data[['TRADE_DATE', 'STK_CODE', 'TRADE_OPEN_PRICE', 'TRADE_HIGH_PRICE', 'TRADE_LOW_PRICE', 'TRADE_CLOSE_PRICE', 'TRADE_FRUC_RATE',\
                        'TRADE_VOLUME', 'TRADE_VALUE', 'LIST_SHARES', 'MKT_CAPITAL', 'FLOW_RATE']]


    
#print(getMarketPrice('005930', '20220101', '20220202'))
#print(getTradingOfInvestors("005930","20220603","20221203").to_csv("fwfew.csv"))

if __name__== '__main__':

