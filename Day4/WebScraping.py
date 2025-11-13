from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time

url = "https://webscraper.io/test-sites/e-commerce/ajax/computers/laptops"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
time.sleep(3)

products = driver.find_elements(By.CLASS_NAME, "thumbnail")

data = []
for product in products:
    titles = product.find_element(By.CLASS_NAME, "title").text
    prices = product.find_element(By.CLASS_NAME, "price").text
    link = product.find_element(By.CLASS_NAME, "title").get_attribute("href")

    print(f"{titles} - {prices} - {link}")
    data.append({"Title": titles,"Price": prices,"Link": link})

pd.DataFrame(data).to_csv("laptops.csv", index=False)
print("\n Scraping completed. Data saved to laptops.csv")
          

    
driver.quit()
