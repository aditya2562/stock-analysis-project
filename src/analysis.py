import pandas as pd
import matplotlib.pyplot as plt

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

    plt.close()

def plot_sharpe_ratio(stats):

    stats["Sharpe_Ratio"].plot(kind="bar")

    plt.title("Sharpe Ratio by Stocks")

    plt.xlabel("Ticker")

    plt.ylabel("Sharpe Ratio")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig("data/sharpe_ratio_chart.png")

    plt.close()