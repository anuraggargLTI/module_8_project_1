import pandas as pd
from pathlib import Path
from fire import Fire
import sqlalchemy as sql
import os

database_connection_string = "sqlite:///"
engine = sql.create_engine(database_connection_string)
symbol_master_df =pd.DataFrame()
symbol_details_df = pd.DataFrame()
def read_files():
    initialize_symbol_master()
    initialize_symbol_details()

def initialize_symbol_master():
    symbol_master_df = pd.read_csv(Path("./Resources/Technology Sector List.csv"))
    insert_into_symbol_master(symbol_master_df)

def initialize_symbol_details():
    insert_into_symbol_details()

def insert_into_symbol_master(symbol_master_df):
    symbol_master_df.to_sql("SYMBOL_MASTER",engine,if_exists="replace")

def insert_into_symbol_details():
    #symbol_details_df.to_sql("SYMBOL_DETAILS",engine,if_exists="replace")
    filename_list = os.listdir("./Resources/")
    for file in filename_list:
        if(file!='Technology Sector List.csv' and file!='MutualFunds.csv' and file!='ETFs.csv' and file!='.gitkeep'):
            symbol_details_df = pd.read_csv(Path(f"./Resources/{file}"))
            symbol = file.split(".csv")[0]
            symbol_details_df.to_sql(f"SYMBOL_DETAILS_{symbol}",engine,index=False,if_exists="replace")

def  return_engine_handler():
    return engine

def return_symbol_master_handler():
    symbol_master_df = pd.read_csv(Path("./Resources/Technology Sector List.csv"))
    return symbol_master_df