# Import libraries
import yfinance as yf
import time
import logging
import pandas as pd

# Import userdefined libraries
import mongodb.mongodatabase as mdb
from yahoofinance.constants import symbols

# Initialize
def ticker_do(symbol_list):

    try:
        ticker_data = yf.download(
            tickers = symbol_list,
            period = "6mo",
            interval = "1d",
            group_by = 'ticker',
            auto_adjust = True,
            prepost = True,
            threads = True,
            proxy = None)

        for x in symbols:
            insert_data = []
            for index, row in ticker_data[str(x)].iterrows():
                date_time = str(index)
                pattern = '%Y-%m-%d %H:%M:%S'
                epoch = int(time.mktime(time.strptime(date_time, pattern)))

                data = {
                    '_id':x + '-' + str(epoch),
                    'open':float(row["Open"]),
                    'high':float(row["High"]),
                    'low':float(row["Low"]),
                    'close':float(row["Close"]),
                    'volume':float(row["Volume"]),
                    'timestamp':epoch
                }

                insert_data.append(data)

            mdb.insert(insert_data,'monthyly_6',str(x))
    
    except Exception:
        print("Cannot connect to network")
        logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
        logging.warning(x + " : " + Exception)

    print("Insertion ended for : " + x)

# Initialize
def initiate():
    
    symbol_list = ""
    for x in symbols:
        symbol_list = symbol_list + " " + x

    ticker_do(symbol_list)
