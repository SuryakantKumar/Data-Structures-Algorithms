#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 14:23:26 2020

@author: suryakantkumar
"""

'''
Given a matrix, area which is a village in which every element is a home. 
Some homes have value 1 and some are having 0. 1 means occupied home and 0 means home is vacant.
We need to find number of neighbourhood (i.e, occupied home) around the given position as your home.
'''

def neighbour(area, n, m, x, y):
    if x > n-1 or x < 0:
        return 0
    
    if y > m-1 or y < 0:
        return 0
        
    count = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i >= 0 and j >= 0 and i <= n-1 and j <= m-1:
                count += area[i][j]
    
    if area[x][y] == 0:
        return count
    else:
        return count - 1


area = [[0,1,1,0,0,0],
        [1,0,0,1,1,0],
        [0,0,0,0,0,0],
        [1,1,0,1,1,0],
        [1,0,1,0,0,0],
        [1,0,0,1,0,1],
        [0,1,0,0,0,0],
        [0,0,0,1,1,0]]

n = 8   # No of rows
m = 6   # No of columns
position = [5,2]
x = position[0]
y = position[1]

result = neighbour(area, n, m, x, y)
print(result)     