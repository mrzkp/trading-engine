import ccxt
import websockets
import asyncio
import api_module


# ex fn
def main():
    exchange = ccxt.binance({
        'enableRateLimit': True,
    })

    print(exchange)



if __name__ == "__main__":
    main()
