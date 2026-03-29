import time, datetime
from ib_insync import *
util.startLoop()
import pandas as pd

from lightweight_charts import Chart

if __name__ == '__main__':

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
        
    print(df)

    time.sleep(1)

    chart = Chart()

    chart.set(df)

    chart.show(block=True)

