import ccxt
import json

"""
Test for reloading markets.
"""

def main():
    try:
        poloniex = ccxt.poloniex({'verbose': True}) # log HTTP requests`
        print(poloniex.has) # Fetches methods


        # poloniex.load_markets() # Gets markets
        # print(poloniex.id, poloniex.markets) # output a full list of all loaded markets

        # print(list(poloniex.markets.keys())) # output a short list of market symbols
        # print(poloniex.markets['SEN/USDT'])     # output single market details
        # poloniex.load_markets() # return a locally cached version, no reload, as we have already loaded earlier.
        #
        # This has some consequences. Doesn't use an API request, however, as a result, we aren't getting the most recent information. Is it possible to get a PARTICULAR market's most recent updates?

        # print("\n\n\n\n\n")
        # print("\n\n\n\n\n")
        # print("\n\n\n\n\n")
        # print("\n\n\n\n\n")
        # reloadedMarkets = poloniex.load_markets(True) # force HTTP reload = True
        #
        # This uses an API request, gets the most recent information.
        #

        """
        Note: If storing information locally, all objects are stored
        """

        # print("\n\n\n\n\n")
        # print("\n\n\n\n\n")
        # print("\n\n\n\n\n")
        # print("\n\n\n\n\n")
        # print(reloadedMarkets['HONKETH/USDT'])

    except KeyError as KE:
        print(KE)

if __name__ == "__main__":
    main()
