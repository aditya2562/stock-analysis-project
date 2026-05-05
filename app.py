from src.data_loader import fetch_data, reshape_data
from src.quality_checks import audit_data, clean_data
from src.analysis import (
    load_data,
    calculate_returns,
    compute_statistics,
    plot_volatility,
    plot_sharpe_ratio,
    apply_indicator,
    calculate_correlation,
)
from src.visualization import (
    candlestick_with_volume_graph,
    normalised_prices_graph,
    risk_return_graph
)
from src.report import excel_report
from src.config import OUTPUT_FILE


def main():

    # 🔥 CONTROL FLAG
    FETCH_NEW_DATA = False   # Change to True for first run

    # -------------------------------
    # STEP 1: Data
    # -------------------------------

    if FETCH_NEW_DATA:
        raw = fetch_data()
        df = reshape_data(raw)

        audit_data(df)

        df = clean_data(df)

        df.to_csv(OUTPUT_FILE, index=False)

        print(f"\nClean data saved to: {OUTPUT_FILE}")

    else:
        df = load_data(OUTPUT_FILE)

    # -------------------------------
    # STEP 2: Returns + Stats
    # -------------------------------

    df = calculate_returns(df)
    stats_df = compute_statistics(df)

    plot_volatility(stats_df)
    plot_sharpe_ratio(stats_df)

    # -------------------------------
    # STEP 3: Indicators
    # -------------------------------

    df = apply_indicator(df)

    # -------------------------------
    # STEP 4: Correlation
    # -------------------------------

    corr_matrix = calculate_correlation(df).round(2)

    # -------------------------------
    # STEP 5: Visualizations
    # -------------------------------

    candlestick_with_volume_graph(df, ticker="HDFCBANK.NS")
    normalised_prices_graph(df)
    risk_return_graph(df)

    # -------------------------------
    # STEP 6: Excel Report
    # -------------------------------

    excel_report(df, stats_df, corr_matrix)


if __name__ == "__main__":
    main()