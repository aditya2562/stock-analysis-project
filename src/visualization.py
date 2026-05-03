import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

def candlestick_with_volume_graph(df, ticker):

    df_stock = df[df["Ticker"] == ticker].copy()
    df_stock = df_stock.sort_values("Date")

    fig = make_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        row_heights=[0.7, 0.3],
        vertical_spacing=0.03
    )

    # ------ CANDLESTICK ------
    fig.add_trace(
        go.Candlestick(
            x = df_stock["Date"],
            open=df_stock["Open"],
            high=df_stock["High"],
            low=df_stock["Low"],
            close=df_stock["Close"],
            name="Price"
        ),
        row=1,
        col=1
    )

    # ------ VOLUME ------
    fig.add_trace(
        go.Bar(
            x=df_stock["Date"],
            y=df_stock["Volume"],
            name="Volume"
        ),
        row=2,
        col=1
    )

    # ------ LAYOUT ------
    fig.update_layout(
        template="plotly_white",
        title = f"{ticker} Price & Volume",
        xaxis_rangeslider_visible=False
    )

    fig.update_yaxes(showgrid=False, row=2, col=1)

    fig.write_html(f"data/{ticker}_candlestick.html")

    return fig

def normalised_prices_graph(df):

    pivot_df = df.pivot(index = "Date", columns = "Ticker", values = "Close")

    norm_df = (pivot_df / pivot_df.iloc[0]) * 100

    fig = go.Figure()

    for col in norm_df.columns:
        fig.add_trace(
            go.Scatter(
                x=norm_df.index,
                y=norm_df[col],
                mode="lines",
                name = col
            )
        )

    fig.update_layout(
        template = "plotly_white",
        title = "Normalized Price Comparison (Base = 100)",
        xaxis_title = "Date",
        yaxis_title = "Indexed Price"
    )

    fig.write_html("data/normalized_prices.html")

    return fig

def risk_return_graph(df):

    stats = df.groupby("Ticker")["Return"].agg(
        Mean_Return = "mean",
        Volatility = "std"
    )

    stats["Annual_Return"] = stats["Mean_Return"] * 252
    stats["Annual_Volatility"] = stats["Volatility"] * np.sqrt(252)

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=stats["Annual_Return"],
            y=stats["Annual_Volatility"],
            mode="markers+text",
            text=stats.index,
            textposition="top center",
            marker=dict(size=10)
        )
    )

    fig.update_layout(
        template="plotly_white",
        title = "Risk vs Return",
        xaxis_title = "Annualised Return",
        yaxis_title = "Volatility"
    )

    fig.update_xaxes(showgrid = False)
    fig.update_yaxes(showgrid = False)

    fig.write_html("data/risk_return_scatter.html")

    return fig 