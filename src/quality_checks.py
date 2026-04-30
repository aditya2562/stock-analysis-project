import pandas as pd


def audit_data(df):

    print("\n--- Missing Values ---")
    print(df.isnull().sum())

    print("\nDuplicate Rows:", df.duplicated().sum())

    zero_volume = (df["Volume"] == 0).sum()
    print(f"\nZero volume rows: {zero_volume}")

def flag_gaps(df):

    df = df.sort_values(["Ticker","Date"])

    df["Gap_Days"] = (df.groupby("Ticker")["Date"].diff().dt.days)

    df["Gap_Flag"] = df["Gap_Days"] > 3

    return df

def clean_data(df):

    initial_rows = len(df)

    missing_pct = (df.isnull().mean().mul(100).round(2))

    df[["Open","High","Low","Close", "Adj Close"]] = (df[["Open","High","Low","Close","Adj Close"]]).round(2)

    df[["Open","High","Low","Close"]] = (df[["Open","High","Low","Close"]].ffill())

    df = df[df["Volume"] > 0]

    dropped_rows = initial_rows - len(df)

    df = flag_gaps(df)

    print("\n=== DATA QUALITY REPORT ===\n")
    print(f"Rows fetched: {initial_rows}")
    print(f"Rows dropped: {dropped_rows}\n")
    print("Percent Missing Per Column:\n")
    print(missing_pct)

    return df
