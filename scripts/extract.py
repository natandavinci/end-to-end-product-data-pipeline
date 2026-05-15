import requests

URL = "https://dummyjson.com/products"

def extract_products():
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()

        products = data["products"]

        for product in products:
            print(
                f"Title: {product['title']} | "
                f"Price: ${product['price']} | "
                f"Category: {product['category']}"
            )
    else:
        print(f"Request failed: {response.status_code}")

if __name__=="__main__":
    extract_products()