from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
chrome_driver_path = 'C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.maximize_window()
driver.get('https://google.com')
search_box = driver.find_element(By.XPATH,"//input[@class = 'gLFyf']")
search_box.send_keys("Real Madrid")
google_search_button = driver.find_element(By.XPATH,"//div[@class ='FPdoLc lJ9FBc']/center/input[@name ='btnK']")
google_search_button.click()
time.sleep(5)

#Retreiving the checkout text
checkout = driver.find_element(By.XPATH,"//div[@class = 'SPZz6b']")
checkout_text = checkout.text
actual_result = checkout.text
print(actual_result)
#Checking if the checkout text matches with the desired text.
expected_result = "रियल म्याड्रिड (Real Madrid CF)"
try:
    assert actual_result == expected_result
    result = "Title Matched"
except AssertionError:
    result = "Title don't match"
print(result)
driver.quit()
