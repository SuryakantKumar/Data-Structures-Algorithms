#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 14:24:25 2020

@author: suryakantkumar
"""

'''
Problem : Rotate only outer rows or columns of given matrix li, n number of times.
where n is number of rotation.
'''

def MatrixOuterRotation(li, n):
    for i in range(n % 4):
        l = []
        for i in range(len(li)):
            l.append(li[i][0])
        
        for j in range(len(li)):        # Restoring first column
            li[j][0] = li[len(li)-1][j] 
            
        for k in range(len(li)):        # Restoring last row
            li[len(li)-1][k] = li[len(li)-k-1][len(li)-1]
            
        for m in range(len(li)-1):        # Restoring last column
            li[m][len(li)-1] = li[0][m]
            
        for p in range(len(li)):        # Restoring first row
            li[0][p] = l[len(l) -p -1]
    return
    
li = [[1, 2, 3, 4, 5, 6],
      [20, 0, 0, 0, 0, 7],
      [19, 0, 0, 0, 0, 8],
      [18, 0, 0, 0, 0, 9],
      [17, 0, 0, 0, 0, 10],
      [16, 15, 14, 13, 12, 11]]

n = int(input())
MatrixOuterRotation(li, n)
for e in li:
    print(*e)