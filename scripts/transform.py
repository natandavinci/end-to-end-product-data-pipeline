import pandas as pd

INPUT_CSV = "data/products.csv"
OUTPUT_CSV = "data/products_automation.csv"


def transform_products():
    df = pd.read_csv(INPUT_CSV)

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


if __name__ == "__main__":
    transform_products()