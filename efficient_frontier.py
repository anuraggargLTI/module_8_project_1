import pandas as pd
import numpy as np
import symbol_data
import portfolio_data

# This function may have to be rewritten to accomodate Anurag's data functions
# as it performs all the analysis within the same loop as retrieving the data.
# The function accepts a list of stocks and returns a dictionary which contains
# the annual expected return, beta, standard deviation, and variance of each stock
def stock_data_calculator(stocks):
    # Generate a dataframe of daily returns for S&P 500
    spx_daily_returns = symbol_data.get_historical_data('SPX')
    spx_daily_returns = spx_daily_returns['Close'].pct_change().dropna()
    # Create an empty dictionary to store the stock data
    stock_data_dict = {}
    # This section can be replaced by Anurag's function
    for stock in stocks:
        stock_df = symbol_data.get_historical_data(stock)
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
    stock_data = stock_data_calculator(stocks)
    # Pull only the expected returns from the data
    for stock in stock_data:
        expected_returns.append(stock_data[stock]['expected_return'])
    # Multiply the expected returns by the weights to get weighted expected returns
    weighted_expected_returns = expected_returns * weights
    # Sum all these to get the expected return of the portfolio
    weighted_expected_returns = weighted_expected_returns.sum()
    return weighted_expected_returns 

# This function accepts a list of stocks and a list of weights which must be in the 
# same order. It returns the variance of the portfolio.
def portfolio_variance_calculator(stocks, weights):
    # Retrieve a dataframe of close prices for all stocks entered
    stock_df = portfolio_data.get_portfolio_historical_close_data(stocks)
    # Get the daily returns of each stock
    daily_returns = stock_df.pct_change().dropna()
    
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
    # Retrieve the closing price data for the stocks entered.
    stocks_df = portfolio_data.get_portfolio_historical_close_data(stocks)
    # Calculate the daily returns for each stock.
    daily_returns = stocks_df.pct_change().dropna()
    # Calculate cumulative returns for each stock in the portfolio.
    cumulative_returns = (1+daily_returns).cumprod() - 1
    # Multiply each stock by its respective weight.
    cumulative_returns = cumulative_returns * weights
    # Sum all the weighted cumulative returns
    cumulative_returns = cumulative_returns.sum(axis=1)
    return cumulative_returns

# This function accepts a list of stocks and a list of weights which must be in the 
# same order. It will return the 95% confidence interval for annual performance
# of the portfolio.
def portfolio_95percent_confidence_calculator(stocks, weights):
    expected_return = portfolio_expected_return_calculator(stocks, weights)
    variance = portfolio_variance_calculator(stocks, weights)
    lower_bound = expected_return - 2*variance
    upper_bound = expected_return + 2*variance
    return lower_bound, upper_bound

# Takes a naive approach to finding the portfolio with the minimum risk.
# There is a way to minimize a function with SciPy.optimize.minimize but 
# I can't figure out how to do it. 
# This function takes a list of stocks and creates 100 random portfolios
# and returns the one with the minimum risk.
def naive_minimum_risk_finder(stocks):
    # Create an iterator
    i = 0
    # Create dictionary to store the minimum risk portfolio
    min_risk = {}
    # Generate 100 portfolios with random weightings.
    # Save only the one with the minimim risk.
    while i < 100:
        weights = np.random.random(len(stocks))
        weights /= weights.sum()
        risk = portfolio_variance_calculator(stocks, weights)
        if not min_risk:
            min_risk['min_risk']={'risk':risk, 'weights':weights}
        elif risk < min_risk['min_risk']['risk']:
            min_risk['min_risk']={'risk':risk, 'weights':weights}
        i += 1
    return min_risk

# Takes a naive approach to finding the portfolio with the minimum risk.
# There is a way to minimize a function with SciPy.optimize.minimize but 
# I can't figure out how to do it. 
# This function takes a list of stocks and creates 100 random portfolios
# and returns the one with the maximum return.
def naive_maximum_return_finder(stocks):
    i = 0
    # Create dictionary to store the maximum return portfolio
    max_return = {}
    # Generate 100 portfolios with random weightings.
    # Save only the one with the minimim risk.
    while i < 100:
        weights = np.random.random(len(stocks))
        weights /= weights.sum()
        returns = portfolio_expected_return_calculator(stocks, weights)
        if not max_return:
            max_return['max_return']={'return':returns, 'weights':weights}
        elif returns > max_return['max_return']['return']:
            max_return['max_return']={'return':returns, 'weights':weights}
        i += 1
    return max_return