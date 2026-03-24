import requests
import selenium 
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://sverh.tech")

driver.find_element(By.XPATH, '//*[@id="rec704512955"]/div/div/div[8]/a').click()

time.sleep(4)
#Test passed
print("\033[92mDoc button - Test passed\033[0m")  

driver.quit()


