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

RESPONSE = requests.get(
    "https://api.shutterstock.com/v2/oauth/authorize",
    params={"client_id": "dacc7-8c9b6-8c77f-9b788-e3f1c-6314c",
            "redirect_url": "http://localhost:3000/callback",
            "response_type": "code",
            "state": "Data set gathering",
            "scope": "licenses.create purchases.view licenses.view"})

print(RESPONSE.json())




# driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
# driver.get('http://www.unsplash.com/')
# searchQuery = driver.find_element_by_name("searchKeyword")
# searchQuery.clear()
# searchQuery.send_keys("Dog")
# searchQuery.send_keys(Keys.RETURN)
