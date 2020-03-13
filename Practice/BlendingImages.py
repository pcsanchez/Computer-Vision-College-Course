import cv2
import numpy as np

# Reading images from memory, apply color correction if working with different color mappings
img1 = cv2.imread('../../../Desktop/Computer-Vision-with-Python/DATA/dog_backpack.png')
# img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.imread('../../../Desktop/Computer-Vision-with-Python/DATA/watermark_no_copy.png')
# img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

# In the case of these sample images, they have different sizes.
# img1 has a size of (1401, 934, 3)
# img2 has a size of (1280, 1277, 3)
print(img1.shape)
print(img2.shape)

# For this example I made both the images the same size to make the blending easier.
img1 = cv2.resize(img1,(1200,1200))
img2 = cv2.resize(img2,(1200,1200))

# addWeighted function only works when the images are the same size.
blended = cv2.addWeighted(src1=img1,alpha=0.8,src2=img2,beta=0.1, gamma=0)

while True:

    cv2.imshow('img1', img1)
    cv2.imshow('img2', img2)
    cv2.imshow('blended', blended)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

###############################################################################################

# Overlay small image on top of a larget image (No Blending)
# Numpy reassignment

# Reloading of pictures to start over
img1 = cv2.imread('../../../Desktop/Computer-Vision-with-Python/DATA/dog_backpack.png')
img2 = cv2.imread('../../../Desktop/Computer-Vision-with-Python/DATA/watermark_no_copy.png')

# Resizing img2 to be smaller
img2 = cv2.resize(img2, (600, 600))

# Changing names for better readability
large_img = img1
small_img = img2

# x and y offsets represent the markers of where to start and overlay the images
# In this case I started in the top left corner
x_offset = 0
y_offset = 0

# Ending points depend on the size of the smaller image
x_end = x_offset + small_img.shape[1]
y_end = y_offset + small_img.shape[0]

large_img[y_offset:y_end,x_offset:x_end] = small_img

# Blending together images of different sizes


while True:
    cv2.imshow('large_img', large_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
