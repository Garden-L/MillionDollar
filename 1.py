from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('mysql://root@localhost/stock',)

def prefixSum(stkcode, date):
    sql=f"select I.stk_code, I.tr_date, M.flow_rate, M.fruc_rate,\
        (M.tr_clsprc - sum(M.tr_clsprc) over W1) * 100 / sum(M.tr_clsprc) over W1 AS std_cls_rt,\
        (M.tr_hgprc - sum(M.tr_clsprc) over W1) * 100 / sum(M.tr_clsprc) over W1 AS std_hg_rt,\
        (max(M.tr_hgprc) over W3 - sum(M.tr_clsprc) over W1) * 100 / M.tr_clsprc AS after_max_hg_rt,\
        (min(M.tr_lwprc) over W3 - sum(M.tr_clsprc) over W1) * 100 / M.tr_clsprc AS after_min_lw_rt,\
        (avg(M.tr_clsprc) over W3 - sum(M.tr_clsprc) over W1) * 100 / M.tr_clsprc AS after_avg_cls_rt,\
        max(M.fruc_rate) OVER W2 AS prev_max_fruc_rate,\
        sum(value_finance_net) over W2 * 100 / (sum(M.mkt_capital) over W1  * sum(M.flow_rate) over W1 / 100)  AS finance,\
        sum(value_insurance_net) over W2 * 100 / (sum(M.mkt_capital) over W1  * sum(M.flow_rate) over W1 / 100)  AS insurance,\
        sum(value_investortrust_net) over W2 * 100 / (sum(M.mkt_capital) over W1  * sum(M.flow_rate) over W1 / 100)  AS investortrust,\
        sum(value_private_net) over W2 * 100 / (sum(M.mkt_capital) over W1  * sum(M.flow_rate) over W1 / 100)  AS private,\
        sum(value_bank_net) over W2 * 100 / (sum(M.mkt_capital) over W1  * sum(M.flow_rate) over W1 / 100)  AS bank,\
        sum(value_otherfinance_net) over W2 * 100 / (sum(M.mkt_capital) over W1  * sum(M.flow_rate) over W1 / 100)  AS otherfinance,\
        sum(value_otherfund_net) over W2 * 100 / (sum(M.mkt_capital) over W1  * sum(M.flow_rate) over W1 / 100)  AS otherfund,\
        sum(value_othercor_net) over W2 * 100 / (sum(M.mkt_capital) over W1  * sum(M.flow_rate) over W1 / 100)  AS othercor,\
        sum(value_individual_net) over W2 * 100 / (sum(M.mkt_capital) over W1  * sum(M.flow_rate) over W1 / 100)  AS individual,\
        sum(value_foreigner_net) over W2 * 100 / (sum(M.mkt_capital) over W1  * sum(M.flow_rate) over W1 / 100)  AS foreigner,\
        sum(value_otherforeigner_net) over W2 * 100 / (sum(M.mkt_capital) over W1  * sum(M.flow_rate) over W1 / 100)  AS otherforeigner,\
        (sum(value_finance_net) over W2 + sum(value_insurance_net) over W2 + sum(value_investortrust_net) over W2 + sum(value_private_net) over W2\
        + sum(value_bank_net) over W2 + sum(value_otherfinance_net) over W2 +sum(value_otherfund_net) over W2) * 100 / (sum(M.mkt_capital) over W1  * sum(M.flow_rate) over W1 / 100) AS sum_ins,\
        (sum(value_foreigner_net) over W2 * 100 + sum(value_otherforeigner_net) over W2 * 100) / (sum(M.mkt_capital) over W1  * sum(M.flow_rate) over W1 / 100) AS sum_foreigner\
        from investors I INNER JOIN (SELECT stk_code, tr_date, tr_hgprc, tr_clsprc, tr_lwprc, tr_value,mkt_capital,flow_rate, (tr_clsprc - tr_opnprc)*100/ tr_opnprc AS fruc_rate from MARKETPRICES) M\
                            ON I.STK_CODE = M.STK_CODE AND I.TR_DATE = M.TR_DATE\
        WHERE I.stk_code ='{stkcode}' and I.tr_date >=date('{date}') \
        WINDOW W1 AS (ORDER BY tr_date ASC ROWS BETWEEN 1 PRECEDING AND 1 PRECEDING),\
            W2 AS (ORDER BY tr_date ASC ROWS BETWEEN 60 PRECEDING AND 1 PRECEDING),\
            W3 AS (ORDER BY tr_date ASC ROWS BETWEEN 0 FOLLOWING AND 20 FOLLOWING)"

    df = pd.read_sql(sql, engine.connect())
    df['tr_date'] = pd.to_datetime(df['tr_date'])
    return df


def getstkcode():
    sql='select stk_code from marketprices\
        group by stk_code;'

    return pd.read_sql(sql, engine.connect())


code = getstkcode();

for i in code['stk_code']:
    try:
        df = prefixSum(i, "20170101")
        print(df)
        df.to_sql('prevPrefixSum_30', engine.connect(), if_exists='append', index=False)
        print("성공")
    except:
        print('lost')
engine.connect().close()