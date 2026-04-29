from src.data_loader import fetch_data, reshape_data
from src.quality_checks import audit_data, clean_data
from src.config import OUTPUT_FILE

def main():

    Raw = fetch_data()

    df = reshape_data(Raw)

    audit_data(df)

    clean_df = clean_data(df)

    clean_df.to_csv(OUTPUT_FILE, index = False)

    print(f"\nClean Data saved to: {OUTPUT_FILE}")

    print("NaNs in Close:", clean_df["Close"].isnull().sum())

    print("NaNs in Volume:", clean_df["Volume"].isnull().sum())

if __name__ == "__main__":
    main()