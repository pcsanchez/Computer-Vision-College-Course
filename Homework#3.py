import os
import numpy as np
import requests
import cv2
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from io import BytesIO

###############################
#### CONSTANT DECLARATIONS ####
###############################

search_term = input("Enter search term: \n")

parent_dir = "/home/pcsanchez/Desktop/"
general_dir = search_term + "/"
training_dir = "training"
testing_dir = "testing"

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

path = os.path.join(parent_dir, general_dir)
training_path = os.path.join(path, training_dir)
testing_path = os.path.join(path, testing_dir)

############################
#### DIRECTORY CREATION ####
############################

try:
    os.mkdir(path)
except OSError:
    print('Creation of the directory %s failed' % path)
else:
    print('Succesfully created the directory %s' %path)

try:
    os.mkdir(training_path)
except OSError:
    print('Creation of the directory %s failed' %training_path)
else:
    print('Succesfully created the directory %s' %training_path)

try:
    os.mkdir(testing_path)
except OSError:
    print("Creation of the directory %s failed" %testing_path)
else:
    print("Succesfully created the directory %s" %testing_path)

###########################
#### IMAGE DOWNLOADING ####
###########################

driver.get('https://www.shutterstock.com/search/' + search_term)
aux = driver.find_element_by_class_name('b_ay_g').text
aux = aux.split()[1]
total_results = int(aux.replace(',', ''))

number_of_downloads = min(3000, total_results)
photos_downloaded = 0
train_index = 0
test_index = 0

while photos_downloaded < number_of_downloads:
    button_div = driver.find_element_by_class_name('z_b_g')
    button = button_div.find_element_by_tag_name('a')
    body = driver.find_element_by_tag_name('body')
    for x in range(20):
        body.send_keys(Keys.PAGE_DOWN)
    imgs = driver.find_elements_by_css_selector('img.z_h_a.z_h_b')
    photos_downloaded += len(imgs)

    os.chdir(training_path)
    for i in range(int(len(imgs)*0.8)):
        response = requests.get(imgs[i].get_attribute('src'))
        img = Image.open(BytesIO(response.content))
        imgarr = np.asarray(img)
        fixedimg = cv2.cvtColor(imgarr, cv2.COLOR_RGB2BGR)
        cv2.imwrite('train' + str(train_index) + '.jpg', fixedimg)
        train_index = train_index + 1
        print(imgs[i].get_attribute('src'))
    
    os.chdir(testing_path)
    for i in range(int(len(imgs)*0.8), len(imgs)):
        response = requests.get(imgs[i].get_attribute('src'))
        img = Image.open(BytesIO(response.content))
        imgarr = np.asarray(img)
        fixedimg = cv2.cvtColor(imgarr, cv2.COLOR_RGB2BGR)
        cv2.imwrite('test' + str(test_index) + '.jpg', fixedimg)
        test_index = test_index + 1
        print(imgs[i].get_attribute('src'))

    driver.get(button.get_attribute('href'))
