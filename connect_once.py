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

last_printed_date = None  # <- Track last printed bar

def on_bar_update(bars, has_new_bar):
    global last_printed_date
    latest_bar = bars[-1]

    if latest_bar.date != last_printed_date:
        print(latest_bar)
        last_printed_date = latest_bar.date  # Update tracker

bars.updateEvent += on_bar_update
ib.run()