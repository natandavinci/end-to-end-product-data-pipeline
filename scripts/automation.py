from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def open_browser():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    driver.get("https://dlp.hashtagtreinamentos.com/python/intensivao/tabela")

    input("Press ENTER to close browser...")

    driver.quit()


if __name__ == "__main__":
    open_browser()