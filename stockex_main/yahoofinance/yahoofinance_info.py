# Import libraries
import yfinance as yf
import time
from mongodb.constants import database_name
import mongodb.database_manager as mdb
from yahoofinance.constants import symbols
from logger import logging_manager


# Initialize
def insert_info(info):

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


def change_ticker(info):
    mdb.drop_collection(database_name, info)

