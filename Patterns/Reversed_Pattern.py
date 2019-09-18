#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 18:08:10 2019

@author: suryakantkumar
"""
'''
Problem : Print Reversed triangular star pattern for n = 4 as :
    
   *
  **
 ***
****

'''
n = int(input())

row = 1
while row <= n:
    space = 1
    while space <= n - row:
        print(' ', end = '')
        space += 1
    
    star = 1
    while star <= row:
        print('*', end = '')
        star += 1
    print()
    row += 1