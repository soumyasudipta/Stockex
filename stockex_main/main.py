import time
import schedule 
import requests
import json
from pymongo import MongoClient
import pandas as pd

# import alphavantage.daily as alphavantagedaily
# import alphavantage.monthly as alphavantagemonthly
# import alphavantage.weekly as alphavantageweekly
# import alphavantage.conf as alphavantageconf
# import alphavantage.daily_updated as daily_updated

# import yahoofinance.historical as historical
import yahoofinance.yahoofinance_manager as yahoofinance_manager

import mongodb.mongodatabase

def main():
    # alphavantagemonthly.jprint()
    # alphavantagedaily.jprint()
    # alphavantageweekly.jprint()
    # daily_updated.jprint()
    # historical.jprint()
    yahoofinance_manager.initiate()
    print('Inside main')

if __name__ == "__main__":
    # count = 0 
    # while True: 
    #     schedule.run_pending() 
    #     time.sleep(1)
    main()
