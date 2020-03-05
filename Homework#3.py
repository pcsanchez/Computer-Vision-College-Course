import os
from PIL import Image
import numpy as np
import requests
import cv2
from selenium import webdriver
from io import BytesIO

###############################
#### CONSTANT DECLARATIONS ####
###############################

searchTerm = input("Enter search term: \n")

PARENT_DIR = "/home/pcsanchez/Desktop/"
GENERAL_DIR = searchTerm + "/"
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

DRIVER.get('https://www.shutterstock.com/search/' + searchTerm)
# time.sleep(5)
IMGS = DRIVER.find_elements_by_css_selector('.z_h_a.z_h_b')

TOTAL_SIZE = len(IMGS)

os.chdir(TRAINING_PATH)
for i in range(int(TOTAL_SIZE*0.8)):
    response = requests.get(IMGS[i].get_attribute('src'))
    img = Image.open(BytesIO(response.content))
    imgarr = np.asarray(img)
    fixedimg = cv2.cvtColor(imgarr,cv2.COLOR_RGB2BGR)
    cv2.imwrite("train" + str(i) + ".jpg", fixedimg)
    print(IMGS[i].get_attribute('src'))

os.chdir(TESTING_PATH)
for i in range(int(TOTAL_SIZE*0.8),TOTAL_SIZE):
    response = requests.get(IMGS[i].get_attribute('src'))
    img = Image.open(BytesIO(response.content))
    imgarr = np.asarray(img)
    fixedimg = cv2.cvtColor(imgarr,cv2.COLOR_RGB2BGR)
    cv2.imwrite("test" + str(i-int(TOTAL_SIZE*0.8)) + ".jpg", fixedimg)
    print(IMGS[i].get_attribute('src'))
