## G-Docs Sys design (only accessible to maintainers of repo)
https://docs.google.com/document/d/1-MC-V0tMUkZKWz0wJgzzFASUWdYWJbORo4DWmuGOPCE/edit?usp=sharing

## High-Level Overview

1) Connect to websocket
2) Subscribe to the stream
3) Handling incoming data
4) Managing ping/pong + reconnects

## Low-Level Overview
1) Each package has their own main function. We only have one package at this time. We use util methods to establish  
## Server-Side
Sends HTTP request, then upgrades said HTTP request to a websocket conn.

Occasionally sends ping frames to ensure connection to client is still healthy. Receieves pong frame with same payload as what was sent in the ping frame.

## Client-Side
Dials the server through a HTTP request with a request to upgrade said connection to a websocket conn from the server.

While it is not returned, we are spinning and waiting for a response. We timeout after awhile.

We close connection after exiting out of main.

## To-Do:
#### IMMEDIATE
1) Establish websocket conn with binance server. Send pings and pongs back and forth to prolong said connection.
2) Get particular currency pair from binance and obtain orderbook.
3) From said orderbook (L2 orderbook), utilize backend API call (C++ side) to determine sufficient vol.

#### LATER
Support additional exchagnes, only support binance.
-> Requires modularizing connections and main function needs to take in a list of pre-defined exchanges.

