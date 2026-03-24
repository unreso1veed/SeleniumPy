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

driver.find_element(By.XPATH, '//*[@id="nav730517295"]/div[1]/div[2]/button').click()
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="nav730517295"]/div[2]/div[2]/nav/ul/li[5]/a').click()
time.sleep(4)

print("\033[92mNav menu - Documentation button - Test passed\033[0m")

driver.quit()