# Francisco Carlos Sanchez Ramirez
# A01196903
# B.S. Digital Systems and Robotics Engineering

import matplotlib.pyplot as plt
import numpy as np
import cv2
import os

TRAINING_DIRECTORY = '/home/pcsanchez/Desktop/train/'

objects = os.listdir(TRAINING_DIRECTORY)
quantities = []

for object in objects:
    quantities.append(len(os.listdir(TRAINING_DIRECTORY + object)))

fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.bar(objects, quantities)

plt.show()

###########################
#### DATA AUGMENTATION ####
###########################

img = cv2.imread(TRAINING_DIRECTORY + 'Dog/train0.jpg')
verticalFlip = cv2.flip(img.copy(), 0)
mirrorImg = cv2.flip(img.copy(), 1)

# Saving the augmented data
# cv2.imwrite('verticalFlip.jpg', vertical_flip)
# cv2.imwrite('mirrorImg.jpg', mirror_img)

new_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
new_img = cv2.resize(new_img,(300, 200))

# Es necesario dividir el data set en entranamiento y validacion ya que
# es necesario ver el comportamiento del modelo con datos que nunca ha visto antes.
# Esto para verificar su robustes.