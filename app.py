# from src.data_loader import fetch_data, reshape_data
# from src.quality_checks import audit_data, clean_data
from src.analysis import load_data, calculate_returns, compute_statistics, analyze_result, plot_volatility, plot_sharpe_ratio, apply_indicator, validate_indicators, calculate_correlation, plot_correlation_heatmap, assign_sectors, compute_sector_metrics, top_correlations
from src.visualization import candlestick_with_volume_graph, normalised_prices_graph, risk_return_graph
from src.report import excel_report
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

    # print("\n---- SUMMARY STATISTICS ----\n")
    stats = compute_statistics(df)
    # print(stats)

    # analyze_result(stats)

    # plot_volatility(stats)

    # plot_sharpe_ratio(stats)

    df = apply_indicator(df)

    # validate_indicators(df)

    # df.to_csv("data/indicators.csv", index = False)

    # print(f"\nIndicator data saved to: data/indicators.csv")

    correlation_matrix = calculate_correlation(df)
    corr_matrix = correlation_matrix.round(2)

    # plot_correlation_heatmap(correlation_matrix)

    # print("\n---CORRELATION MATRIX---")
    # print(correlation_matrix)

    # df = assign_sectors(df)

    # sector_stats = compute_sector_metrics(df)

    # print("\n---SECTOR SUMMARY---")
    # print(sector_stats)

    # top_corr = top_correlations(correlation_matrix)

    # print("\n---TOP CORRELATED PAIRS---")
    # print(top_corr.rename_axis(["Ticker_A", "Ticker_B"]).reset_index(name="Correlation"))

    # candlestick_with_volume_graph(df, ticker="HDFCBANK.NS")

    # normalised_prices_graph(df)

    # risk_return_graph(df)

    excel_report(df, stats, corr_matrix)

if __name__ == "__main__":
    main()