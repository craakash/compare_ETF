import yfinance as yf
import matplotlib.pyplot as plt

# Define ETFs to compare

# Update the ETF list to include 5 more popular ETFs
etfs = {
    "SPY": "S&P 500 ETF (SPY)",                  # Broad US Market
    "VWO": "Emerging Markets ETF (VWO)",         # Developing World
    "XLE": "Energy Select Sector ETF (XLE)",     # Oil and Energy Industry
    "XLK": "Technology Select Sector ETF (XLK)", # Technology Industry
    "ARKK": "ARK Innovation ETF (ARKK)",         # Innovation and Disruptive Tech
    "IEMG": "iShares Core MSCI Emerging Markets (IEMG)", # Emerging Markets
    "QQQ": "Invesco QQQ ETF (QQQ)",              # NASDAQ-100
    "VNQ": "Vanguard Real Estate ETF (VNQ)",     # Real Estate
    "XLF": "Financial Select Sector ETF (XLF)"   # Financials
}

# Attempt to fetch the historical adjusted close prices for all ETFs
try:
    # Download historical data
    prices = yf.download(list(etfs.keys()), start=start_date, end=end_date)['Adj Close']

    # Normalize prices for comparison (base = 100)
    normalized_prices = prices / prices.iloc[0] * 100

    # Plot
    plt.figure(figsize=(14, 8))
    for ticker, label in etfs.items():
        plt.plot(normalized_prices[ticker], label=label)

    # Add labels, title, and legend
    plt.title("Performance of SPY vs Popular ETFs (2019-2024)", fontsize=16)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Normalized Price (Base = 100)", fontsize=12)
    plt.legend(fontsize=10)
    plt.grid(alpha=0.3)
    plt.show()
except Exception as e:
    print("An error occurred:", e)
