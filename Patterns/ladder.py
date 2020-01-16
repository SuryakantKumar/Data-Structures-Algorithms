#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 16:39:17 2020

@author: suryakantkumar
"""

l = int(input())    # corner
h = int(input())    # height
w = int(input())    # width


row  = h * l
column = w * l

space = w - 2
print((column - w)*' ', end = '')
print(w*'*')

for i in range(1, row):
    if i % h == 0:
        print((column - (i//h + 1)*w)*' ', end = '')
        
        print((w+1)*'*', end = '')
        
        print(space*' ', end = '')
        space += w
        pass
    else:
        print((column - (i//h + 1)*w)*' ', end = '')
              
        print('*', end = '')
        
        print(space*' ', end = '')
    print('*')
print(column*'*')