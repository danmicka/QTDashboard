import asyncio
from ib_async import IB, util, Future

async def main():
    ib = IB()
    await ib.connectAsync('127.0.0.1', 7496, clientId=1)

    try:
        # qualify the contract (good practice)
        [contract] = await ib.qualifyContractsAsync(
            Future(symbol='MYM', lastTradeDateOrContractMonth='20250919', exchange='CBOT')
        )

        bars = await ib.reqHistoricalDataAsync(
            contract,
            endDateTime='',
            durationStr='100 D',
            barSizeSetting='5 mins',
            whatToShow='TRADES',
            useRTH=False,
            formatDate=1,
            keepUpToDate=False
        )
        if not bars:
            raise RuntimeError("No bars returned; check permissions/exchange.")

        df = util.df(bars)
        df.to_csv("YM_5min_last100days.csv", index=False)
        print("Saved NQ_5min_last2days.csv with", len(df), "rows")

    finally:
        # <-- sync method; do NOT await
        if ib.isConnected():
            ib.disconnect()

if __name__ == "__main__":
    asyncio.run(main())