
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("books_cleaned.csv")

# Ensure prices are numeric
df["price"] = pd.to_numeric(df["price"], errors="coerce")
df = df.dropna(subset=["price"])

if df.empty:
    raise ValueError("No valid prices available for visualization.")

# Chart 1: Distribution of book prices
plt.figure(figsize=(9, 5))
plt.hist(df["price"], bins=8, edgecolor="black")
plt.title("Distribution of Book Prices")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("price_distribution.png", dpi=150)
plt.show()

# Chart 2: Ten most expensive books
top_books = df.nlargest(10, "price").sort_values("price")

plt.figure(figsize=(10, 6))
plt.barh(top_books["title"], top_books["price"])
plt.title("Top 10 Most Expensive Books")
plt.xlabel("Price (£)")
plt.ylabel("Book")
plt.tight_layout()
plt.savefig("top_10_expensive_books.png", dpi=150)
plt.show()

print("Charts saved successfully.")
