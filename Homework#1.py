import numpy as np
import cv2

#### LIST EXERCISES ####
colors = ['blue','white','green','red','pink','yellow']
print(len(colors))
print('blue' in colors)
print('purple' in colors)

try:
    print(colors.index('white'))
except:
    print('Value not in list')

try:
    print(colors.index('black'))
except:
    print('Value not in list')

colors.extend(['violet','gray'])
print(colors)

colors.append(['brown','black'])
print(colors)

colors[0:3] = ['cyan']
print(colors)

colors[len(colors)-1].append('orange')
print(colors)

del colors[2:]
print(colors)

matrix = [[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24]]
print(matrix)

lists = [[1,2],[3,4],[5,6],[7,8,9]]
print(len(lists[len(lists)-1]))

odds = []
for i in range(1,10,2):
    odds.append(i*i)
print(odds)

threeTable = []
for i in range(1,11):
    threeTable.append([3,i,3*i])
print(threeTable)

array3D = []

for i in range(4):
    array3D.append([])
    for j in range(3):
        array3D[i].append([])
        for k in range(2):
            array3D[i][j].append('?')
print(array3D)

#### DICTIONARY EXERCISES ####

alphabet = {(1,'a'),(2,'b')}
print(alphabet)