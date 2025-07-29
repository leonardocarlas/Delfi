# Api Key 61YHHTT68FQMH7G1 vantage
# Finhub  d23k9u1r01qg1okjunu0d23k9u1r01qg1okjunug
# FMP dtAp78sCDVrcVk6oxLJd9B4u23Mv8BOu
import yfinance as yf
import pandas as pd
from art import text2art
from datetime import datetime
# from excel_io import create_excel_file, write_value_within_cell
from datetime import date


from data import get_earnings, get_goodwill_and_other_intangible_assets, get_market_cap, get_median_price, get_total_current_assets, get_total_current_liabilities, ultimi_3_anni_dividendi


def main():
    Logo = text2art("Delfi Program")
    print(Logo)
    while True:
        TICKER = input("Inserisci il ticker dell'azienda (es. ENI.MI): ").strip()
        if not TICKER:
            print("Ticker non valido. Riprova.")
            continue
        print(text2art(TICKER))
        data_str = date.today().strftime("%d-%m-%Y")
        FILE_NAME = f"{data_str}_{TICKER}"
        stock = yf.Ticker(TICKER)

        market_cap = get_market_cap(stock)
        total_current_assets = get_total_current_assets(stock)
        total_current_liabilities = get_total_current_liabilities(stock)
        goodwill = get_goodwill_and_other_intangible_assets(stock)

        print("\n--- DATI FINANZIARI ---")
        print(f"Goodwill: {goodwill}")
        print("Dividendi (2022–2025):")
        for dividend in ultimi_3_anni_dividendi(stock.dividends):
            print(dividend)

        print("\nEarnings:")
        print(get_earnings(stock))
        print("\nInformazioni generali:")
        print(stock)
        print("\nPrezzo mediano:")
        print(get_median_price(stock))

        print(f"\nCapitalizzazione di mercato per {TICKER}:")
        if isinstance(market_cap, (int, float)):
            print(f"${market_cap:,.2f}")
        else:
            print(market_cap[1])

        risposta = input("\nVuoi inserire un altro ticker? (s/n): ").lower()
        if risposta != 's':
            print("Uscita dall'applicazione.")
            break


if __name__ == "__main__":
    main()




