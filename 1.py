from sqlalchemy import create_engine

engine = create_engine('mysql://root@localhost/stock')
a = ['finance'     ,    
        'insurance'     ,     
        'investortrust',  
        'private'     ,         
        'bank'       ,             
        'otherfinance',    
        'otherfund',          
        'othercor',            
        'individual',        
        'foreigner',          
        'otherforeigner' ]

for i in a:
    try:
        print('alter table investor2 rename column tradevalue_{i}_buy to value_{i}_buy')
        engine.execute(f'alter table investor2 rename column tradevalue_{i}_buy to value_{i}_buy')
        engine.execute(f'alter table investor2 rename column tradevalue_{i}_sell to value_{i}_sell')
        engine.execute(f'alter table investor2 rename column tradevalue_{i}_net to value_{i}_net')
    except: pass
engine.connect().close()