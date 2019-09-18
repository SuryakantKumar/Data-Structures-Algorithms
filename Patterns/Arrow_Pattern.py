#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 01:34:26 2019

@author: suryakantkumar
"""
'''
Problem : Print Arrow Pattern for n = 7 as :

* 
 * * 
  * * * 
   * * * * 
  * * * 
 * * 
*

'''

p = int(input())

q = (p+1)//2
for i in range(1, q+1):
    for spaces in range(i-1):
        print(' ', end = '')
    for star in range(i):
        print('* ', end = '')
    print()

r = (p-1)//2 
for i in range(1, r+1):
    for spaces in range(r-i):
        print(' ', end = '')
    for star in range(r-i+1):
        print('* ', end = '')
    print()