
import pandas as pd
from pathlib import Path

# File paths
INPUT_FILE = Path("books.csv")
CLEAN_FILE = Path("books_cleaned.csv")
REPORT_FILE = Path("analysis_report.txt")


def clean_data(df):
    # Remove unnecessary spaces from text columns
    for column in ["title", "price", "availability"]:
        df[column] = df[column].astype("string").str.strip()

    # Remove rows without a title
    df = df.dropna(subset=["title"])
    df = df[df["title"] != ""]

    # Convert price from text to a numeric value
    df["price"] = pd.to_numeric(
        df["price"]
        .astype("string")
        .str.replace(r"[^\d.]", "", regex=True),
        errors="coerce"
    )

    # Remove duplicate records
    df = df.drop_duplicates(subset=["title"])

    # Standardize availability text
    df["availability"] = df["availability"].str.replace(
        r"\s+", " ", regex=True
    )

    # Reset row numbering
    return df.reset_index(drop=True)


def analyze_data(df):
    total_books = len(df)
    average_price = df["price"].mean()
    median_price = df["price"].median()
    minimum_price = df["price"].min()
    maximum_price = df["price"].max()
    missing_prices = df["price"].isna().sum()

    report = [
        "BOOK DATA ANALYSIS REPORT",
        "=" * 30,
        f"Total books after cleaning: {total_books}",
        f"Average price: £{average_price:.2f}" if pd.notna(average_price) else "Average price: N/A",
        f"Median price: £{median_price:.2f}" if pd.notna(median_price) else "Median price: N/A",
        f"Minimum price: £{minimum_price:.2f}" if pd.notna(minimum_price) else "Minimum price: N/A",
        f"Maximum price: £{maximum_price:.2f}" if pd.notna(maximum_price) else "Maximum price: N/A",
        f"Missing prices: {missing_prices}",
        "",
        "Availability counts:",
        df["availability"].value_counts(dropna=False).to_string()
    ]

    return "\n".join(report)


def main():
    if not INPUT_FILE.exists():
        print(f"Input file not found: {INPUT_FILE.resolve()}")
        return

    df = pd.read_csv(INPUT_FILE)

    required_columns = {"title", "price", "availability"}
    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        print(f"Missing required columns: {sorted(missing_columns)}")
        return

    print(f"Rows before cleaning: {len(df)}")

    cleaned_df = clean_data(df)

    print(f"Rows after cleaning: {len(cleaned_df)}")

    cleaned_df.to_csv(
        CLEAN_FILE,
        index=False,
        encoding="utf-8-sig"
    )

    report = analyze_data(cleaned_df)
    REPORT_FILE.write_text(report, encoding="utf-8")

    print("\n" + report)
    print(f"\nCleaned data saved to: {CLEAN_FILE.resolve()}")
    print(f"Analysis report saved to: {REPORT_FILE.resolve()}")


if __name__ == "__main__":
    main()
