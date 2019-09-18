#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 01:41:50 2019

@author: suryakantkumar
"""
'''
Problem : Print Number pyramid Pattern for n = 6 as :
    
123456
 23456
  3456
   456
    56
     6
    56
   456
  3456
 23456
123456

'''

p = int(input())

q = p
for i in range(1, q+1):
    for spaces in range(i-1):
        print(' ', end = '')
    for no in range(i, q+1):
        print(no, end = '')
    print()
    
r = p-1
for i in range(1, r+1):
    for spaces in range(r-i):
        print(' ', end = '')
    for no in range(r-i+1, r+2):
        print(no, end = '')
    print()