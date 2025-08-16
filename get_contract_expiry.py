from ib_insync import *

ib = IB()
ib.connect('127.0.0.1', 7496, clientId=1)  # Run IB Gateway or TWS first

futures = ib.reqContractDetails(Future(symbol='NQ', exchange='CME'))
for f in futures:
    print(f.contract.lastTradeDateOrContractMonth)