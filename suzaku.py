import os
import json
import time
import requests
import sqlite3
from os import path
import urllib.request
from operator import itemgetter
import pandas as pd
from settings import settings
from playsound import playsound


# Retrive previous results from databse
# Get 24 hour summary of all markets
# Loop through all markets and select BTC ones and ignore "ignore" coins
    # Check change from high and current
        # If change is > 10%, add the coin to current_results
# Add any new coins in the table and play sound
# Add new coins to the table
# Dont delete the old table


class Suzaku:

    def __init__(self):

        # Connect to Database
        self.conn = sqlite3.connect('suzaku.db')
        self.c = self.conn.cursor()

        # Clear Screen
        os.system('cls')

        # Previous Results
        self.previous_results_bittrex = self.get_previous_results()[0]
        self.previous_results_binance = self.get_previous_results()[1]
        print("\n\nPrevious Results (Bittrex):")
        print(sorted(self.previous_results_bittrex))
        print("\n\nPrevious Results (Binance):")
        print(sorted(self.previous_results_binance))
        print("\n\n")

        # Settings
        self.bittrex_ignore = settings["bittrex_ignore"]
        self.binance_ignore = settings["binance_ignore"]
        self.pct_change_threshold = settings["pct_change_threshold"]
        self.flush_db = settings["flush_db"]
        self.exchanges = settings["exchanges"]

        # Loop Markets
        self.current_results_bittrex = []
        self.current_results_binance = []
        if self.flush_db == True:
            self.refresh_table() # Refresh results table on new day
        else:
            self.loop_markets()

        self.c.close()
        self.conn.close()


    # Get Market Summaries
    def loop_markets(self):

        for exchange in self.exchanges:
            if exchange == "bittrex":
                try:
                    markets = requests.get('https://api.bittrex.com/api/v1.1/public/getmarketsummaries', timeout=5).json()["result"]
                except Exception as e:
                    print(e)
                else:
                    for market in markets:
                        market_name = market["MarketName"]
                        if market_name.startswith('BTC-'):
                            coin = market_name[4:]
                            if coin in self.bittrex_ignore:
                                continue
                            low = market["Low"]
                            high = market["High"]
                            prev = market["PrevDay"]
                            last = market["Last"]
                            try:
                                pct_change = 100 * (high - last) / last
                            except Exception as e:
                                print(coin, e)
                            else:
                                if last > prev:
                                    if pct_change > self.pct_change_threshold:
                                        self.current_results_bittrex.append(coin)

            elif exchange == "binance":
                try:
                    markets = requests.get('https://api.binance.com/api/v1/ticker/24hr', timeout=5).json()
                except Exception as e:
                    print(e)
                else:
                    for market in markets:
                        market_name = market["symbol"]
                        if market_name.endswith('BTC'):
                            coin = market_name[:-3]
                            if coin in self.binance_ignore:
                                continue
                            low = float(market["lowPrice"])
                            high = float(market["highPrice"])
                            prev = float(market["prevClosePrice"])
                            last = float(market["lastPrice"])
                            try:
                                pct_change = 100 * (high - last) / last
                            except Exception as e:
                                print(coin, e)
                            else:
                                if last > prev:
                                    if pct_change_1 > self.pct_change_threshold:
                                        self.current_results_binance.append(coin)
                                        print(coin, pct_change_1)


        # Handle any new results
        self.handle_new_results()


    # Handle New Results
    def handle_new_results(self):
        previous_results_bittrex_set = set(self.previous_results_bittrex)
        current_results_bittrex_set = set(self.current_results_bittrex)
        new_results_bittrex = list(current_results_bittrex_set - previous_results_bittrex_set)
        previous_results_binance_set = set(self.previous_results_binance)
        current_results_binance_set = set(self.current_results_binance)
        new_results_binance = list(current_results_binance_set - previous_results_binance_set)

        print("\n\nNew Results:")
        if len(new_results_bittrex) > 0 or len(new_results_binance) > 0:
            # Play sound if any new results
            playsound('more.mp3')
            # Bittrex New Results
            if len(new_results_bittrex) > 0:
                print("\n\nBittrex:")
                print(new_results_bittrex)
            # Binance New Results
            if len(new_results_binance) > 0:
                print("\n\nBinance:")
                print(new_results_binance)
                playsound('more.mp3')
        else:
            print("None.")

        # Add New results to the table
        for result in new_results_bittrex:
            params = (result,)
            self.c.execute("INSERT INTO bittrex_coins VALUES (?)", params)
        for result in new_results_binance:
            params = (result,)
            self.c.execute("INSERT INTO binance_coins VALUES (?)", params)
        self.conn.commit()

    # Get Previous Results
    def get_previous_results(self):
        bittrex_results = []
        binance_results = []
        self.c.execute('SELECT Coin FROM bittrex_coins')
        bittrex_items = self.c.fetchall()
        for item in bittrex_items:
            bittrex_results.append(item[0])
        self.c.execute('SELECT Coin FROM binance_coins')
        binance_items = self.c.fetchall()
        for item in binance_items:
            binance_results.append(item[0])
        return bittrex_results, binance_results


    # Used to ocationally refresh table
    def refresh_table(self):
        self.c.execute("DELETE FROM bittrex_coins") # Remove previous entries from table
        self.c.execute("DELETE FROM binance_coins") # Remove previous entries from table
        self.conn.commit()

if __name__ == '__main__':

    while True:
        i = Suzaku()
        print("\n\nRestarting in 2 minutes")
        time.sleep(120)
