from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input").send_keys("standard_user")
driver.find_element(By.XPATH, "//*[@id='password']").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
driver.close()
