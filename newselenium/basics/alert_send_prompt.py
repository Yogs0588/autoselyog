'''
Created on May 23, 2025

@author: yogs0
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

'''1. Launching the chrome browser'''
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)

driver.get('https://testautomationpractice.blogspot.com/') # clicking on alert button
alert_btn = driver.find_element(By.ID,'promptBtn')
alert_btn.click()


simple_alert=driver.switch_to.alert #switching to alert

simple_alert_text= simple_alert.text # sending prompt

simple_alert.send_keys("yogs")

print(simple_alert.text)

simple_alert.accept()

# dynamic button
dynamic_btn = driver.find_element(By.NAME,'start')
dynamic_btn.click()
dynamic_btn = driver.find_element(By.NAME,'stop')
dynamic_btn.click()