# Import libraries
import yfinance as yf
import time
import logging
from mongodb.constants import database_name
import mongodb.database_manager as mdb
from yahoofinance.constants import symbols


# Initialize
def get_ticker(symbol_list, ticker_period, ticker_interval, offset_value):
    try:
        data_to_insert = []

        ticker_data = yf.download(
            tickers=symbol_list,
            period=ticker_period,
            interval=ticker_interval,
            group_by='ticker',
            auto_adjust=True,
            threads=True,
            proxy=None)

        print("Insertion started", sep=" || ")

        for symbol in list(ticker_data.columns.levels[0]):

            last_timestamp = mdb.read_from_database(symbol, database_name, ticker_period)

            for index, row in ticker_data.dropna()[str(symbol)][:-offset_value].iterrows():
                date_time = str(index)[0:19]
                pattern = '%Y-%m-%d %H:%M:%S'
                epoch = int(time.mktime(time.strptime(date_time, pattern)))

                if (epoch > last_timestamp) or (last_timestamp is None):
                    data = {
                        '_id': symbol + '-' + str(epoch),
                        'symbol': str(symbol),
                        'open': float(row["Open"]),
                        'high': float(row["High"]),
                        'low': float(row["Low"]),
                        'close': float(row["Close"]),
                        'volume': float(row["Volume"]),
                        'timestamp': int(epoch)
                    }

                    data_to_insert.append(data)

        if len(data_to_insert) > 0:
            mdb.write_to_database(data_to_insert, database_name, ticker_period)

        print("Insertion ended")

    except Exception as e:
        print(e)
        logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
        logging.warning(str(e))


def change_ticker(ticker_period):
    mdb.drop_collection(database_name, ticker_period)


# Initialize
def initiate(ticker_period, ticker_interval, offset_value):
    symbol_string = ' '.join([str(symbol) for symbol in symbols])

    get_ticker(symbol_string, ticker_period, ticker_interval, offset_value)
