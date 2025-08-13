# Api Key 61YHHTT68FQMH7G1 vantage
# Finhub  d23k9u1r01qg1okjunu0d23k9u1r01qg1okjunug
# FMP dtAp78sCDVrcVk6oxLJd9B4u23Mv8BOu
from math import floor
from typing import List
import yfinance as yf
import pandas as pd
from art import text2art
from datetime import datetime
# from excel_io import create_excel_file, write_value_within_cell
from datetime import date


from data import get_earnings, get_goodwill_and_other_intangible_assets, get_market_cap, get_median_price, get_price_per_share, get_total_current_assets, get_total_current_liabilities, ultimi_3_anni_dividendi
from model import EarningPerYear, MediumPrice


def main():
    Logo = text2art("Delfi Program")
    print(Logo)
    while True:
        TICKER = input("Inserisci il ticker dell'azienda (es. ENI.MI): ").strip()
        if not TICKER:
            print("Ticker non valido. Riprova.")
            continue
        print(text2art(TICKER))

        stock = yf.Ticker(TICKER)

        market_cap = get_market_cap(stock)
        total_current_assets = get_total_current_assets(stock)
        total_current_liabilities = get_total_current_liabilities(stock)
        goodwill = get_goodwill_and_other_intangible_assets(stock)
        current_price = get_price_per_share(stock)
        number_of_shares = floor(market_cap / current_price)

        print("\n--- DATI FINANZIARI ---")
        print(f"\n Current Price: {current_price}")
        print(f"\n Market cap: {market_cap}")
        print(f"\n Number of shares: {number_of_shares}")
        # print(f"\n Goodwill And Other Intangible Assets: {goodwill}")
        print("\n Dividends: \n")
        for dividend in ultimi_3_anni_dividendi(stock.dividends):
            print(f"   2022  {dividend}")

        earnings: List[EarningPerYear] = get_earnings(stock)
        print("\n Earnings: \n")
        for earning in earnings:
            print(f"   Year {earning.year}:  {earning.earning}")

        print("\n Medium Prices: \n")
        medium_prices: List[MediumPrice] = get_median_price(stock)
        
        if len(medium_prices) != 0:
            for price in medium_prices:
                if price == None:
                    print("Price not available")
                else:
                    print(f"   Year {price.year}:  {price.price}")


        risposta = input("\nVuoi inserire un altro ticker? (s/n): ").lower()
        if risposta != 's':
            print("Uscita dall'applicazione.")
            break


if __name__ == "__main__":
    main()




