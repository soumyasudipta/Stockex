import yfinance as yf
import mongodb.mongodatabase as mdb
from yahoofinance.constants import symbols
import time
import logging

def jprint():
    for symbol in symbols:
        print("Initiating insertion for : " + symbol,end =" || ")
        try:
            stock = yf.Ticker(str(symbol))
            hist = stock.history(period="max")

            insert_data = []

            for index, row in hist.iterrows():
                date_time = str(index)
                pattern = '%Y-%m-%d %H:%M:%S'
                epoch = int(time.mktime(time.strptime(date_time, pattern)))

                data = {
                    '_id':symbol + '-' + str(epoch),
                    'open':float(row["Open"]),
                    'high':float(row["High"]),
                    'low':float(row["Low"]),
                    'close':float(row["Close"]),
                    'volume':float(row["Volume"]),
                    'timestamp':epoch
                }

                insert_data.append(data)

            mdb.insert(insert_data,'historical_data',str(symbol))
        
        except Exception:
            print("Cannot connect to network")
            logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
            logging.warning(symbol + " : " + Exception)

        print("Insertion ended for : " + symbol)