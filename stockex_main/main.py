import time
import datetime
import schedule
import os

from yahoofinance.constants import *
import yahoofinance.yahoofinance_manager as yahoofinance_manager

from yahoofinance.constants import *


def minute_job():
    print('Started the minute wise job')
    yahoofinance_manager.initiate(period_1d, interval_1m)
    yahoofinance_manager.initiate(period_5d, interval_1m)
    print('Stopped the minute wise job')


def daily_delete_job():
    print('Started the daily wise job')
    yahoofinance_manager.change_ticker(interval_1d)
    print('Stopped the daily wise job')


def daily_insert_job():
    print('Started the daily wise job')
    yahoofinance_manager.initiate(period_1mo, interval_1d)
    yahoofinance_manager.initiate(period_3mo, interval_1d)
    yahoofinance_manager.initiate(period_6mo, interval_1d)
    yahoofinance_manager.initiate(period_1y, interval_1d)
    # yahoofinance_manager.initiate(period_5y, interval_1d)
    yahoofinance_manager.initiate(period_ytd, interval_1d)
    # yahoofinance_manager.initiate(period_max, interval_1d)
    print('Stopped the daily wise job')


if __name__ == "__main__":
    os.environ['TZ'] = 'America/Detroit'
    time.tzset()

    now = datetime.datetime.now()
    current_time = int(now.strftime("%H")) * 60 + int(now.strftime("%M"))
    start = 9 * 60 + 25
    stop = 16 * 60 + 5

    if start < current_time < stop:
        # After every min minute_job() is called.
        schedule.every().minute.do(minute_job)
        print(current_time)
        print(start)
        print(stop)

    # Task scheduling
    # # From Monday to Friday at 9:25am time daily_deletion() is called.
    schedule.every().monday.at("09:25").do(daily_delete_job)
    schedule.every().tuesday.at("09:25").do(daily_delete_job)
    schedule.every().wednesday.at("09:25").do(daily_delete_job)
    schedule.every().thursday.at("09:25").do(daily_delete_job)
    schedule.every().friday.at("09:25").do(daily_delete_job)

    # # From Monday to Friday at 12am or 00:00 time daily_job() is called.
    schedule.every().monday.at("00:00").do(daily_insert_job)
    schedule.every().tuesday.at("00:00").do(daily_insert_job)
    schedule.every().wednesday.at("00:00").do(daily_insert_job)
    schedule.every().thursday.at("00:00").do(daily_insert_job)
    schedule.every().friday.at("00:00").do(daily_insert_job)

    daily_insert_job()
    minute_job()

    # # Loop so that the scheduling task 
    # keeps on running all time. 
    while True:
        # Checks whether a scheduled task 
        # is pending to run or not 
        schedule.run_pending()
        time.sleep(1)
