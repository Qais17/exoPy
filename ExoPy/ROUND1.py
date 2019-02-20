# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 09:33:07 2018

@author: Dell
"""

#Exercice 1

import numpy as np

#Exercice 2 

print(np.__version__)
print(np.__config__.show())

#Exercice 3

x = np.zeros(10)
print(x)

#Exercice 4

a = np.array([1,2,3])

print(a.nbytes)

#Exercice 5

np.info(np.add)

#python -c 'import numpy as np;  np.info(np.add)'

#Exercice 6

new_mat=np.zeros((10),dtype=int)
new_mat[4]=1

#Exercice 7
print(np.arange(10, 50))

#Exercice 8

A[::-1]

#Exercice 9

a=np.arange(9).reshape(3,3)
print(a)

#Exercice 10

A = [1,2,0,0,4,0]
B = np.argwhere(A)
print (B)

#Exercice 11

a = np.eye(3)

#Exercice 12

a = np.random.random((3, 3, 3))

#Exercice 13

t = np.random.random((10, 10))
print (t.min(), t.max())

#Exercice 14

v = np.random.random((1, 30))

#Exercice 15

b = np.zeros((8,8))

x = 0
while (x < 8):
    y = 0
    while (y < 8):
        if (x == 7 or x == 0 or y == 0 or y == 7):
            b[x][y] = 1
        y += 1
    pass
    x += 1
pass

print (b)