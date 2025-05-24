'''
Created on May 14, 2025

@author: yogs0
'''
'''# from selenium import webdriver

from selenium.webdriver import Chrome, Edge

# driver = webdriver.Chrome()
driver = Edge()
driver.get('https://selenium.dev/')'''

# TO Launch chrome

from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)
driver.get('https://selenium.dev/')



