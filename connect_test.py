from ib_insync import *
util.startLoop()
import pandas as pd

ib = IB()
ib.connect('127.0.0.1', 7496, clientId=1)  # Run IB Gateway or TWS first

contract = Future(symbol='NQ', lastTradeDateOrContractMonth='20250919', exchange='CME', currency='USD')
ib.qualifyContracts(contract)

# Live candles
bars = ib.reqHistoricalData(
    contract,
    endDateTime='',
    durationStr='1 D',
    barSizeSetting='3 mins',
    whatToShow='TRADES',
    useRTH=False,
    formatDate=1,
    keepUpToDate=True
)

ib.disconnect()

df = util.df(bars)

print(df)

