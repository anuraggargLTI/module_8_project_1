import pandas as pd
from pathlib import Path
import numpy as np


spx_df = pd.read_csv(Path('./Resources/SPX.csv'), 
                    index_col='Date', 
                    parse_dates=True,
                    infer_datetime_format=True
                    )
spx_daily_returns = spx_df['Close'].pct_change().dropna()
# This function may have to be rewritten to accomodate Anurag's data functions
# as it performs all the analysis within the same loop as retrieving the data.
# The function accepts a list of stocks and returns a dictionary which contains
# the annual expected return, beta, standard deviation, and variance of each stock
def stock_data_calculator(stocks):
    # Create an empty dictionary to store the stock data
    stock_data_dict = {}
    # This section can be replaced by Anurag's function
    for stock in stocks:
        stock_df = pd.read_csv(
            Path(f'./Resources/{stock}.csv'), 
            index_col = 'Date', 
            parse_dates = True, 
            infer_datetime_format=True
            )
        
        daily_returns = stock_df['Close'].pct_change().dropna()
        daily_returns_df = pd.concat(
            [daily_returns, spx_daily_returns], 
            axis=1,
            join='inner', 
            keys = [stock, 'SPX']
            )
        covariance = daily_returns_df[stock].cov(daily_returns_df['SPX'])
        beta = covariance / daily_returns_df['SPX'].var()

        std = daily_returns.std()

        var = daily_returns.var()

        expected_return = .035 + beta*(.1-.035)
        
        stock_data_dict[stock] = {'expected_return': expected_return, 'std': std, 'var': var, 'beta': beta}
    return stock_data_dict


# This function accepts a list of stocks and a list of weights which must be in the 
# same order. It will return the expected return of the portfolio.
def portfolio_expected_return_calculator(stocks, weights):
    # Create an empty list which will hold the expected returns
    expected_returns = []
    # Gather the stock data from the symbol_data_calculator function
    symbol_data = symbol_data_calculator(stocks)
    # Pull only the expected returns from the data
    for symbol in symbol_data:
        expected_returns.append(symbol_data[symbol]['expected_return'])
    # Multiply the expected returns by the weights to get weighted expected returns
    weighted_expected_returns = expected_returns * weights
    # Sum all these to get the expected return of the portfolio
    weighted_expected_returns = weighted_expected_returns.sum()
    return weighted_expected_returns 

# This function accepts a list of stocks and a list of weights which must be in the 
# same order. It returns the variance of the portfolio.
def portfolio_variance_calculator(symbols, weights):
    # Getting the data. This part can be replaced by anurag's function
    df_dict = {}
    for symbol in symbols:
        symbol_df = pd.read_csv(
            Path(f'./Resources/{symbol}.csv'),
            index_col = 'Date',
            parse_dates = True,
            infer_datetime_format = True
            )
        df_dict[symbol] = symbol_df['Close']

    prices_df = pd.concat(df_dict.values(), axis = 1, join = 'inner', keys = symbols_list)
    daily_returns = prices_df.pct_change().dropna()
    
    # Get the covariance array of the portfolio using the .cov() method.
    portfolio_cov = np.array(daily_returns.cov())

    # Get the standard deviation of each asset in the portfolio using the .std() method.
    portfolio_std = np.array(daily_returns.std())

    # Cross multiply the std array with the transposition of itself.
    portfolio_stdT = np.transpose(np.array([portfolio_std]))
    portfolio_std_cp = portfolio_std * portfolio_stdT

    # Get the correlation matrix by dividing the covariance matrix by the standard deviation matrix.
    correlation_matrix = portfolio_cov / portfolio_std_cp

    # Get weighted standard deviation and save the transposition of that array.
    weighted_std = portfolio_std * weights
    weighted_stdT = np.transpose(np.array([weighted_std]))

    # Calculate portfolio variance by first multiplying the covariance matrix by the 
    # weighted standard deviation array. This will give an array which is 
    # 1x<the number of stocks in the portfolio>
    portfolio_var = np.matmul(weighted_std, correlation_matrix)
    # Then multiplying that array by the transposition of the weighted standard deviation array.
    # This will give a single value.
    portfolio_var = np.matmul(portfolio_var, weighted_stdT)
    # And finally taking the square root of that value.
    portfolio_var = np.sqrt(portfolio_var)
    return portfolio_var

# This function accepts a list of stocks and a list of weights which must be in the 
# same order. It will return a dataframe which contains the cumulative returns
# of the entire portfolio. This can be used to plot the performance of the portfolio.
def portfolio_performance_calculator(stocks, weights):
    # This section can be replaced by Anurag's function
    df_dict = {}
    for symbol in stocks:
        symbol_df = pd.read_csv(
            Path(f'./Resources/{symbol}.csv'),
            index_col = 'Date',
            parse_dates = True,
            infer_datetime_format = True
            )
        symbol_df['daily_returns'] = symbol_df['Close'].pct_change().dropna()
        df_dict[symbol] = symbol_df[['daily_returns']]

    stocks_df = pd.concat(df_dict.values(), axis = 1, join = 'inner', keys = stocks)

    # Calculate cumulative returns for each stock in the portfolio.
    cumulative_returns = (1+stocks_df).cumprod() - 1
    # Multiply each stock by its respective weight.
    cumulative_returns = cumulative_returns * weights
    # Sum all the weighted cumulative returns
    cumulative_returns = cumulative_returns.sum(axis=1)
    return cumulative_returns


