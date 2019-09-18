#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 18:20:37 2019

@author: suryakantkumar
"""
'''
Problem : Print Isosceles Pattern of numbers for n = 5 as : 
    
    1
   121
  12321
 1234321
123454321

'''
n = int(input())

row = 1
while row <= n:
    space = 1
    while space <= n - row:             # Spaces
        print(' ', end = '')
        space += 1
    
    incr = 1
    while incr <= row:                  # Increasing Pattern
        print(incr, end = '' )
        incr += 1
    
    decr = row - 1
    while decr >= 1:                    # Decreasing Pattern
        print(decr, end = '')
        decr -= 1
    print()
    row += 1