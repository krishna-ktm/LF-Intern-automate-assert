
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
s = Service(ChromeDriverManager().install()) #install chromedriver during run time
driver = webdriver.Chrome(service=s) #pass chromedriver as a service
#driver=webdriver.Chrome(r'C:\Users\dell\PycharmProjects\automation\chromedriver.exe')
driver.get('https://merolagani.com/ContactUs.aspx')
full_name = driver.find_element(By.XPATH,"//input[@name ='ctl00$ContentPlaceHolder1$txtFullName']")
full_name.send_keys("Ram Bahadur")
mobile_num = driver.find_element(By.XPATH,"//input[@name ='ctl00$ContentPlaceHolder1$txtMobileNo']")
mobile_num.send_keys("981234567")
email = driver.find_element(By.XPATH,"//input[@name ='ctl00$ContentPlaceHolder1$txtEmail']")
email.send_keys("abc@gmail.com")
contact_us = driver.find_element(By.XPATH,"//div[@class ='panel-body text-center']")
contactus_text = contact_us.text
print(contactus_text)
m_area = driver.find_element(By.XPATH,"//textarea[@name ='ctl00$ContentPlaceHolder1$txtMessage']")
m_area.send_keys(contactus_text)
Sub_but = driver.find_element(By.XPATH,"//a[@id ='ctl00_ContentPlaceHolder1_lbtnSubmit']")
Sub_but.click()
time.sleep(20)