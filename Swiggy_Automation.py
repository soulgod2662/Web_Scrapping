
from selenium import webdriver
import time
from selenium.webdriver.common import desired_capabilities
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://swiggy.com')
locate_ME = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div/div[1]/div[1]/div/div[2]/div/div[2]')
locate_ME.click()
time.sleep(5)
search_ITEM = driver.find_element_by_xpath('//*[@id="root"]/div[1]/header/div/div/ul/li[5]/div/a/span[2]')
search_ITEM.click()
time.sleep(10)
search_restaurant_dish = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div/div/div/div/input')
search_restaurant_dish.send_keys('Burger King')
time.sleep(10)
select_resto_as_burger_king = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div/div/div/div[2]/div[1]/div[1]')
select_resto_as_burger_king.click()
time.sleep(10)
burger_king = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/a/div/div/div[2]/div[2]')
burger_king.click()
time.sleep(10)
select_Burger = driver.find_element_by_xpath('//*[@id="h-1950595611"]/div[2]/div[5]/div[1]/div/div[2]/div/div/div[1]')
select_Burger.click()
time.sleep(5)
checkout = driver.find_element_by_xpath('//*[@id="menu-content"]/div[2]/div/div[3]/div[3]')
checkout.click()
time.sleep(5)
Log_IN = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div/div[1]/div/div[1]/div[2]/div[2]/div[1]')
Log_IN.click()
time.sleep(10)
Phone_Number = driver.find_element_by_xpath('//*[@id="mobile"]')
Phone_Number.send_keys('') ## YOUR PHONE NUMBER IN HERE
time.sleep(10)
CLick_LOgin = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div/div[1]/div/div[1]/div[2]/div[2]/div/form/div[2]/a')
CLick_LOgin.click()
time.sleep(5)
otp_input = driver.find_element_by_xpath('//*[@id="otp"]')
otp_input.send_keys(input('OTP please'))  ## OTP will be sent to your mobile number
time.sleep(10)
verify_otp = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div/div[1]/div/div[1]/div[2]/div[2]/div/div[2]/form/div[2]/div[2]/a')
verify_otp.click()
time.sleep(10)
deliver_here = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div/div[2]/div[4]')
deliver_here.click()
