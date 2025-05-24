'''
Created on May 23, 2025

@author: yogs0
'''
'''
current_page_title = driver.title
print(current_page_title)

current_window = driver.current_window_handle
print(current_window)
# driver.switch_to.new_window('tab') # It opens new tab/ window
'''
window_handles_list = driver.window_handles
# print(window_handles_list)

driver.switch_to.window(window_handles_list[1])

'''
new_window = driver.current_window_handle
print(new_window)

new_page_title = driver.title
print(new_page_title)
'''
history_link = driver.find_element(By.XPATH, '//*[@id="toc-History"]/a/div/span[2]')
history_link.click()