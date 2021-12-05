# This module will be responsible for grabbing data. A separate module will grab data and populate a dataframe.

# Imports
import yfinance as yf
import finra
import pandas as pd
import numpy as np
import math


def get_data(symbol):

    ticker_to_get = yf.Ticker(symbol)
    finra_symbol = finra.get_hidden_from_symbol(symbol)

    nan_value = float("NaN")
    # This will get all the data available on Yahoo Finance. We will adjust later to accept an input date, which will be
    # useful for when our database has some data, and we want to only fetch the new stuff
    ticker_to_get = ticker_to_get.history(period='max')

    # Get rid of useless stats
    ticker_to_get.drop(columns=['Stock Splits', 'Dividends'], inplace=True)

    # Add the symbol and Finra hidden symbol to entry
    ticker_to_get.insert(0, 'Symbol', symbol)
    ticker_to_get.insert(1, 'Finra Symbol', finra_symbol)

    # Get raw PE and Short interest data
    short_interest_dates, short_interest, pe_dates, pe = finra.get_short_float(finra_symbol)

    # Convert into separate dataframes (allows for built in merge by date with Pandas)
    finra_db_short_interest = pd.DataFrame({'Date': short_interest_dates, 'Short Interest (%)': short_interest})
    finra_db_pe = pd.DataFrame({'Date': pe_dates, "PE Ratio": pe})

    # Merge the two DB's by date
    finra_db = finra_db_short_interest.merge(right=finra_db_pe, how='outer', on='Date')

    # Anywhere the PE ratio is unspecified, means the PE ratio is negative, so replace Nan with negative 1.
    # Likewise, because we dont know how negative the PE ratio is, we make the positive PE ratio +1 for normalization
    finra_db['PE Ratio'].fillna(0, inplace=True)
    finra_db['PE Ratio'] = np.where((finra_db['PE Ratio'].astype('float64') > 0), 1, finra_db['PE Ratio'])

    # Merge entire db by date
    final_db = ticker_to_get.merge(right=finra_db, how='outer', on='Date')
    # final_db = ticker_to_get.merge()

    final_db.replace('', nan_value, inplace=True)
    final_db.dropna(inplace=True)
    print(final_db.to_string())

    return final_db


if __name__ == '__main__':
    symbol = 'LMND'
    db = get_data(symbol)

    db.to_csv(f'{symbol}.csv', index=False)
