'''
Created on May 18, 2025

@author: yogs0
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

'''1. Launching the chrome browser'''
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)
# driver = Chrome()

'''2. Navigating to practice site'''
driver.get('https://testautomationpractice.blogspot.com/')

'''3. Entering'''

name_txt_bx = driver.find_element(By.ID, 'name')
name_txt_bx.send_keys("yogs")
email_bx = driver.find_element(By.ID, 'email')
email_bx.send_keys("yogs0588@gamil.com")
phone_bx = driver.find_element(By.ID, 'phone')
phone_bx.send_keys("9630785316")
address_txt_bx = driver.find_element(By.ID, 'textarea')
address_txt_bx.send_keys("Vijayanagara 2nd stage")
gender_txt_bx = driver.find_element(By.ID, 'female')
gender_txt_bx.click()
days_txt_bx = driver.find_element(By.ID, 'wednesday')

days_txt_bx.click()
country_txt_bx = driver.find_element(By.ID, 'country')
country_txt_bx.click()
germany_txt_bx = driver.find_element(By.CSS_SELECTOR,'#country > option:nth-child(4)')
germany_txt_bx.click()

colors_txt_bx = driver.find_element(By.CSS_SELECTOR,'#colors > option:nth-child(3)')
colors_txt_bx.click()

SortedList_txt_bx = driver.find_element(By.CSS_SELECTOR,'#animals > option:nth-child(9)')
SortedList_txt_bx.click()



#date picker

datepicker1_txt_bx = driver.find_element(By.ID,'datepicker')
datepicker1_txt_bx.click()
datepicker1_txt_bx.send_keys('05/05/1988')
datepicker2_txt_bx = driver.find_element(By.NAME,'SelectedDate')
datepicker2_txt_bx.click()
datepicker2_txt_bx.send_keys('20/12/1990')


# search
search_txt_bx = driver.find_element(By.ID,'Wikipedia1_wikipedia-search-input')
search_txt_bx.send_keys('test')
search1_txt_bx = driver.find_element(By.CSS_SELECTOR,'#Wikipedia1_wikipedia-search-form > div > span.wikipedia-search-bar > span:nth-child(2) > input')
search1_txt_bx.click()
search3_txt_bx = driver.find_element(By.CSS_SELECTOR,'#wikipedia-search-result-link > a')
search3_txt_bx.click()



