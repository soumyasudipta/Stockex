# Import libraries
import yfinance as yf
import time
from mongodb.constants import database_name
import mongodb.database_manager as mdb
from yahoofinance.constants import symbols
from logger import logging_manager
import prediction.StockPricePrediction as StockPricePrediction


# Initialize
def get_ticker_data(symbol_list_string, ticker_period, ticker_interval):

    try:
        data_to_insert = []

        ticker_data = yf.download(
            tickers=symbol_list_string,
            period=ticker_period,
            interval=ticker_interval,
            group_by='ticker',
            auto_adjust=True,
            threads=True)

        print("Insertion started for : " + ticker_period)

        # Start getting data from downloaded data 
        for symbol in ticker_data.columns.levels[0]:

            last_timestamp = mdb.read_from_database(symbol, database_name, ticker_period)

            for index, row in ticker_data[str(symbol)].dropna().iterrows():
                date_time = str(index)[0:19]
                pattern = '%Y-%m-%d %H:%M:%S'
                epoch = int(time.mktime(time.strptime(date_time, pattern)))

                if last_timestamp == 0 or last_timestamp < epoch:

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

            if(ticker_period == '1y'):
                StockPricePrediction.predict_next(ticker_data[symbol][["Open","High","Low","Close"]],symbol)

        if len(data_to_insert) > 0:
            mdb.write_to_database(data_to_insert, database_name, ticker_period)

        print("Insertion ended for : " + ticker_period)

    except Exception as e:
        logging_manager.logging_do(e, 40)


def get_info_data(info):

    print("Insertion started for : " + info)

    data_to_insert = []

    for symbol in symbols:
        try:
            company_info = yf.Ticker(symbol).info

            data = {
                '_id': symbol,
                'data': company_info
            }

            data_to_insert.append(data)

        except Exception as e:
            logging_manager.logging_do(e, 40)

    if len(data_to_insert) > 0:
        mdb.write_to_database(data_to_insert, database_name, info)
   
    print("Insertion ended for : " + info)


def change_collection(collection):
    mdb.drop_collection(database_name, collection)


def initiate(ticker_period, ticker_interval):

    symbol_list_string = ' '.join([str(symbol) for symbol in symbols])
    get_ticker_data(symbol_list_string, ticker_period, ticker_interval)
