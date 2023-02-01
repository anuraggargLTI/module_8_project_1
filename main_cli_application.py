import pandas as pd
from fire import Fire
import questionary
import portfolio_data as pfd
import os


symbol_list = ""
def take_tickers_input():
    symbol_list = questionary.text("Please enter the tickers you want to see the portfolio for :").ask()
    symbol_list=symbol_list
    print(pfd.search_by_symbol_list(symbol_list))
    os.system("python app.py")
def return_tickers_entered():
    return symbol_list

























if __name__=="__main__":
    Fire(take_tickers_input)