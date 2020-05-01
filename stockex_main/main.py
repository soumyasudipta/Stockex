import time
import schedule

# import yahoofinance.historical as historical
import yahoofinance.yahoofinance_manager as yahoofinance_manager

from yahoofinance.constants import *


def minute_job():
    print('Started the minute wise job')
    yahoofinance_manager.initiate(period_1d, interval_1m, offset_1m)
    yahoofinance_manager.initiate(period_5d, interval_1m, offset_1m)
    print('Stopped the minute wise job')


def daily_job():
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
    # Task scheduling 
    # After every 10mins geeks() is called. 
    schedule.every().minute.do(minute_job)

    # # Every day at 12am or 00:00 time bedtime() is called. 
    schedule.every().day.at("00:00").do(daily_job)

    # # Loop so that the scheduling task 
    # keeps on running all time. 
    while True:
        # Checks whether a scheduled task 
        # is pending to run or not 
        schedule.run_pending()
        time.sleep(1)
    # read_last_timestamp(database_name, period_1d)
