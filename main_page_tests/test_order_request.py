import requests
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
driver.get("https://sverh.tech")

driver.find_element(By.XPATH,('//*[@id="rec730512253"]/div/div/div[6]/a')).click()
time.sleep(5)

#Test passed
print("\033[92mOrder button - Test passed\033[0m")  


driver.quit()