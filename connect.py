from ib_insync import *
util.startLoop()

ib = IB()
ib.connect('127.0.0.1', 7496, clientId=1)  # Run IB Gateway or TWS first

contract = Future(symbol='NQ', lastTradeDateOrContractMonth='20250919', exchange='CME', currency='USD')
ib.qualifyContracts(contract)

# Live candles
bars = ib.reqHistoricalData(
    contract,
    endDateTime='',
    durationStr='2 D',
    barSizeSetting='1 min',
    whatToShow='TRADES',
    useRTH=False,
    formatDate=1,
    keepUpToDate=True
)

def on_bar_update(bars, has_new_bar):
    print(bars[-1])  # Each new bar as it arrives
bars.updateEvent += on_bar_update
ib.run()