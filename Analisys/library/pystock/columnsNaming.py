import pandas as pd
import numpy as np

class Type:
    dataTypes = {
        'stk_code'      : np.str_,   
        'cpr_name'      : np.str_,
        'list_date'     : np.datetime64,  
        'mkt_name'      : np.str_,   
        'list_shares'   : np.int64,
        'std_code'      : np.str_,
        'mkt_code'      : np.int32,
        'mkt_name'      : np.str_,
        'tr_date'       : np.datetime64,    
        'tr_value'      : np.int64,   
        'tr_volume'     : np.int64,  
        'tr_prevcomp'   : np.int32,
        'fluc_rt'       : np.float32,    
        'fluc_code'     : np.int32,  
        'mkt_capital'    : np.int64, 
        'tr_clsprc'     : np.int32,  
        'tr_hgprc'      : np.int32,   
        'tr_lwprc'      : np.int32,   
        'tr_opnprc'     : np.int32,
        'tr_foreiner_rt': np.float32,

        'finance'       : np.int64,        
        'insurance'     : np.int64,      
        'investortrust' : np.int64,  
        'private'       : np.int64,        
        'bank'          : np.int64,           
        'otherfinance'  : np.int64,   
        'otherfund'     : np.int64,      
        'othercor'      : np.int64,       
        'individual'    : np.int64,     
        'foreigner'     : np.int64,      
        'otherforeigner': np.int64, 
        'total'         : np.int64,          
        'tr_date'       : np.datetime64,     
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
        'ISU_SRT_CD'    : 'stk_code',               #종목코드
        'ISU_ABBRV'     : 'cpr_name',               #회사이름
        'LIST_DD'       : 'list_date',              #상장일
        'MKT_TP_NM'     : 'mkt_name',               #시장구분(코스피, 코스닥, ...)
        'LIST_SHRS'     : 'list_shares',            #상장 주식수
        'full_code'     : 'std_code',
        'short_code'    : 'stk_code',
        'codeName'      : 'cpr_name',
        'marketCode'    : 'mkt_code',
        'marketName'    : 'mkt_name',
        'TRD_DD'        : 'tr_date',             #거래일
        'ACC_TRDVAL'    : 'tr_value',            #거래대금
        'ACC_TRDVOL'    : 'tr_volume',           #거래량
        'CMPPREVDD_PRC' : 'tr_prevcomp',          #전일대비
        'FLUC_RT'       : 'fluc_rt',        #등락율
        'FLUC_TP_CD'    : 'fluc_code',        #등락코드(1: 상승, 2: 하락, 0: 동일)
        'MKTCAP'        : 'mkt_capital',            #시가총액
        'TDD_CLSPRC'    : 'tr_clsprc',      #종가
        'TDD_HGPRC'     : 'tr_hgprc',       #고가
        'TDD_LWPRC'     : 'tr_lwprc',        #저가
        'TDD_OPNPRC'    : 'tr_opnprc',       #시가
        
        # Naver Naming
        '날짜'           : 'tr_date',
        '시가'           : 'tr_opnprc',
        '고가'           : 'tr_hgprc',
        '종가'           : 'tr_clsprc',
        '저가'           : 'tr_lwprc',
        '거래량'          : 'tr_volume',
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

        'TRDVAL1'       : 'finance',            #금융투자
        'TRDVAL2'       : 'insurance',          #보험
        'TRDVAL3'       : 'investortrust',      #투신
        'TRDVAL4'       : 'private',            #사모
        'TRDVAL5'       : 'bank',               #은행
        'TRDVAL6'       : 'otherfinance',       #기타금융   
        'TRDVAL7'       : 'otherfund',          #연기금 등
        'TRDVAL8'       : 'othercor',           #기타법인
        'TRDVAL9'       : 'individual',         #개인
        'TRDVAL10'      : 'foreigner',          #외국인
        'TRDVAL11'      : 'otherforeigner',      #기타외국인
        'TRDVAL_TOT'    : 'total',              #전체
        'TRD_DD'        : 'tr_date',     
    }

    @staticmethod
    def setColumnsNaming(df: pd.DataFrame, errors='ignore') -> pd.DataFrame:
        df = df.rename(columns=naming.COLUMNS_NAMING, errors=errors, inplace=False)
        df = Type.setTypes(df)

        return df
        
