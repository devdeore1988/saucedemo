from asyncio import wait_for

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input").send_keys("standard_user")
driver.find_element(By.XPATH, "//*[@id='password']").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
driver.find_element(By.XPATH, "//*[@id='item_1_title_link']/div").click()
driver.find_element(By.XPATH, "//*[@id='add-to-cart']").click()
driver.back()
driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a").click()
# wait_for(timeout=3)
input("wait")
driver.close()