from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

for i in range(2):

    driver.get("https://tees.co.id/")

    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div')))
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]').click()

    except TimeoutException:
        print("kedua kali")
        pass
    
