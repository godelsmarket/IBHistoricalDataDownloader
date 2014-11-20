##IB Historical Data Downloader
================================
####Info

This code can be used to download quotes for the constituents of the S&P500 through Interactive Brokers' API using Python 2.7 and IbPy.

It will pause for 10 seconds after each request so that you won't go over the 60 symbol a minute limit. Also, it keeps track of which symbols you have downloaded. If you need to check for missed symbols go to the "downloaded_symbols.csv" file and match it to the entire S&P500 list. Other than the fact that you need a folder named "csv_day_test" in the same folder as the python script, there's not much to using this. It's pretty simple (and shouldn't hang like the GUI version sometimes does).

It's hard coded to do "1 min" bars over the course of "1 D". Change these if you'd like to download other data. You can also add/subtract symbols as you would expect. If you want it to print data it receives into the Python window, you can remove the # mark before the "print msg.reqId, msg.date," ... etc. This will, however, slow things down to some extent.
