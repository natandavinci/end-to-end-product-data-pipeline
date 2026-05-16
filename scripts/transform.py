import pandas as pd
import sqlite3

INPUT_CSV = "data/products.csv"
OUTPUT_CSV = "data/products_automation.csv"


def transform_products():
    df = pd.read_csv(INPUT_CSV)

    # Cleaning the marca because some cases there is not data
    df["brand"] = df["brand"].fillna("No Brand")

    df_final = pd.DataFrame()

    df_final["codigo_produto"] = df["sku"]

    df_final["marca_produto"] = df["brand"]

    df_final["tipo_produto"] = df["category"]

    df_final["categoria_produto"] = df["category"]

    df_final["preco_unitario"] = df["price"]

    df_final["custo_produto"] = df["price"] * 0.7

    df_final["obs"] = df["description"]

    print(df_final.head())

    df_final.to_csv(OUTPUT_CSV, index=False)

    print("Automation dataset created successfully.")

    connection = sqlite3.connect("database/products.db")

    df_final.to_sql(
        "automation_products",
        connection,
        if_exists="replace",
        index=False
    )

    connection.close()

    print("Automation table created successfully.")

  


if __name__ == "__main__":
    transform_products()