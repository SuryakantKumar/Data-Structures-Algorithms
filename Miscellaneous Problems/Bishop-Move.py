#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:57:07 2020

@author: suryakantkumar
"""

'''
Find out number of positions on chess where bishop can attack.
Bishop position is given as (x, y) coordinates and chess dimension is n * n.
'''

def bishopMove(chess, position):
    count = 0
    x, y = position
    while x >= 1 and y >= 1:
        x = x - 1
        y = y - 1
        if x >= 1 and y >= 1:
            count += 1
        
    x, y = position
    while x <= n and y >= 1:
        x = x + 1
        y = y - 1
        if x <= n and y >= 1:
            count += 1
        
    x, y = position        
    while x >= 1 and y <= n:
        x = x - 1
        y = y + 1
        if x >= 1 and y  <= n:
            count += 1
        
    x, y = position
    while x <= n and y <= n:
        x = x + 1
        y = y + 1
        if x <= n and y <= n:
            count += 1
        
    return count

n = int(input())
x = int(input())
y = int(input())
position = (x, y)
chess = [[[i, j] for j in range(1, n+1) ]for i in range(1, n+1)]
result = bishopMove(chess, position)
print(result)