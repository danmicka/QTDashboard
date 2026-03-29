import time, datetime
from ib_insync import *
util.startLoop()
import pandas as pd
import pytz

from QuaterlyCyclesv2 import QuarterlyCycles

from lightweight_charts import Chart

local_timezone = 'America/New_York'
target_timezone = 'America/New_York'

tz_ny = pytz.timezone("America/New_York")
now_ny = datetime.now(tz_ny)

if __name__ == '__main__':

    qt =  QuarterlyCycles(now_ny, local_timezone=local_timezone, target_timezone=target_timezone)
    
    ib = IB()
    ib.connect('127.0.0.1', 7496, clientId=1)  # Run IB Gateway or TWS first

    contract = Future(symbol='NQ', lastTradeDateOrContractMonth='20250919', exchange='CME', currency='USD')
    ib.qualifyContracts(contract)

    # Live candles
    bars = ib.reqHistoricalData(
        contract,
        endDateTime='',
        durationStr='1 D',
        barSizeSetting='5 mins',
        whatToShow='TRADES',
        useRTH=False,
        formatDate=1,
        keepUpToDate=True
    )

    ib.disconnect()

    df = util.df(bars)
 
    # Drop the volume column
    if 'volume' in df.columns:
        df = df.drop(columns=['volume'])

    df.rename(columns={'date': 'date', 'open': 'open', 'high': 'high', 'low': 'low', 'close': 'close'}, inplace=True)
    
    daily_qt, daily_start, daily_end = qt.get_daily_quarter_()
    prev_daily_qt, prev_daily_start, prev_daily_end = qt.get_previous_daily_quarter_()

    sess_qt, sess_start, sess_end = qt.get_90_minute_quarter_()
    prev_sess_start = sess_start - qt.get_previous_90_minute_quarter_()
    prev_sess_end = sess_start

    # True opens
    daily_open, daily_open_time = get_true_open(df, daily_start, daily_end)
    sess_open, sess_open_time = get_true_open(df, sess_start, sess_end)

    
    print(df)

    time.sleep(1)

    chart = Chart()

    chart.set(df)

    chart.show(block=True)

