#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 16:39:17 2020

@author: suryakantkumar
"""

'''
Print a ladder pattern for given corner point, height and width of each steps like:
for l = 5, h = 5, w = 4 pattern is :

                ****
                *  *
                *  *
                *  *
                *  *
            *****  *
            *      *
            *      *
            *      *
            *      *
        *****      *
        *          *
        *          *
        *          *
        *          *
    *****          *
    *              *
    *              *
    *              *
    *              *
*****              *
*                  *
*                  *
*                  *
*                  *
********************

'''

l = int(input())    # corner
h = int(input())    # height
w = int(input())    # width


row  = h * l
column = w * l

space = w - 2           # Inner space count

print((column - w)*' ', end = '')       # First row space
print(w*'*')                            # first row star

for i in range(1, row):
    if i % h == 0:                      # for row no of h, 2h, 3h...
        print((column - (i//h + 1)*w)*' ', end = '')        # Outer space
        
        print((w+1)*'*', end = '')
        
        print(space*' ', end = '')      # Inner space
        
        space += w                      # inner space increase after this point
        pass
    else:                               # For other rows than h, 2h, 3h
        print((column - (i//h + 1)*w)*' ', end = '')
              
        print('*', end = '')
        
        print(space*' ', end = '')      # Inner space
        
    print('*')
    
print(column*'*')           # Last row