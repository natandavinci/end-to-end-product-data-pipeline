from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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




    input("Press ENTER to close browser...")

    driver.quit()


if __name__ == "__main__":
    open_browser()