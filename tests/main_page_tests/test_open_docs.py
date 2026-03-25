import requests
import selenium 
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_open_docs():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        driver.get("https://sverh.tech")
        driver.maximize_window()

        driver.find_element(By.XPATH, '//*[@id="rec704512955"]/div/div/div[8]/a').click()
        wait = WebDriverWait(driver, 10)

        wait.until(EC.url_contains("https://docs.sverh.tech/"))

        #Test passed
        print("\033[92mDoc button - Test passed\033[0m") 

    finally:
        driver.quit() 












