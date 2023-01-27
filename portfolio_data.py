import pandas as pd
import db_initializer as di


di.initialize_symbol_master()
di.initialize_symbol_details()

def get_portfolio_historical_data(symbol_list):
    engine = di.return_engine_handler()
    start_counter = 0
    end_counter = len(symbol_list)
    df_dict = {}
    while (start_counter<end_counter):
        symbol_name = symbol_list[start_counter]
        get_historical_data_query = f"""
         SELECT * from SYMBOL_DETAILS_{symbol_name}
        """
        df_dict[symbol_name]= pd.read_sql_query(get_historical_data_query,con=engine,index_col = 'Date')
        df_dict[symbol_name].index = pd.to_datetime(df_dict[symbol_name].index, infer_datetime_format = True)
        start_counter += 1
    symbol_details_df = pd.concat(df_dict.values(), axis=1, join = 'inner', keys=symbol_list)
    return symbol_details_df

def get_portfolio_historical_close_data(symbol_list):
   
    return get_portfolio_historical_data(symbol_list).copy().drop(columns=['High','Low','Open','Volume','Adj Close'])

