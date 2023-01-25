import pandas as pd
from fire import Fire
import questionary
import portfolio_data as pfd
import symbol_data as sd

def show_task_menu():
    menu_choice = questionary.select("Welcome Guest , what do you want to do now?", choices=['See the price of a ticker','See details of a ticker']).ask()
    if menu_choice == 'See the price of a ticker':
        ticker_list = sd.get_all_tickers() 
        ticker_selected = questionary.select("Welcome Guest , here are few tickers for you to select from :", choices=ticker_list).ask()
        print(sd.get_ticker_price(ticker_selected))
        # print(choice_list)
    elif menu_choice == 'See details of a ticker':
        ticker_list = sd.get_all_tickers() 
        ticker_selected = questionary.select("Welcome Guest , here are few tickers for your choices?", choices=ticker_list).ask()
        print(sd.get_historical_data(ticker_selected))
  

if __name__=="__main__":
    Fire(show_task_menu)
