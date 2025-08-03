# Trading Engine

## Terminology

__Exchange__: The specific platform we we pulling data from.
__Market__: The specified trades available on that platform (e.g., ETH/BTC). Includes what you can actually trade and includes details such as prices, limits, and precisions.

__prices__: When we fetch them from ccxt, we are getting the previous and current trading rates for a market. To get current prices, we do fetch_ticker('BTC/USDT') and to get, say, the previous hours values, we can do something like fetch_ohlcv('BTC/USDT', '1h'). These are not stored statically within
__limits__:
__fees__:
__precisions__:

### Features
* Arbitrage - Order Execution
* Threshold L2 Order Book Depth - Order Execution

NOTES: Activate venv first:
python3 -m venv venv
source venv/bin/activate
