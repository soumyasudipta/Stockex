import time
import datetime
import schedule
import os

from yahoofinance.constants import *
import yahoofinance.yahoofinance_manager as yahoofinance_manager


def minute_job():
    now = datetime.datetime.now()
    current_time = int(now.strftime("%H")) * 60 + int(now.strftime("%M"))

    start = 13 * 60 + 25
    stop = 20 * 60 + 25

    while start < current_time < stop:
        # After every min minute_job() is called.
        print(start, end="  |  ")
        print(current_time, end="  |  ")
        print(stop)
        print('Started the minute wise job')
        yahoofinance_manager.initiate(period_1d, interval_1m)
        yahoofinance_manager.initiate(period_5d, interval_1m)
        print('Stopped the minute wise job')
        now = datetime.datetime.now()
        current_time = int(now.strftime("%H")) * 60 + int(now.strftime("%M"))


def daily_delete_job():
    print('Started the daily wise job')
    yahoofinance_manager.change_collection(period_1d)
    yahoofinance_manager.change_collection(period_5d)
    print('Stopped the daily wise job')


def daily_insert_job():
    print('Started the daily wise job')
    yahoofinance_manager.initiate(period_1mo, interval_1d)
    yahoofinance_manager.initiate(period_3mo, interval_1d)
    yahoofinance_manager.initiate(period_6mo, interval_1d)
    yahoofinance_manager.initiate(period_1y, interval_1d)
    yahoofinance_manager.initiate(period_5y, interval_1d)
    yahoofinance_manager.initiate(period_ytd, interval_1d)
    # yahoofinance_manager.initiate(period_max, interval_1d)
    print('Stopped the daily wise job')


if __name__ == "__main__":
    print("Started Script")

    # Task scheduling
    # From Monday to Friday at 9:45am EDT time minute_job() is called.
    schedule.every().monday.at("13:45").do(minute_job)
    schedule.every().tuesday.at("13:45").do(minute_job)
    schedule.every().wednesday.at("13:45").do(minute_job)
    schedule.every().thursday.at("13:45").do(minute_job)
    schedule.every().friday.at("13:45").do(minute_job)

    # From Monday to Friday at 9:25am EDT time daily_deletion() is called.
    schedule.every().monday.at("13:25").do(daily_delete_job)
    schedule.every().tuesday.at("13:25").do(daily_delete_job)
    schedule.every().wednesday.at("13:25").do(daily_delete_job)
    schedule.every().thursday.at("13:25").do(daily_delete_job)
    schedule.every().friday.at("13:25").do(daily_delete_job)

    # # From Monday to Friday at 12am or 00:00 EDT time daily_job() is called.
    schedule.every().tuesday.at("04:05").do(daily_insert_job)
    schedule.every().wednesday.at("04:05").do(daily_insert_job)
    schedule.every().thursday.at("04:05").do(daily_insert_job)
    schedule.every().friday.at("04:05").do(daily_insert_job)
    schedule.every().saturday.at("04:05").do(daily_insert_job)


    # Loop so that the scheduling task 
    # keeps on running all time. 
    while True:
        # Checks whether a scheduled task 
        # is pending to run or not 
        schedule.run_pending()
        time.sleep(1)
