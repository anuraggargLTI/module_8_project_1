import pandas as pd
import db_initializer as di


di.initialize_symbol_master()
di.initialize_symbol_details()

def get_portfolio_historical_data(symbol_list):
    engine = di.return_engine_handler()
    start_counter = 0
    key_list=[]
    end_counter = len(symbol_list)
    while (start_counter<end_counter):
        symbol_name = symbol_list[start_counter]
        get_historical_data_query = f"""
         SELECT * from SYMBOL_DETAILS_{symbol_name}
        """
        symbol_details_df_temp= pd.read_sql_query(get_historical_data_query,con=engine)
        symbol_details_df_temp['symbol']=symbol_name
        key_list.append(symbol_name)
        if(start_counter==0):
            symbol_details_df = symbol_details_df_temp
        else:
            #symbol_details_df_temp.drop(['index','Date'],axis=1)
            symbol_details_df = pd.concat([symbol_details_df,symbol_details_df_temp],axis=1)
        start_counter = start_counter+1
    return symbol_details_df

def get_portfolio_historical_close_data(symbol_list):
   
    return get_portfolio_historical_data(symbol_list).copy().drop(columns=['High','Low','Open','Volume','Adj Close'])

