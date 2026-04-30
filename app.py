# from src.data_loader import fetch_data, reshape_data
# from src.quality_checks import audit_data, clean_data
from src.analysis import load_data, calculate_returns, compute_statistics, analyze_result, plot_volatility, plot_sharpe_ratio
from src.config import OUTPUT_FILE

def main():

    # Raw = fetch_data()

    # df = reshape_data(Raw)

    # audit_data(df)

    # clean_df = clean_data(df)

    # clean_df.to_csv(OUTPUT_FILE, index = False)

    # print(f"\nClean Data saved to: {OUTPUT_FILE}")

    # print("NaNs in Close:", clean_df["Close"].isnull().sum())

    # print("NaNs in Volume:", clean_df["Volume"].isnull().sum())

    df = load_data(OUTPUT_FILE)

    df = calculate_returns(df)

    stats = compute_statistics(df)

    print("\n---- SUMMARY STATISTICS ----\n")

    print(stats)

    analyze_result(stats)

    plot_volatility(stats)

    plot_sharpe_ratio(stats)
    

if __name__ == "__main__":
    main()