import pandas as pd
import db_initializer as di


symbol_list_df = pd.DataFrame()

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
        df_dict[symbol_name]= pd.read_sql_query(get_historical_data_query,con=engine)
        if 'date' in df_dict[symbol_name].columns:
            df_dict[symbol_name].index = df_dict[symbol_name]['date']
        if 'Date' in df_dict[symbol_name].columns:
            df_dict[symbol_name].index = df_dict[symbol_name]['Date']
        df_dict[symbol_name].index = pd.to_datetime(df_dict[symbol_name].index, infer_datetime_format = True)
        start_counter += 1
    symbol_details_df = pd.concat(df_dict.values(), axis=1, join = 'inner', keys=symbol_list)
    return symbol_details_df

def get_portfolio_historical_close_data(symbol_list):
   
    engine = di.return_engine_handler()
    start_counter = 0
    end_counter = len(symbol_list)
    df_dict = {}
    while (start_counter<end_counter):
        symbol_name = symbol_list[start_counter]
        get_historical_data_query = f"""
         SELECT * from SYMBOL_DETAILS_{symbol_name}
        """
        df_dict[symbol_name]= pd.read_sql_query(get_historical_data_query,con=engine)
        if 'date' in df_dict[symbol_name].columns:
            df_dict[symbol_name].index = df_dict[symbol_name]['date']
            df_dict[symbol_name].index = pd.to_datetime(df_dict[symbol_name].index, infer_datetime_format = True)
            df_dict[symbol_name] = df_dict[symbol_name][['close']]
        if 'Date' in df_dict[symbol_name].columns:
            df_dict[symbol_name].index = df_dict[symbol_name]['Date']
            df_dict[symbol_name].index = pd.to_datetime(df_dict[symbol_name].index, infer_datetime_format = True)
            df_dict[symbol_name] = df_dict[symbol_name][['Close']]
        start_counter += 1
    symbol_details_df = pd.concat(df_dict.values(), axis=1, join = 'inner', keys=symbol_list)
    return symbol_details_df

def search_by_symbol(symbol):
    engine = di.return_engine_handler()
    search_by_symbol_query = f"""
        SELECT * from SYMBOL_MASTER
        WHERE symbol like '%{symbol}%'
    """
    return pd.read_sql_query(search_by_symbol_query,con=engine).drop(columns='index')
    

def get_historical_data(symbol):
    engine = di.return_engine_handler()
    get_historical_data_query = f"""
        SELECT * from SYMBOL_DETAILS_{symbol}
    """
    
    stock_df =  pd.read_sql_query(get_historical_data_query,con=engine)
    if 'date' in stock_df.columns:
        stock_df.index = stock_df['date']
    if 'Date' in stock_df.columns:
        stock_df.index = stock_df['Date']
    stock_df.index = pd.to_datetime(stock_df.index, infer_datetime_format=True)
    return stock_df

def get_all_tickers():
    result_df=di.return_symbol_master_handler()
    return result_df['Symbol']

def get_ticker_price(symbol):
    return symbol
def search_by_symbol_list(symbol_list):
    di.initialize_symbol_master()
    engine = di.return_engine_handler()
    search_by_symbol_query = f"""
             SELECT * from SYMBOL_MASTER
             WHERE symbol IN ({symbol_list})
        """
    symbol_list_df = pd.read_sql_query(search_by_symbol_query,con=engine).drop(columns='index')
    symbol__list_df = symbol_list_df.drop(columns =["Avg Vol","Change"])
    symbol__list_df.columns = ["Symbol","Name","Price","%Change","Volume","Market Cap","PE Ratio"]
    return symbol_list_df

def return_symbol_list_data():
    return symbol_list_df