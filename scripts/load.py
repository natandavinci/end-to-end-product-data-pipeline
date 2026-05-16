import sqlite3
import pandas as pd

DATABASE_PATH = "database/products.db"
CSV_PATH = "data/products.csv"


def load_products():
    df = pd.read_csv(CSV_PATH)

    connection = sqlite3.connect(DATABASE_PATH)

    df.to_sql(
        "products",
        connection,
        if_exists="replace",
        index=False
    )

    connection.close()

    print("Data loaded successfully into SQLite database.")


if __name__ == "__main__":
    load_products()