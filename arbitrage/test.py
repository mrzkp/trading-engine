import ccxt
import json

"""
Test for reloading markets.
"""

def main():
    try:
        poloniex = ccxt.poloniex({'verbose': True}) # log HTTP requests`
        poloniex.load_markets() # request markets
        print(poloniex.id, poloniex.markets)   # output a full list of all loaded markets

        print(list(poloniex.markets.keys())) # output a short list of market symbols
        print(poloniex.markets['SEN/USDT'])     # output single market details
        poloniex.load_markets() # return a locally cached version, no reload

        print("\n\n\n\n\n")
        print("\n\n\n\n\n")
        print("\n\n\n\n\n")
        print("\n\n\n\n\n")
        reloadedMarkets = poloniex.load_markets(True) # force HTTP reload = True

        print("\n\n\n\n\n")
        print("\n\n\n\n\n")
        print("\n\n\n\n\n")
        print("\n\n\n\n\n")
        print(reloadedMarkets['HONKETH/USDT'])

    except KeyError as KE:
        print(KE)

if __name__ == "__main__":
    main()
