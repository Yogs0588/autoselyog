'''
Created on May 24, 2025

@author: yogs0
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

'''1. Launching the chrome browser'''
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)

driver.get('https://demo.automationtesting.in/Frames.html') 

# switch to iframe
driver.switch_to.frame('singleframe')


form_search_btn = driver.find_element(By.XPATH, '/html/body/section/div/div/div/input')
form_search_btn.send_keys("yogs")

# switch to iframe within iframe by passing index

driver.switch_to.frame(14)