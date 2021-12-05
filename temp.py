import pandas as pd


if __name__ == '__main__':
    db = pd.read_csv('symbol_list_backup.csv')

    db = db[['Symbol']]
    db.head()
    db.to_csv('symbol_list.csv', index=False)