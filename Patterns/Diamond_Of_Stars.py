#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 01:50:20 2019

@author: suryakantkumar
"""
'''
Problem : Print Diamond of stars Pattern for n = 7 as :
    
   *
  ***
 *****
*******
 *****
  ***
   *
   
'''

p = int(input())

q = (p+1)//2
for i in range(1, q+1):
    for j in range(q-i):
        print(' ', end = '')
    for k in range(2*i - 1):
        print('*', end = '')
    print()

r = (p-1)//2 
for i in range(r, 0, -1):
    for j in range(r-i+1):
        print(' ', end = '')
    for k in range(2*i -1):
        print('*', end = '')
    print()