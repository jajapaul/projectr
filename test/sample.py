from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get("http://127.0.0.1:8787")
assert "RStudio" in driver.title
elem = driver.find_element_by_name("username")
elem.clear()
elem.send_keys("admin")

elem = driver.find_element_by_name("password")
elem.clear()
elem.send_keys("password")

elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

import time 
time.sleep(10)


driver.close()
