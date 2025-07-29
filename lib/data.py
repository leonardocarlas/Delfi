from datetime import datetime, timedelta
import yfinance as yf
import pandas as pd

# Function to fetch market cap
def get_market_cap(stock) -> str:
    try:
        info = stock.info
        market_cap = info.get("marketCap")
        if market_cap:
            return market_cap
        else:
            return None, "Market cap data unavailable"
    except Exception as e:
        return None, f"Error fetching market cap: {str(e)}"
   

def get_total_current_liabilities(stock) -> str:
    try:
        balance_sheet = stock.balance_sheet
        if not balance_sheet.empty:
            # Get the most recent annual balance sheet (first column)
            total_current_assets = balance_sheet.loc["Current Liabilities"].iloc[0]
            if total_current_assets is not None and not pd.isna(total_current_assets):
                return float(total_current_assets)
            else:
                return None, "Total Current Liabilities data unavailable"
        else:
            return None, "Balance sheet data unavailable"
    except Exception as e:
        return None, f"Error fetching total Current Liabilities: {str(e)}"

def get_total_current_assets(stock) -> str:
    try:
        balance_sheet = stock.balance_sheet
        if not balance_sheet.empty:
            # Get the most recent annual balance sheet (first column)
            total_current_liabilities = balance_sheet.loc["Current Assets"].iloc[0]
            if total_current_liabilities is not None and not pd.isna(total_current_liabilities):
                return float(total_current_liabilities)
            else:
                return None, "Total current assets data unavailable"
        else:
            return None, "Balance sheet data unavailable"
    except Exception as e:
        return None, f"Error fetching total current assets: {str(e)}"
    
    
def get_goodwill_and_other_intangible_assets(stock) -> str:
    try:
        balance_sheet = stock.balance_sheet
        if not balance_sheet.empty:
            # Get the most recent annual balance sheet (first column)
            goodwill = balance_sheet.loc["Goodwill And Other Intangible Assets"].iloc[0]
            if goodwill is not None and not pd.isna(goodwill):
                return float(goodwill)
            else:
                return None, "Total Goodwill And Other Intangible Assets data unavailable"
        else:
            return None, "Balance sheet data unavailable"
    except Exception as e:
        return None, f"Error fetching total Goodwill And Other Intangible Assets: {str(e)}"
    

def ultimi_3_anni_dividendi(dividends_series):
    """
    Prende una Series con indici datetime e valori di dividendi.
    Restituisce una lista con la somma dei dividendi per ciascuno degli ultimi 3 anni.
    """
    # Ottieni l'anno corrente
    anno_corrente = datetime.now().year
    
    # Crea un DataFrame temporaneo con anno e dividendo
    df = dividends_series.copy().to_frame(name='Dividendo')
    df['Anno'] = df.index.year
    
    # Filtro per gli ultimi 3 anni
    ultimi_anni = list(range(anno_corrente - 2, anno_corrente + 1))
    df_filtrato = df[df['Anno'].isin(ultimi_anni)]
    
    # Raggruppa e somma per anno
    somma_annua = df_filtrato.groupby('Anno')['Dividendo'].sum()
    
    # Crea lista ordinata per anno
    return [somma_annua.get(anno, 0.0) for anno in ultimi_anni]



# Function to fetch earnings for the last 10 years
def get_earnings(stock):
    earnings_data = []
    # Fetch net income from financials
    financials = stock.financials
    if not financials.empty:
        net_income_row = financials.loc["Net Income"] if "Net Income" in financials.index else None
        if net_income_row is not None:
            for date in financials.columns:
                year = date.year
                net_income = net_income_row[date]
                # Update or add entry for the year
                for entry in earnings_data:
                    if entry["Fiscal Year"] == year:
                        entry["Net Income"] = float(net_income) if pd.notna(net_income) else None
                        break
                else:
                    earnings_data.append({
                        "Fiscal Year": year,
                        "EPS": None,
                        "Net Income": float(net_income) if pd.notna(net_income) else None
                    })
    print(earnings_data)    
     


def get_median_price(stock, years: int = 3) -> str:
    try:
        # Calculate date range
        end_date = datetime.now()
        start_date = end_date - timedelta(days=years * 365)
        # Fetch historical data
        history = stock.history(start=start_date, end=end_date, interval="1d")
        
        if not history.empty:
            # Extract closing prices and add year column
            history["Year"] = history.index.year
            # Group by year and calculate median
            yearly_medians = []
            for year in range(end_date.year - years + 1, end_date.year + 1):
                year_prices = history[history["Year"] == year]["Close"].dropna()
                if not year_prices.empty:
                    yearly_medians.append({
                        "Year": year,
                        "Median Closing Price": float(year_prices.median())
                    })
                else:
                    yearly_medians.append({
                        "Year": year,
                        "Median Closing Price": None
                    })  # Include None for years with no data
            if any(item["Median Closing Price"] is not None for item in yearly_medians):
                return yearly_medians
            else:
                return None, "No valid closing price data available for any year"
        else:
            return None, "Historical price data unavailable"
    except Exception as e:
        return None, f"Error fetching median price: {str(e)}"
