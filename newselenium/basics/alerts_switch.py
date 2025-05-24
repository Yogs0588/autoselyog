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
alert_btn = driver.find_element(By.ID,'alertBtn')
alert_btn.click()
  
  

simple_alert=driver.switch_to.alert #switching to alert

simple_alert_text= simple_alert.text #printing the alert
print(simple_alert.text)
simple_alert.accept() # accepting the alert
