import pandas as pd
import requests as req
import re

from label import *


# 모든종목 기본정보 요청
def getCorpoation() -> pd.DataFrame:
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


# 종목코드 -> 표준코드
def StkcodeToStdcode(stkcode: str):
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

    return krx_data.loc[stkcode][0] # 알맞은 표준코드 반환


'''
* function : krx 개별종목 시세 추이
'''
def getKrxMarketPrice(stkCode: str, startDate: str, endDate: str) -> pd.DataFrame:
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
    return krx_data
    
'''
* function : naver 개별종목 시세 추이
'''
def getNaverMarketPrice(stkCode: str, startDate: str, endDate: str) -> pd.DataFrame:
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
    return naver_data

print(getKrxMarketPrice("005930","20220101","20221111"))

'''
* function : 개별 종목 시세 요청
'''
def getMarketPrice(stkCode: str, startDate:str, endDate:str) -> pd.DataFrame:
    krx_data: pd.DataFrame = getKrxMarketPrice(stkCode, startDate, endDate)
    naver_data: pd.DataFrame = getNaverMarketPrice(stkCode, startDate, endDate)


    fnguide_data = req.get("https://asp01.fnguide.com/SVO2/ASP/SVD_main.asp?pGB=1&gicode=A{005930}&cID=&MenuYn=Y&ReportGB=&NewMenuID=11&stkGb=&strResearchYN=",
                            headers=REQUEST_HEADERS,
    )

    # FnGuide 데이터 가공
    soup = BeautifulSoup(fnguide_data.text, 'html.parser')
    extraction = soup.find('table', attrs={'class':'us_table_ty1 table-hb thbg_g h_fix zigbg_no'}).findAll('tr')[-1].find('td', attrs={'class':'cle r'}).text
    flowRate = float(re.sub(pattern='\s', repl='', string=extraction).split('/')[1]);



