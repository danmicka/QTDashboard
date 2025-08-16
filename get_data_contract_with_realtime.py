import argparse
import asyncio
import time, random
from ib_async import IB, RealTimeBar
from ib_async.contract import Future

SYMBOL_INFO = {
    'ES': {
        'type': Future,
        'exchange': 'CME',
        'lastTradeDateOrContractMonth': '20250919',
        'currency': 'USD'
    },
    'NQ': {
        'type': Future,
        'exchange': 'CME',
        'lastTradeDateOrContractMonth': '20250919',
        'currency': 'USD'
    },
    'YM': {
        'type': Future,
        'exchange': 'CBOT',
        'lastTradeDateOrContractMonth': '20250919',
        'currency': 'USD'
    },
    # Example for Index:
    # 'SPX': {
    #     'type': Index,
    #     'exchange': 'CBOE',
    #     'currency': 'USD'
    # },
}

def build_contract(symbol: str):
    info = SYMBOL_INFO.get(symbol)
    if not info:
        raise ValueError(f"Symbol info not found for '{symbol}'")

    contract_class = info['type']
    contract_kwargs = {
        'symbol': symbol,
        'exchange': info['exchange'],
        'currency': info['currency'],
    }

    # Only include this field if the contract type is Future
    if contract_class == Future:
        contract_kwargs['lastTradeDateOrContractMonth'] = info['lastTradeDateOrContractMonth']

    return contract_class(**contract_kwargs)

# Coroutine that requests and prints historical data for one symbol
# ES / NQ : CME
# YM : CBOT
async def fetch_opening_range(ib: IB, symbol: str, opening_range_minutes: int = 15):
    print(f"Requesting data for {symbol}")
    
    contract = build_contract(symbol)
    
    bars = await ib.reqHistoricalDataAsync(
        contract,
        endDateTime="",
        durationStr="1 D",
        barSizeSetting="1 min",
        whatToShow="TRADES",
        useRTH=True
    )
    
    opening_range_bars = bars[:opening_range_minutes]

    print(f"== Opening range for {symbol} ==")
    for bar in opening_range_bars:
        print(bar)

    highs = [b.high for b in opening_range_bars]
    lows  = [b.low  for b in opening_range_bars]
    
    return symbol, max(highs), min(lows)


async def monitor_breakout(ib: IB, symbol: str):

    contract = build_contract(symbol)

    ticker = ib.reqRealTimeBars(
        contract,
        barSize=5,
        whatToShow="TRADES",
        useRTH=True
    )

    def on_bar(bars: list[RealTimeBar], hasNewBar: bool):
        print(f"\n--- {symbol} 5-sec bars (count={len(bars)}) ---")
        for bar in bars:
            print(bar)

    ticker.updateEvent += on_bar

    # keep this coroutine alive indefinitely
    await asyncio.Event().wait()


# Main coroutine that connects once and launches all requests concurrently
async def main(symbols):
    ib = IB()
    await ib.connectAsync("127.0.0.1", 7496, clientId=1)

    # Launch fetch_data tasks concurrently using the same connection
    fetch_data_coroutines = [
        fetch_opening_range(ib, symbol) for symbol in symbols
    ]
    print(f"Fetching data for {len(symbols)} symbols: {', '.join(symbols)}")
    results = await asyncio.gather(*fetch_data_coroutines)
    
    print("\n=== Opening Ranges ===")
    monitors = []
    for result in results:
        symbol, high, low = result
        print(f"{symbol} Opening Range High={high:.2f} Low={low:.2f}")
        monitors.append(monitor_breakout(ib, symbol))

    print("Starting real-time 5-sec monitors...\n")
    await asyncio.gather(*monitors)

    ib.disconnect()

# start program
if __name__ == "__main__":
    # Parse command line arguments
    p = argparse.ArgumentParser(description="Fetch 1-min bars for multiple symbols from IBKR")
    p.add_argument("symbols", nargs="+", help="One or more ticker symbols, e.g. AAPL MSFT TSLA")
    args = p.parse_args()

    # Run the main coroutine
    asyncio.run(main(args.symbols))