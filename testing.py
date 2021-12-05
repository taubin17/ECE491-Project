import pandas as pd


def main(symbol):

    db = pd.read_csv(f'{symbol}.csv')

    db['Date'] = pd.to_datetime(db['Date'])

    last_date = '2020-01-30'
    last_date = pd.to_datetime(last_date)

    new_db = db.loc[(db['Date'] > last_date)]

    new_db.to_csv(f'{symbol}.csv', index=False)


if __name__ == '__main__':
    symbol = 'LMND'
    main(symbol)