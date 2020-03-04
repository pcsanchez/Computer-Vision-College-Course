from selenium import webdriver
import time
import os
from selenium.webdriver.common.keys import Keys

parentdir = "/home/pcsanchez/Desktop/"
generalDir = "Dogs"
path = os.path.join(parentdir, generalDir)

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver.get('http://www.unsplash.com/')
searchQuery = driver.find_element_by_name("searchKeyword")
searchQuery.clear()
searchQuery.send_keys("Dog")
searchQuery.send_keys(Keys.RETURN)
