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

### DICTIONARY EXERCISES ###

alphabet = {
    1:'a',
    2:'b',
    3:'c',
    4:'d',
    5:'e'
}
print(alphabet)

print(4 in alphabet)
print(7 in alphabet)

print('a' in alphabet.values())
print('z' in alphabet.values())

alphabet[6]='f'
print(alphabet)

alphabet.pop(2)
print(alphabet)

dictNum = {
    'x':700,
    'y':56874,
    'z':990
}

print('Max:', max(dictNum.values()))
print('Min:', min(dictNum.values()))

### NUMPY EXERCISES ###

firstArray = np.arange(20)
print(firstArray)

secondArray = np.arange(30,40)
print(secondArray)

matrix = np.zeros((6,6))
print(matrix)

onesMatrix = np.ones((4,4))
print(onesMatrix)

sampleArray = np.array([[11,22,33],[44,55,66],[77,88,99]])
print(sampleArray)
print(sampleArray[:,2])

toReverse = np.arange(12,38)
print(toReverse)
print(np.flip(toReverse))

CwHwMat = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(CwHwMat[0:2,1:3])
print(CwHwMat[1:,2:])

X = CwHwMat[:,0:3]
y = CwHwMat[:,3]
print('X:',X)
print('Y:',y)

Test = X[0:1,:]
Train = X[1:,:]
print("Test:", Test)
print("Train:", Train)
