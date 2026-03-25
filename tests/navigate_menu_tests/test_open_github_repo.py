import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_navigate_to_github_repo():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        driver.get("https://sverh.tech")
        driver.maximize_window()

        driver.find_element(By.XPATH, '//*[@id="nav730517295"]/div[1]/div[2]/button').click()
        time.sleep(1)

        driver.find_element(By.XPATH, '//*[@id="nav730517295"]/div[2]/div[2]/nav/ul/li[4]/a').click()
        wait = WebDriverWait(driver, 10)

        wait.until(EC.url_contains("https://github.com/CopterExpress/clover"))


        #Test passed
        print("\033[92mNav menu - GitHub button - Test passed\033[0m")

    finally:
        driver.quit()