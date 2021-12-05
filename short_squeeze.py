import pandas as pd
import data


def check_short_squeeze(db):
    window_size = 30

    for i in range(db.shape[0] - window_size):
        if db.iloc[i].High * 5 < db.iloc[i+window_size].High:
            # print(db.iloc[0].Symbol)
            return True

    return False


def main():

    symbols = ['AAPL', 'AMD', 'BAC', 'DIS', 'SPCE', 'AMC', 'GME', 'WKHS']

    for each in symbols:
        db = data.get_data(each)
        print(each, check_short_squeeze(db))


if __name__ == '__main__':
    main()