from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://10.0.101.1:20080/#/login")

tenantcode_input = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div/div/form/div[1]/div/div/input')
tenantcode_input.send_keys("2028")
time.sleep(25)
username_input = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div/div/form/div[2]/div/div/input')
username_input.send_keys("002")
time.sleep(25)
password_input = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div/div/form/div[3]/div/div/input')
password_input.send_keys("123456")
time.sleep(25)
login_button = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div/div/form/div[5]/div/button')
login_button.click()

# driver.implicitly_wait(500)
time.sleep(30)
driver.quit()



