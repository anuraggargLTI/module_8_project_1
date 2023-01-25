import pandas as pd
from pathlib import Path
from fire import Fire
import sqlalchemy as sql

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
    create_symbol_details_query = """
        CREATE TABLE SYMBOL_DETAILS (
            DATE DATE,
            HIGH BIGINT,
            LOW BIGINT,
            OPEN BIGINT,
            CLOSE BIGINT,
            VOLUME BIGINT,
            ADJ_CLOSE BIGINT
        )
    """
    #engine.execute(create_symbol_details_query)
    insert_into_symbol_details()


def insert_into_symbol_master(symbol_master_df):
    symbol_master_df.to_sql("SYMBOL_MASTER",engine,if_exists="replace")

def insert_into_symbol_details():
    #symbol_details_df.to_sql("SYMBOL_DETAILS",engine,if_exists="replace")
    symbol_details_df = pd.read_csv(Path("./Resources/AAPL.csv"))
    symbol_details_df.to_sql("SYMBOL_DETAILS_AAPL",engine,if_exists='replace',index=False)
    symbol_details_df = pd.read_csv(Path("./Resources/ACN.csv"))
    symbol_details_df.to_sql("SYMBOL_DETAILS_ACN",engine,if_exists='replace',index=False)
    symbol_details_df = pd.read_csv(Path("./Resources/ADBE.csv"))
    symbol_details_df.to_sql("SYMBOL_DETAILS_ADBE",engine,if_exists='replace',index=False)
    symbol_details_df = pd.read_csv(Path("./Resources/ADI.csv"))
    symbol_details_df.to_sql("SYMBOL_DETAILS_ADI",engine,if_exists='replace',index=False)
    symbol_details_df = pd.read_csv(Path("./Resources/ADSK.csv"))
    symbol_details_df.to_sql("SYMBOL_DETAILS_ADSK",engine,if_exists='replace',index=False)
    symbol_details_df = pd.read_csv(Path("./Resources/AKAM.csv"))
    symbol_details_df.to_sql("SYMBOL_DETAILS_AKAM",engine,if_exists='replace',index=False)
    symbol_details_df = pd.read_csv(Path("./Resources/AMAT.csv"))
    symbol_details_df.to_sql("SYMBOL_DETAILS_AMAT",engine,if_exists='replace',index=False)
    symbol_details_df = pd.read_csv(Path("./Resources/AMD.csv"))
    symbol_details_df.to_sql("SYMBOL_DETAILS_AMD",engine,if_exists='replace',index=False)
    symbol_details_df = pd.read_csv(Path("./Resources/CDW.csv"))
    symbol_details_df.to_sql("SYMBOL_DETAILS_CDW",engine,if_exists='replace',index=False)
    symbol_details_df = pd.read_csv(Path("./Resources/CRM.csv"))
    symbol_details_df.to_sql("SYMBOL_DETAILS_CRM",engine,if_exists='replace',index=False)
    symbol_details_df = pd.read_csv(Path("./Resources/DELL.csv"))
    symbol_details_df.to_sql("SYMBOL_DETAILS_DELL",engine,if_exists='replace',index=False)
    symbol_details_df = pd.read_csv(Path("./Resources/DOCU.csv"))
    symbol_details_df.to_sql("SYMBOL_DETAILS_DOCU",engine,if_exists='replace',index=False)
    symbol_details_df = pd.read_csv(Path("./Resources/EPAM.csv"))
    symbol_details_df.to_sql("SYMBOL_DETAILS_EPAM",engine,if_exists='replace',index=False)
    symbol_details_df = pd.read_csv(Path("./Resources/FIS.csv"))
    symbol_details_df.to_sql("SYMBOL_DETAILS_FIS",engine,if_exists='replace',index=False)
    symbol_details_df = pd.read_csv(Path("./Resources/FISV.csv"))
    symbol_details_df.to_sql("SYMBOL_DETAILS_FISV",engine,if_exists='replace',index=False)
    symbol_details_df = pd.read_csv(Path("./Resources/IBM.csv"))
    symbol_details_df.to_sql("SYMBOL_DETAILS_IBM",engine,if_exists='replace',index=False)
    symbol_details_df = pd.read_csv(Path("./Resources/INFY.csv"))
    symbol_details_df.to_sql("SYMBOL_DETAILS_INFY",engine,if_exists='replace',index=False)
    symbol_details_df = pd.read_csv(Path("./Resources/LRCX.csv"))
    symbol_details_df.to_sql("SYMBOL_DETAILS_LRCX",engine,if_exists='replace',index=False)
    symbol_details_df = pd.read_csv(Path("./Resources/MSFT.csv"))
    symbol_details_df.to_sql("SYMBOL_DETAILS_MSFT",engine,if_exists='replace',index=False)
    symbol_details_df = pd.read_csv(Path("./Resources/MU.csv"))
    symbol_details_df.to_sql("SYMBOL_DETAILS_MU",engine,if_exists='replace',index=False)
    symbol_details_df = pd.read_csv(Path("./Resources/NOW.csv"))
    symbol_details_df.to_sql("SYMBOL_DETAILS_NOW",engine,if_exists='replace',index=False)
    symbol_details_df = pd.read_csv(Path("./Resources/NVDA.csv"))
    symbol_details_df.to_sql("SYMBOL_DETAILS_NVDA",engine,if_exists='replace',index=False)
    symbol_details_df = pd.read_csv(Path("./Resources/ORCL.csv"))
    symbol_details_df.to_sql("SYMBOL_DETAILS_ORCL",engine,if_exists='replace',index=False)
    symbol_details_df = pd.read_csv(Path("./Resources/SAP.csv"))
    symbol_details_df.to_sql("SYMBOL_DETAILS_SAP",engine,if_exists='replace',index=False)
    symbol_details_df = pd.read_csv(Path("./Resources/TEAM.csv"))
    symbol_details_df.to_sql("SYMBOL_DETAILS_TEAM",engine,if_exists='replace',index=False)
    symbol_details_df = pd.read_csv(Path("./Resources/TXN.csv"))
    symbol_details_df.to_sql("SYMBOL_DETAILS_TXN",engine,if_exists='replace',index=False)
    symbol_details_df = pd.read_csv(Path("./Resources/WDAY.csv"))
    symbol_details_df.to_sql("SYMBOL_DETAILS_WDAY",engine,if_exists='replace',index=False)
    symbol_details_df = pd.read_csv(Path("./Resources/WORK.csv"))
    symbol_details_df.to_sql("SYMBOL_DETAILS_WORK",engine,if_exists='replace',index=False)

def  return_engine_handler():
    return engine

def return_symbol_master_handler():
    symbol_master_df = pd.read_csv(Path("./Resources/Technology Sector List.csv"))
    return symbol_master_df

