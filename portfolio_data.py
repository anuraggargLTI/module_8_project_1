import pandas as pd
import db_initializer as di
from fire import Fire


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
        df_dict[symbol_name]= pd.read_sql_query(get_historical_data_query,con=engine)
        if 'date' in df_dict[symbol_name].columns:
            df_dict[symbol_name].index = df_dict[symbol_name]['date']
        if 'Date' in df_dict[symbol_name].columns:
            df_dict[symbol_name].index = df_dict[symbol_name]['Date']
        df_dict[symbol_name].index = pd.to_datetime(df_dict[symbol_name].index, infer_datetime_format = True)
        start_counter += 1
    symbol_details_df = pd.concat(df_dict.values(), axis=1, join = 'inner', keys=symbol_list)
    print(symbol_details_df)

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
    print(symbol_details_df)


def get_prebuilt_portfolio_historical_close_data(portfolios_nested_list): 
    engine = di.return_engine_handler()
    start_counter=0
    portfolio_dict={}
    symbol_dict ={}
    portfolio_details_list = []
    for portfolio_list in portfolios_nested_list:
        portfolio_holder_name = str(portfolio_list.keys())
        symbol_multi_list = portfolio_list.values()
        for symbol_list in symbol_multi_list:
            for symbol_name in symbol_list:
                get_historical_data_query = f"""
                    SELECT * from SYMBOL_DETAILS_{symbol_name}
                """
                symbol_dict[symbol_name]= pd.read_sql_query(get_historical_data_query,con=engine,index_col = 'Date')
                symbol_dict[symbol_name].index = pd.to_datetime(symbol_dict[symbol_name].index, infer_datetime_format = True)
                symbol_dict[symbol_name] = symbol_dict[symbol_name][['Close']]
                symbol_details_df = pd.concat(symbol_dict.values(), axis=1, join = 'inner', keys=symbol_list)
        portfolio_dict[portfolio_holder_name]=symbol_details_df
    return portfolio_dict

def test_function():
    dict = [{'Mark_Warner': ['INFY', 'CRM', 'DELL', 'MSFT', 'LRCX']}, {'Greg_Gianforte': ['AMD', 'AKAM', 'AMAT', 'EPAM', 'MU', 'MSFT']},{'Nancy_Pelosi': ['AAPL', 'ORCL', 'SAP', 'CRM', 'ZI', 'ZS']}]
    returned_dict = get_prebuilt_portfolio_historical_close_data(dict)   
    portfolio_holder_names = returned_dict.keys()
    for portfolio_holder_name in portfolio_holder_names:
        print(portfolio_holder_name)
        print(returned_dict[portfolio_holder_name].head())

if __name__=="__main__":
    Fire(test_function)
