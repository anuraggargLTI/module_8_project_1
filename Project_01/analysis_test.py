import os
import requests
import alpaca_trade_api as tradeapi
import pandas as pd
from dotenv import load_dotenv

response = requests.get('https://cloud.iexapis.com/beta/ref-data/symbols?token=MNDY')
print(response)

