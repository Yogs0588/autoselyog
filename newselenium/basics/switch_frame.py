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

form_search_btn = driver.find_element(By.XPATH,'/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a')
form_search_btn.click()

'''#finding using partial link text
form_search_btn = driver.find_element(By.PARTIAL_LINK_TEXT,'Iframe with in an Iframe')
form_search_btn.click()'''


# Switch to outer frame nested iframe
driver.switch_to.frame(1)

# Switch to outer frame iframe demo
inner_frame=driver.find_element(By.XPATH,'/html/body/section/div/div/iframe')
driver.switch_to.frame(inner_frame)

form_search_txt = driver.find_element(By.XPATH,'/html/body/section/div/div/div/input')
form_search_txt.send_keys("yogs")
