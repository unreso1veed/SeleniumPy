import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_navigate_to_order_form():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        driver.get("https://sverh.tech")
        driver.maximize_window()
        
        driver.find_element(By.XPATH, '//*[@id="nav730517295"]/div[1]/div[2]/button').click()
        time.sleep(1)

        driver.find_element(By.XPATH, '//*[@id="nav730517295"]/div[2]/div[2]/nav/ul/li[3]/a').click()

        wait = WebDriverWait(driver, 10)
        
        order_popup_title = wait.until(EC.visibility_of_element_located((By.ID, "popuptitle_730967006")))

        #Test passed
        print("\033[92mNav menu - Order form button - Test passed\033[0m")

    finally:
        driver.quit()








