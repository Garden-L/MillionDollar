import pandas as pd
import numpy as np

class Type:
    dataTypes = {
        'stkCd'      : np.str_,   
        'cpr_name'      : np.str_,
        'list_date'     : np.datetime64,  
        'mkt_name'      : np.str_,   
        'lstShrs'   : np.int64,
        'std_code'      : np.str_,
        'mkt_code'      : np.int32,
        'mkt_name'      : np.str_,
        'trDt'       : np.datetime64,    
        'trTrans'      : np.int64,   
        'trVol'     : np.int64,  
        'tr_prevcomp'   : np.int32,
        'fluc_rt'       : np.float32,    
        'fluc_code'     : np.int32,  
        'mktCap'    : np.int64, 
        'trClsPrc'     : np.int32,  
        'trHgPrc'      : np.int32,   
        'trLwPrc'      : np.int32,   
        'trOpnPrc'     : np.int32,
        'tr_foreiner_rt': np.float32,

        'fin'       : np.int64,        
        'insur'     : np.int64,      
        'inves' : np.int64,  
        'priv'       : np.int64,        
        'bank'          : np.int64,           
        'othFin'  : np.int64,   
        'othFund'     : np.int64,      
        'othCorp'      : np.int64,       
        'indi'    : np.int64,     
        'fore'     : np.int64,      
        'othFore': np.int64, 
        'total'         : np.int64,          
        'trDt'       : np.datetime64,     


        'mktCd'          : np.str_, 
        'sctCd'          : np.str_,
        'sctNm'      : np.str_,
        'mktSrtNm'       : np.str_,
        'mktNm'       : np.str_,   
        'tr_compprc'    : np.int32,
    }

    @staticmethod
    def setTypes(df: pd.DataFrame):
        types = {}

        for column in df.columns:
            if(Type.dataTypes[column] != np.str_):
                df[column] = df[column].str.replace(',', '')
            types[column] = Type.dataTypes[column]
        
        return df.astype(dtype=types)

    
class naming:
    '''
    *** Naming rule ***
    std         = Standard 
    stk         = Stock
    mkt         = Market
    crp         = coration
    tr          = trading
    fluc        = fluc
    rt          = rate
    comp        = compare
    cls         = close
    opn         = open
    hg          = high
    lw          = low
    prc         = price

    '''
    COLUMNS_NAMING = {
        'ISU_CD'        : 'std_code',               #표준코드
        'ISU_SRT_CD'    : 'stkCd',               #종목코드
        'ISU_ABBRV'     : 'cpr_name',               #회사이름
        'LIST_DD'       : 'list_date',              #상장일
        'MKT_TP_NM'     : 'mkt_name',               #시장구분(코스피, 코스닥, ...)
        'LIST_SHRS'     : 'lstShrs',            #상장 주식수
        'full_code'     : 'std_code',
        'short_code'    : 'stkCd',
        'sctNm'      : 'cpr_name',
        'marketCode'    : 'mkt_code',
        'marketName'    : 'mkt_name',
        'TRD_DD'        : 'trDt',             #거래일
        'ACC_TRDVAL'    : 'trTrans',            #거래대금
        'ACC_TRDVOL'    : 'trVol',           #거래량
        'CMPPREVDD_PRC' : 'tr_prevcomp',          #전일대비
        'FLUC_RT'       : 'fluc_rt',        #등락율
        'FLUC_TP_CD'    : 'fluc_code',        #등락코드(1: 상승, 2: 하락, 0: 동일)
        'MKTCAP'        : 'mktCap',            #시가총액
        'TDD_CLSPRC'    : 'trClsPrc',      #종가
        'TDD_HGPRC'     : 'trHgPrc',       #고가
        'TDD_LWPRC'     : 'trLwPrc',        #저가
        'TDD_OPNPRC'    : 'trOpnPrc',       #시가
        
        # Naver Naming
        '날짜'           : 'trDt',
        '시가'           : 'trOpnPrc',
        '고가'           : 'trHgPrc',
        '종가'           : 'trClsPrc',
        '저가'           : 'trLwPrc',
        '거래량'          : 'trVol',
        '외국인소진율'     : 'tr_foreiner_rt',

        # Trade Of Investor Naming
        'ASK_TRDVAL'        : 'SELL_TRADE_VALUE',       #매도 거래대금
        'ASK_TRDVOL'        : 'SELL_VOLUME',            #매도 거래량
        'BID_TRDVAL'        : 'BUY_TRADE_VALUE',        #매수 거래대금
        'BID_TRDVOL'        : 'BUY_VOLUME',             #매수 거래량
        'CONV_OBJ_TP_CD'    : 'NONE',                   #NONE
        'INVST_TP_NM'       : 'INVESTOR_NAME',          #투자자이름
        'NETBID_TRDVAL'     : 'BUY_NET_TRADE_VALUE',    #순매수 거래대금
        'NETBID_TRDVOL'     : 'BUY_NET_VOLUME',         #순매수 거래량 

        'TRDVAL1'       : 'fin',            #금융투자
        'TRDVAL2'       : 'insur',          #보험
        'TRDVAL3'       : 'inves',      #투신
        'TRDVAL4'       : 'priv',            #사모
        'TRDVAL5'       : 'bank',               #은행
        'TRDVAL6'       : 'othFin',       #기타금융   
        'TRDVAL7'       : 'othFund',          #연기금 등
        'TRDVAL8'       : 'othCorp',           #기타법인
        'TRDVAL9'       : 'indi',         #개인
        'TRDVAL10'      : 'fore',          #외국인
        'TRDVAL11'      : 'othFore',      #기타외국인
        'TRDVAL_TOT'    : 'total',              #전체
        'TRD_DD'        : 'trDt',     

        # index codes 
        'full_code'     : 'mktCd',
        'short_code'    : 'sctCd',
        'codeName'      : 'sctNm',
        'marketCode'    : 'mktSrtNm',
        'marketName'    : 'mktNm',

        'STR_CMP_PRC'   : 'tr_compprc',

    }

    @staticmethod
    def setColumnsNaming(df: pd.DataFrame, errors='ignore') -> pd.DataFrame:
        df = df.rename(columns=naming.COLUMNS_NAMING, errors=errors, inplace=False)
        df = Type.setTypes(df)

        return df
        
