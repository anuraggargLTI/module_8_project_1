import pandas as pd
import db_initializer as di


di.initialize_symbol_master()
di.initialize_symbol_details()

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



