# Python Book Recommender

This is a Python-based command-line tool that filters a large dataset of books based on user-defined criteria (pages, rating, and publication year) and outputs a list of highly-ranked recommendations. It utilizes the **Pandas** library for efficient data manipulation and filtering.

---

## Key Features

* **Flexible Filtering:** Users can set maximum page count, minimum average rating, and minimum publication year.
* **Optional Criteria:** Users can easily **skip** any filter by entering `0` (zero) when prompted.
* **Robust Data Cleaning:** Handles messy CSV data using `pd.to_numeric` with `errors='coerce'`, ensuring numerical comparisons are accurate.
* **Efficient Logic:** Uses **Boolean Indexing** to combine all user criteria into a single, highly efficient filter operation.
* **Smart Ranking:** Results are sorted primarily by **Average Rating** and secondarily by **Ratings Count** to prioritize popular and well-received books.

---

## Prerequisites

This project requires Python and the Pandas library.

1.  **Python 3**
2.  **Pandas:** Install via pip:
    ```bash
    pip install pandas
    ```

---

## Dataset

The script is designed to work with a file named `books.csv`. This file should contain book metadata, including the following required columns:

| Column Name | Type | Description |
| :--- | :--- | :--- |
| `title` | String | The book's title. |
| `authors` | String | The book's author(s). |
| `average_rating` | Numerical | The book's average community rating. |
| `num_pages` | Numerical | The book's page count. |
| `publication_date`| String | The original publication date (used to extract the year). |
| `ratings_count` | Numerical | The total number of ratings (used for popularity ranking). |

---

## How to Run the Script

1.  Save the provided Python code as `recommender.py`.
2.  Ensure the `books.csv` file is in the same directory as the script.
3.  Run the script from your terminal:

    ```bash
    python recommender.py
    ```

4.  Follow the prompts to enter your preferences:
    * **Page Length:** Enter the maximum number of pages.
    * **Rating:** Enter the minimum acceptable rating (enter `0` to skip).
    * **Year:** Enter the oldest acceptable publication year (enter `0` to skip).

---

## Output

Upon completion, the script will:

1.  Print a summary of the applied filters to the console.
2.  Display the **Top 10** ranked recommendations directly in the terminal.
3.  Save the **full list** of matching, sorted recommendations to a new file named `results.csv` in the same directory.

---

## Core Logic Explained

The script avoids repetitive filtering by building a single master mask:

1.  **Initialize Mask:** `final_mask = ~df["title"].isna()` creates a filter that initially selects every row.
2.  **Conditional Building:** If the user provides an input, the corresponding Boolean condition is generated and **combined** with the `final_mask` using the **AND operator (`&`)**:
    ```python
    final_mask = final_mask & rating_filter
    ```
3.  **Single Application:** After all criteria are evaluated, the entire DataFrame is filtered in one efficient step: `df = df[final_mask]`.
4.  **Sorting:** The resulting books are sorted by `average_rating` and `ratings_count` for optimal user experience.
