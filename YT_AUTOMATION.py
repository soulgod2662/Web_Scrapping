from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
print("This is a YouTube Automator")

webdrivere = webdriver.Chrome(ChromeDriverManager().install())
webdrivere.get("https://youtube.com")
searchbar = webdrivere.find_element_by_xpath('//*[@id="search"]')
searchbar.send_keys(input("Search in YouTube"))
searchbtn = webdrivere.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchbtn.click()
