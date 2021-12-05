# This module is responsible for controlling all interactions with the database

# Imports
import pandas as pd
import data
import tqdm
import finra


def create_db():
    symbol_list = pd.read_csv('symbol_list.csv')
    # symbols = symbol_list['Symbol'].values.tolist()

    frames = []

    # For each symbol, try to get data on it. If not, remove it from symbol list, and update the symbol list
    for index, row in tqdm.tqdm(symbol_list.iterrows()):
        try:
            incoming_data = data.get_data(row['Symbol'])

            if incoming_data.empty:
                raise Exception("Error, invalid ticker")

            incoming_data['Squeeze'] = row['Squeeze']
            frames.append(incoming_data)

        except Exception:
            print(f"Couldn't get {row['Symbol']}")
            symbol_list.drop(symbol_list[symbol_list.Symbol == row['Symbol']].index, inplace=True)

    symbol_list.to_csv('symbol_list.csv', index=False)

    db = pd.concat(frames)
    db.to_csv('StockDatabase.csv', index=False)
    print(db.iloc[0])


def main():
    create_db()


if __name__ == '__main__':
    main()