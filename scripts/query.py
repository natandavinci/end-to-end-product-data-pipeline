import sqlite3
import pandas as pd

DATABASE_PATH = "database/products.db"


def query_products():
    connection = sqlite3.connect(DATABASE_PATH)

    query = """
    SELECT
        id,
        title,
        price,
        category
    FROM products
    WHERE price > 100
    """

    df = pd.read_sql_query(query, connection)

    print(df)

    connection.close()


if __name__ == "__main__":
    query_products()