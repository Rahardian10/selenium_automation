from selenium import webdriver
from selenium.webdriver.common.by import By
# import time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

driver.implicitly_wait(5)
driver.get("https://demoqa.com/alerts")

#driver.maximize_window()
#driver.minimize_window()
driver.find_element(By.ID, "promtButton").click()
# driver.switch_to.alert.dismiss()
driver.switch_to.alert.send_keys("sedang mencoba")
driver.switch_to.alert.accept()

