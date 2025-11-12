import pandas as pd

FILE = "books.csv"
df = pd.read_csv(FILE, on_bad_lines="skip")


# ---------- required columns -------------
# Keep only the necessary columns.
required_columns = [
    "title",
    "authors",
    "average_rating",
    "num_pages",
    "publication_date",
]
df = df[required_columns]

# Extract the year string, convert to numerical Int64, and drop the old column.
df["publication_year"] = pd.to_numeric(
    df["publication_date"].str.split("/").str[-1], errors="coerce"
).astype("Int64")
df = df.drop(columns=["publication_date"])

# Convert these columns to the correct numerical types, handling errors (coerce).
df["num_pages"] = pd.to_numeric(df["num_pages"], errors="coerce").astype("Int64")
df["average_rating"] = pd.to_numeric(df["average_rating"], errors="coerce").astype(
    float
)


# --------- user input -------------
# Page Length
book_Length = int(
    input("What is the maximum number of pages you want to read? (e.g., 500)?\n")
)
# Page Operator
less_greater = input(
    f"Less than or greater {book_Length} pages? (Tpye '>=' or '<=')\n"
).lower()

# Min Rating
rating_input = float(
    input(
        "What is the minimum average rating you'd accept? (e.g., 4.0)\nType '0' to pass.\n"
    )
)

# Min Year
year_input = int(
    input(
        "What is the **oldest** publication year you'd accept?\n(e.g., 2000 means you want books from 2000 or newer):\nType '0' to pass.\n"
    )
)


# ----------- logic -------------
final_mask = ~df["title"].isna()

if less_greater == ">=":
    page_filter = df["num_pages"] >= book_Length
    print(f"Filter 1: Books with >= {book_Length} pages.")
else:
    page_filter = df["num_pages"] <= book_Length
    print(f"Filter 1: Books with <= {book_Length} pages.")

final_mask = final_mask & page_filter

if rating_input == 0:
    print("Skipping rating filter.")
    pass
else:
    rating_filter = df["average_rating"] >= rating_input
    final_mask = final_mask & rating_filter


if year_input == 0:
    print("Skipping year filter.")
    pass
else:
    year_filter = df["publication_year"] >= year_input
    final_mask = final_mask & year_filter

df = df[final_mask]

# Sort the DataFrame: Primary sort by average_rating (highest first), secondary by ratings_count (highest first)
recommendations = df.sort_values(
    by=["average_rating", "publication_year", "num_pages"],
    ascending=[False, False, False],  # False means descending order (highest to lowest)
)


# Write the results to a new CSV file
recommendations.to_csv("results.csv", index=False)
print("Success! recommendations written to results.csv")
