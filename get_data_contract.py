import argparse
import asyncio
import time, random
from ib_async import IB
from ib_async.contract import Stock

# Coroutine that requests and prints historical data for one symbol
async def fetch_data(ib: IB, symbol: str):
    print(f"Requesting data for {symbol}")

    contract = Stock(symbol, "SMART", "USD")
    bars = await ib.reqHistoricalDataAsync(
        contract,
        endDateTime="",
        durationStr="1 D",
        barSizeSetting="1 min",
        whatToShow="TRADES",
        useRTH=True
    )
    print(f"\n=== {symbol} ===")
    for bar in bars[-10:]:
        print(f"{bar.date} O={bar.open:.2f} H={bar.high:.2f} L={bar.low:.2f} C={bar.close:.2f} V={int(bar.volume)}")

    # print(f"\n✅ Finished fetching {symbol} in {delay} seconds")

# Main coroutine that connects once and launches all requests concurrently
async def main(symbols):
    ib = IB()
    await ib.connectAsync('127.0.0.1', 7497, clientId=1)  # Run IB Gateway or TWS first

    start = time.perf_counter()  # ⏱️ Start timing

    # Launch fetch_data tasks concurrently using the same connection
    fetch_data_coroutines = [
        fetch_data(ib, symbol) for symbol in symbols
    ]
    print(f"Fetching data for {len(symbols)} symbols: {', '.join(symbols)}")
    # Use asyncio.gather to run all coroutines concurrently
    # Note: Using *() to unpack the list of coroutines
    # This allows us to run all fetch_data calls concurrently
    await asyncio.gather(*fetch_data_coroutines)

    end = time.perf_counter()  # ⏱️ End timing

    print(f"\nFinished fetching {len(symbols)} symbols in {end - start:.2f} seconds")

    ib.disconnect()

# start program
if __name__ == "__main__":
    # Parse command line arguments
    p = argparse.ArgumentParser(description="Fetch 1-min bars for multiple symbols from IBKR")
    p.add_argument("symbols", nargs="+", help="One or more ticker symbols, e.g. AAPL MSFT TSLA")
    args = p.parse_args()

    # Run the main coroutine
    asyncio.run(main(args.symbols))