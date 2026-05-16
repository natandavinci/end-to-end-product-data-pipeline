import sqlite3
import pandas as pd

connection = sqlite3.connect("database/products.db")

query = """
SELECT codigo_produto, marca_produto
FROM automation_products
"""

df = pd.read_sql_query(query, connection)

print(df)

connection.close()