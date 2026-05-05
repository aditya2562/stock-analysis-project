import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    
    df = pd.read_csv(file_path, parse_dates=["Date"])
    return df

def calculate_returns(df):
    
    df = df.sort_values(["Ticker", "Date"])

    df["Return"] = (df.groupby("Ticker")["Close"].pct_change().mul(100).round(2))

    return df

def compute_statistics(df):

    stats = df.groupby("Ticker")["Return"].agg(
        Mean_Return = 'mean',
        Std_Dev = 'std',
        Skewness = 'skew',
        Kurtosis = 'kurt'
    ).round(2)

    stats["Annualized_Volatility"] = (stats["Std_Dev"] * (252 ** 0.5)).round(2)

    stats["Sharpe_Ratio"] = (stats["Mean_Return"] / stats["Std_Dev"]).round(2)

    return stats

def analyze_result(stats):

    most_volatile = stats["Annualized_Volatility"].idxmax()

    best_sharpe = stats["Sharpe_Ratio"].idxmax()

    print("\n---Analysis---")

    print(f"Most Volatile Stock: {most_volatile}")

    print(f"Best Sharpe Ratio: {best_sharpe}")

def plot_volatility(stats):

    stats["Annualized_Volatility"].plot(kind="bar")

    plt.title("Annualized Volatility by Stocks")

    plt.xlabel("Ticker")

    plt.ylabel("Volatility")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig("data/volatility_chart.png")

    plt.show()

    plt.close()

def plot_sharpe_ratio(stats):

    stats["Sharpe_Ratio"].plot(kind="bar")

    plt.title("Sharpe Ratio by Stocks")

    plt.xlabel("Ticker")

    plt.ylabel("Sharpe Ratio")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig("data/sharpe_ratio_chart.png")

    plt.show()

    plt.close()

def calculate_indiacators(df):

    df = df.sort_values("Date")

    df["SMA_20"] = df["Close"].rolling(window=20).mean().round(2)
    df["SMA_50"] = df["Close"].rolling(window=50).mean().round(2)
    df["SMA_200"] = df["Close"].rolling(window=200).mean().round(2)

    delta = df["Close"].diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.ewm(com=13, adjust=False).mean()
    avg_loss = loss.ewm(com=13, adjust=False).mean()

    RS = avg_gain / avg_loss

    df["RSI"] = (100 - (100 / (1 + RS))).round(2)

    rolling_mean = df["Close"].rolling(window=20).mean()
    rolling_std = df["Close"].rolling(window=20).std()

    df["Bollinger_Bands_Upper"] = (rolling_mean + (2 * rolling_std)).round(2)
    df["Bollinger_Bands_Lower"] = (rolling_mean - (2 * rolling_std)).round(2)

    return df

def apply_indicator(df):

    df = (df.groupby("Ticker").apply(calculate_indiacators)).reset_index(level=0)

    return df

def validate_indicators(df):

    rsi_min = df["RSI"].min()
    rsi_max = df["RSI"].max()

    print("\n--- Indicator Validation ---")

    print(f"RSI Min: {rsi_min}")
    print(f"RSI Max: {rsi_max}")

    if rsi_min < 30:
        print("RSI is below 30, indicating oversold condition")
    if rsi_max > 70:
        print("RSI is above 70, indicating overbought condition")
    else:
        print("RSI is within normal range")

    return df

def calculate_correlation(df):

    pivot_df = df.pivot(index = "Date", columns = "Ticker", values = "Return")

    correlation_matrix = pivot_df.corr()

    return correlation_matrix

def plot_correlation_heatmap(correlation_matrix):

    plt.figure(figsize=(10,8))

    sns.heatmap(
        correlation_matrix, 
        annot=True, 
        fmt=".2f",
        cmap="coolwarm",
        linewidths=0.5
    )

    plt.title("Stocks Return Correlation Heatmap")

    plt.tight_layout()

    plt.savefig("data/correlation_heatmap.png")

    plt.show()

    plt.close()

def assign_sectors(df):

    sector_map = {
        "HDFCBANK.NS" : "Banking",
        "ICICIBANK.NS" : "Banking",
        "SBIN.NS" : "Banking",

        "TCS.NS": "IT",
        "INFY.NS": "IT",
        "WIPRO.NS": "IT",

        "RELIANCE.NS": "Energy",
        "NTPC.NS": "Energy"
    }

    df["Sector"] = df["Ticker"].map(sector_map)

    return df 

def compute_sector_metrics(df):
    
    sector_stats = df.groupby("Sector")["Return"].agg(
        Mean_Return = "mean",
        Volatility = "std"
    ).round(2)

    return sector_stats

def top_correlations(correlation_matrix, top = 3):

    correlation_unstack = correlation_matrix.unstack()

    correlation_unstack = correlation_unstack[correlation_unstack.index.get_level_values(0) != correlation_unstack.index.get_level_values(1)]

    correlation_unstack.index = correlation_unstack.index.map(lambda x: tuple(sorted(x)))

    corr_unique = correlation_unstack[~correlation_unstack.index.duplicated()]

    corr_sorted = corr_unique.sort_values(ascending=False)

    top_pairs = corr_sorted.head(top)

    return top_pairs
