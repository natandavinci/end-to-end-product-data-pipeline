import requests
import pandas as pd

URL = "https://dummyjson.com/products"

def extract_products():
    response = requests.get(URL)

    if response.status_code == 200:

        data = response.json()

        products = data["products"]

        df = pd.DataFrame(products)[
    [
        "id",
        "title",
        "price",
        "category",
        "stock",
        "rating",
        "brand"
                     ]
                                    ]

        print(df.head())

        df.to_csv("data/products.csv", index=False)

    else:
        print(f"Request failed: {response.status_code}")

if __name__=="__main__":
    extract_products()