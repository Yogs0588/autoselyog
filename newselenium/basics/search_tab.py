'''
Created on May 21, 2025

@author: yogs0
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
'''1. Launching the chrome browser'''
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)
# driver = Chrome()


'''2. Navigating to practice site'''
driver.get('https://testautomationpractice.blogspot.com/')

# search
search_txt_bx = driver.find_element(By.ID,'Wikipedia1_wikipedia-search-input')
search_txt_bx.send_keys('test')
search1_txt_bx = driver.find_element(By.CSS_SELECTOR,'#Wikipedia1_wikipedia-search-form > div > span.wikipedia-search-bar > span:nth-child(2) > input')
search1_txt_bx.click()

time.sleep(5)
search3_txt_bx = driver.find_element(By.CSS_SELECTOR,'#wikipedia-search-result-link > a')
search3_txt_bx.click()