#**Dynamic Stock Portfolio Analyzer Using Dash
## Module 8 Project 1 (Group 1)
### A portfolio analyzer: Build an app that compares the performance of portfolios that are composed of different assets. Include calculations, tables, financial models, and Monte Carlo simulations. Also include information about past and future performance of the portfolios, as well as suggestions for improving that performance.

###**Politician stock portfolios:

###For this portion of the project we wanted to compare user portfolios with those of some of the wealthiest politicians. Using information from opensecrets.org, we selected Mark Warner (Senator VA), Greg Gianforte (Gov Montana), and Nancy Pelosi (Congresswoman CA). Considering the extent of these individuals stock portfolios, we elected to use the investment capital each of these individuals had invested in their top 5-6 publicly traded stocks in 2018 (most recent available portfolio data). Alpaca API used to create concatonated dataframes with closing prices. Monte Carlo simulations created and plotted for each of the politicians and summary statistics generated.

###*With an investment of $116,000,000.00 there is a 95% chance that over the next 10 years the Warner sample portfolio (warner_tickers= ['SPY', 'AKREX', 'TROW', 'COHOX', 'VTI']) will end with a range between $100,001,587.36 and $429,029,712.85

###*With an investment of $94,500,000.00 there is a 95% chance that over the next 10 years the Gianforte sample portfolio (gianforte_tickers=['QQQ', 'SPY', 'VTI', 'FICO', 'WK', 'CRM']) will end with a range between $196,935,882.15 and $1,037,571,694.74

###*With an investment of $64,000,000.00 there is a 95% chance that over the next 10 years the Pelosi sample portfolio (pelosi_tickers=['AAPL', 'V', 'DIS', 'CRM', 'META', 'CMCSA']) will end with a range between $361,820,204.05 and $487,164,4514.04


