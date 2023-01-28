import pandas as pd
from fire import Fire
import questionary
import portfolio_data as pfd
import symbol_data as sd

def show_task_menu():
    menu_choice = questionary.select("Welcome Guest , do you want to work on a Stock or on Portfolio",choices=['Stock','Portfolio']).ask()
    if menu_choice == 'Stock':
        sub_menu_choice = questionary.select("Please tell me what you want to do in Stocks :", choices=['See the historical prices of a ticker',
                                                                                             'See details of a ticker',
                                                                                             'Get daily returns of a ticker'
                                                                                              ]).ask()
        if sub_menu_choice == 'See the historical prices of a ticker':
            ticker_list = sd.get_all_tickers().iloc[0:10].append(pd.Series(["Show me more Tickers"]))
            ticker_selected = questionary.select("Welcome Guest , here are first 10 tickers for you to select from :", choices=ticker_list).ask()
            if ticker_selected!='Show me more Tickers':
                 print(sd.get_historical_data(ticker_selected))
            else:
                ticker_list = sd.get_all_tickers().iloc[11:21]
                print(ticker_list)
                print(type(ticker_list))
                ticker_selected = questionary.select("Welcome Guest , here are the next 10 tickers for you to select from :", choices=ticker_list).ask()
                if ticker_selected!='Show me more Tickers':
                 print(sd.get_historical_data(ticker_selected))
        
        elif sub_menu_choice == 'See details of a ticker':
            ticker_list = sd.get_all_tickers() 
            ticker_selected = questionary.select("Welcome Guest , here are few tickers for your choices?", choices=ticker_list).ask()
            print(sd.search_by_symbol(ticker_selected))
    if menu_choice == 'Portfolio':
            sub_menu_choice = questionary.select("Please tell me what you want to do in Portfolios :" , choices=['See the performance of pre-built portfolios',
                                                                                             'Build and see the performance of portfolio',
                                                                                             'Compare portfolios']).ask()  

if __name__=="__main__":
    Fire(show_task_menu)
