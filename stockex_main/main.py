import time
import schedule 
import requests
import json
import pandas as pd
from pymongo import MongoClient

# import yahoofinance.historical as historical
import yahoofinance.yahoofinance_manager as yahoofinance_manager

import mongodb.mongodatabase

def main():
    yahoofinance_manager.initiate()
    print('Inside main')

if __name__ == "__main__":
    # count = 0 
    # while True: 
    #     schedule.run_pending() 
    #     time.sleep(1)
    main()
