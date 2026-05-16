from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time



def open_browser():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    driver.get("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

    time.sleep(3)

    #LOGIN - EMAIL
    email = driver.find_element(By.NAME, "email")
    email.click()
    email.send_keys("bottest@gmail.com")
    email.send_keys(Keys.RETURN)
    
    time.sleep(3)

    #LOGIN - PASSWORD
    password = driver.find_element(By.NAME, "password" )
    password.click()
    password.send_keys("123@#$456&abndBNM")
    password.send_keys(Keys.RETURN)

    time.sleep(1)
    
    tabela = pd.read_csv("data/products_automation.csv")

    time.sleep(3)

    for linha in tabela.index:

        codProdutc = driver.find_element(By.NAME, "codigo")
        codProdutc.click()
        codigo_product = tabela.loc[linha, "codigo_produto"]
        codProdutc.send_keys(codigo_product)
        

        time.sleep(2)

        marcProduct = driver.find_element(By.NAME, "marca")
        marcProduct.click()
        marca_product = tabela.loc[linha, "marca_produto"]
        marcProduct.send_keys(marca_product)
        

        time.sleep(2)
        typProduct = driver.find_element(By.NAME, "tipo")
        typProduct.click()
        type_product = tabela.loc[linha, "tipo_produto"]
        typProduct.send_keys(type_product)
        

        time.sleep(2)

        catProduct = driver.find_element(By.NAME, "categoria")
        catProduct.click()
        category_product = tabela.loc[linha, "categoria_produto"]
        catProduct.send_keys(category_product)
       

        time.sleep(2)

        pricProduct = driver.find_element(By.NAME, "preco_unitario")
        pricProduct.click()
        price_product = tabela.loc[linha, "preco_unitario"]
        pricProduct.send_keys(price_product)
        

        time.sleep(2)

        costProduct = driver.find_element(By.NAME, "custo")
        costProduct.click()
        costs_product = tabela.loc[linha, "custo_produto"]
        costProduct.send_keys(costs_product)

        time.sleep(2)

        obsProduct = driver.find_element(By.ID, "obs")

        obsProduct.clear()

        obsProduct.click()

        obsProduct.send_keys(Keys.CONTROL + "a")

        obsProduct.send_keys(Keys.DELETE)

        observations_product = tabela.loc[linha, "obs"]

        obsProduct.send_keys(str(observations_product))

        print(obsProduct.get_attribute("value"))
       
        time.sleep(2)

        submit_button = driver.find_element(By.ID, "pgtpy-botao")
        submit_button.click()


        
            
        

        time.sleep(2)



    input("Press ENTER to close browser...")

    driver.quit()


if __name__ == "__main__":
    open_browser()

