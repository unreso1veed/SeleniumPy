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

def test_opening_navigation_menu():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        driver.get("https://sverh.tech")
        driver.maximize_window()

        driver.find_element(By.XPATH, '//*[@id="nav730517295"]/div[1]/div[2]/button').click()
        wait = WebDriverWait(driver, 10)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="nav730517295"]/div[2]/div[2]')))


        #Test passed
        print("\033[92mNavigation menu - Test passed\033[0m")
    
    finally:
        driver.quit()







