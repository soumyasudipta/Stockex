# Import libraries
import yfinance as yf
import time
import logging
import pandas as pd
import numpy as np
import os
from mongodb.constants import database_name
import mongodb.database_manager as mdb
from yahoofinance.constants import symbols

os.environ['TZ'] = 'America/Detroit'


# Initialize
def get_ticker(symbol_list, ticker_period, ticker_interval, offset_value):
    try:
        ticker_data = yf.download(
            tickers=symbol_list,
            period=ticker_period,
            interval=ticker_interval,
            group_by='ticker',
            auto_adjust=True,
            prepost=True,
            threads=True,
            proxy=None)

        for x in symbols:
            print("Insertion started for : " + x, sep=" || ")
            insert_data = []
            for index, row in ticker_data[str(x)][:-offset_value].iterrows():
                date_time = str(index)[0:19]
                pattern = '%Y-%m-%d %H:%M:%S'
                epoch = int(time.mktime(time.strptime(date_time, pattern)))

                data = {
                    '_id': x + '-' + str(epoch),
                    'symbol': str(x),
                    'open': float(row["Open"]),
                    'high': float(row["High"]),
                    'low': float(row["Low"]),
                    'close': float(row["Close"]),
                    'volume': float(row["Volume"]),
                    'timestamp': epoch
                }

                insert_data.append(data)

            mdb.insert(insert_data, database_name, ticker_period)
            print("Insertion ended for : " + x)

    except Exception:
        print("Cannot connect to network")
        logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
        logging.warning(x + " : " + str(Exception))


# Initialize
def initiate(ticker_period, ticker_interval, offset_value):
    symbol_list = ""
    for x in symbols:
        symbol_list = symbol_list + " " + x

    get_ticker(symbol_list, ticker_period, ticker_interval, offset_value)
