import sqlite3
import pandas as pd

connection = sqlite3.connect("database/products.db")

query = """
SELECT *
FROM automation_products
LIMIT 10
"""

df = pd.read_sql_query(query, connection)

print(df)

connection.close()