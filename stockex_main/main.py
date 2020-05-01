import time
import schedule
import os

import yahoofinance.yahoofinance_manager as yahoofinance_manager

from yahoofinance.constants import *


def minute_job():

    print('Started the minute wise job')
    yahoofinance_manager.initiate(period_1d, interval_1m, offset_1m)
    yahoofinance_manager.initiate(period_5d, interval_1m, offset_1m)
    print('Stopped the minute wise job')


def daily_delete_job():

    print('Started the daily wise job')
    yahoofinance_manager.change_ticker(interval_1d)
    print('Stopped the daily wise job')


def daily_insert_job():

    print('Started the daily wise job')
    yahoofinance_manager.initiate(period_1mo, interval_1d, offset_1d)
    yahoofinance_manager.initiate(period_3mo, interval_1d, offset_1d)
    yahoofinance_manager.initiate(period_6mo, interval_1d, offset_1d)
    yahoofinance_manager.initiate(period_1y, interval_1d, offset_1d)
    yahoofinance_manager.initiate(period_5y, interval_1d, offset_1d)
    yahoofinance_manager.initiate(period_ytd, interval_1d, offset_1d)
    yahoofinance_manager.initiate(period_max, interval_1d, offset_1d)
    print('Stopped the daily wise job')


if __name__ == "__main__":
    os.environ['TZ'] = 'America/Detroit'
    time.tzset()

    # Task scheduling 
    # After every min minute_job() is called.
    schedule.every().minute.do(minute_job)

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

    # # Loop so that the scheduling task 
    # keeps on running all time. 
    while True:
        # Checks whether a scheduled task 
        # is pending to run or not 
        schedule.run_pending()
        time.sleep(1)
