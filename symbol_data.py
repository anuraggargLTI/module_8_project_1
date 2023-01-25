import pandas as pd
import db_initializer as di
from fire import Fire

di.initialize_symbol_master()
di.initialize_symbol_details()

def search_by_symbol(symbol):
    engine = di.return_engine_handler()
    search_by_symbol_query = f"""
        SELECT * from SYMBOL_MASTER
        WHERE symbol like '%{symbol}%'
    """
    symbol_master_df = pd.read_sql_query(search_by_symbol_query,con=engine)
    print(symbol_master_df.head())

def get_historical_data(symbol):
    engine = di.return_engine_handler()
    get_historical_data_query = f"""
        SELECT * from SYMBOL_DETAILS_{symbol}
    """
    symbol_details_df = pd.read_sql_query(get_historical_data_query,con=engine)
    print(symbol_details_df.head())

def get_all_tickers():
    result_df=di.return_symbol_master_handler()
    return result_df['Symbol'].iloc[0:10]

def get_ticker_price(symbol):
    return symbol



