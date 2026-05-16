from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import sqlite3


def open_browser():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    driver.get("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

    time.sleep(1)

    #LOGIN - EMAIL
    email = driver.find_element(By.NAME, "email")
    email.click()
    email.send_keys("bottest@gmail.com")
    email.send_keys(Keys.RETURN)
    
    time.sleep(1)

    #LOGIN - PASSWORD
    password = driver.find_element(By.NAME, "password" )
    password.click()
    password.send_keys("123@#$456&abndBNM")
    password.send_keys(Keys.RETURN)

    time.sleep(1)
    
    connection = sqlite3.connect("database/products.db")

    query = """
    SELECT *
    FROM automation_products
    """

    tabela = pd.read_sql_query(query, connection)
    connection.close()

    print(tabela[["codigo_produto", "marca_produto"]].head(20))
    
    logs = []
    time.sleep(1)

    
    for linha in tabela.index:

        codigo_product = tabela.loc[linha, "codigo_produto"]

        try:
            codProdutc = driver.find_element(By.NAME, "codigo")
            codProdutc.click()
            codProdutc.send_keys(codigo_product)
            

            time.sleep(1)

            marcProduct = driver.find_element(By.NAME, "marca")
            marcProduct.click()
            marca_product = tabela.loc[linha, "marca_produto"]
            marcProduct.send_keys(marca_product)
            

            time.sleep(1)
            typProduct = driver.find_element(By.NAME, "tipo")
            typProduct.click()
            type_product = tabela.loc[linha, "tipo_produto"]
            typProduct.send_keys(type_product)
            

            time.sleep(1)

            catProduct = driver.find_element(By.NAME, "categoria")
            catProduct.click()
            category_product = tabela.loc[linha, "categoria_produto"]
            catProduct.send_keys(category_product)
        

            time.sleep(1)

            pricProduct = driver.find_element(By.NAME, "preco_unitario")
            pricProduct.click()
            price_product = tabela.loc[linha, "preco_unitario"]
            pricProduct.send_keys(price_product)
            

            time.sleep(1)

            costProduct = driver.find_element(By.NAME, "custo")
            costProduct.click()
            costs_product = tabela.loc[linha, "custo_produto"]
            costProduct.send_keys(costs_product)

            time.sleep(1)

            obsProduct = driver.find_element(By.ID, "obs")

            obsProduct.clear()

            obsProduct.click()

            obsProduct.send_keys(Keys.CONTROL + "a")

            obsProduct.send_keys(Keys.DELETE)

            observations_product = tabela.loc[linha, "obs"]

            obsProduct.send_keys(str(observations_product))

            print(obsProduct.get_attribute("value"))
        
            time.sleep(1)

            submit_button = driver.find_element(By.ID, "pgtpy-botao")
            submit_button.click()
            logs.append({
                "produto": codigo_product,
                "status": "success",
                "message": ""
            })
            

            time.sleep(1)

        except Exception as error:

             logs.append({
            "produto": codigo_product,
            "status": "error",
            "message": str(error)
         })

             continue
        

    df_logs = pd.DataFrame(logs)

    df_logs.to_csv(
        "data/automation_logs.csv",
        index=False
    )

    connection = sqlite3.connect("database/products.db")

    df_logs.to_sql(
        "automation_logs",
        connection,
        if_exists="append",
        index=False
    )

    connection.close()


if __name__ == "__main__":
    open_browser()

