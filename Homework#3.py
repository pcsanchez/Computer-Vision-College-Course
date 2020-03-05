import time
import os
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

###############################
#### CONSTANT DECLARATIONS ####
###############################

PARENT_DIR = "/home/pcsanchez/Desktop/"
GENERAL_DIR = "Dogs/"
TRAINING_DIR = "training"
TESTING_DIR = "testing"

DRIVER = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

PATH = os.path.join(PARENT_DIR, GENERAL_DIR)
TRAINING_PATH = os.path.join(PATH, TRAINING_DIR)
TESTING_PATH = os.path.join(PATH, TESTING_DIR)

############################
#### DIRECTORY CREATION ####
############################

try:
    os.mkdir(PATH)
except OSError:
    print('Creation of the directory %s failed' % PATH)
else:
    print('Succesfully created the directory %s' %PATH)

try:
    os.mkdir(TRAINING_PATH)
except OSError:
    print('Creation of the directory %s failed' %TRAINING_PATH)
else:
    print('Succesfully created the directory %s' %TRAINING_PATH)

try:
    os.mkdir(TESTING_PATH)
except OSError:
    print("Creation of the directory %s failed" %TESTING_PATH)
else:
    print("Succesfully created the directory %s" %TESTING_PATH)

response = requests.get(
    "https://api.unsplash.com/search/photos?page=1&query=dog",
    headers={"Authorization": "Client-ID m7qC-55mLvNEs6GI0TkKiVJAtXoi2OvYJ7oLEuzGyq0"})

results = response.json()['results']


for i in range(len(results)):
    DRIVER.get(results[i]['links']['download'])
    ActionChains(DRIVER).key_down(Keys.CONTROL).send_keys('s').key_up(Keys.CONTROL).perform()



# driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
# driver.get('http://www.unsplash.com/')
# searchQuery = driver.find_element_by_name("searchKeyword")
# searchQuery.clear()
# searchQuery.send_keys("Dog")
# searchQuery.send_keys(Keys.RETURN)
