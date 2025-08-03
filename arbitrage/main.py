import ccxt
import api

# ex fn
def main():
    exchange = ccxt.binance({
        'enableRateLimit': True,
    })
    print(exchange)

    # print(api.factorial(6))
    print(api.a(1))

if __name__ == "__main__":
    main()
