import time
import schedule 
import requests
import json
from pymongo import MongoClient
import pandas as pd

import alphavantage.daily as alphavantagedaily
import alphavantage.monthly as alphavantagemonthly
import alphavantage.weekly as alphavantageweekly
# import alphavantage.conf as alphavantageconf
import mongodb.mongodatabase

def main():
    alphavantagemonthly.jprint()
    alphavantagedaily.jprint()
    alphavantageweekly.jprint()
    time.sleep(60)
schedule.every(1).minutes.do(main) 

if __name__ == "__main__":
    # count = 0 
    # while True: 
    #     schedule.run_pending() 
    #     time.sleep(1)
    main()
