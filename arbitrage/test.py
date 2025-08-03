import ccxt
import json
import api

"""
Test for reloading markets.
"""

def main():
    try:
        poloniex = ccxt.poloniex({'verbose': True}) # log HTTP requests`
        print(poloniex.has) # Fetches methods
        poloniex.set_sandbox_mode(True)

        poloniex.load_markets() # Gets markets
        print(poloniex.id, poloniex.markets) # output a full list of all loaded markets

        print("\n\n\n\n\n")
        print("\n\n\n\n\n")
        print("\n\n\n\n\n")
        print("\n\n\n\n\n")
        print(list(poloniex.markets.keys())) # output a short list of market symbols
        print(poloniex.markets['SEN/USDT'])     # output single market details
        inp = poloniex.markets['SEN/USDT']
        print(api.test(inp))
        # poloniex.load_markets() # return a locally cached version, no reload, as we have already loaded earlier.
        #
        # This has some consequences. Doesn't use an API request, however, as a result, we aren't getting the most recent information. Is it possible to get a PARTICULAR market's most recent updates?
        #
        # I do not think it is possible. load_markets() refreshes ALL markets.

        # print("\n\n\n\n\n")
        # print("\n\n\n\n\n")
        # print("\n\n\n\n\n")
        # print("\n\n\n\n\n")
        # reloadedMarkets = poloniex.load_markets(True) # force HTTP reload = True
        #
        # This uses an API request, gets the most recent information.

        """
        Note: If storing information locally, all objects are stored in the Heap, which can be slow.

        If we were to pass this information to our C API, we will need to pass the pointer to the functions, hence, we are still going to be making reads/writes to the heap?
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
