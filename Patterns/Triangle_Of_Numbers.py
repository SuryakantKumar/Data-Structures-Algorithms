#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 06:53:08 2019

@author: suryakantkumar
"""

'''
Problem : Print the following pattern for the given number of rows.
Pattern for N = 5 is :
    
        1
      232
    34543
  4567654
567898765
   
'''


n = int(input())

i = 1
while i <= n:
    print((n-i)*' ', end = '')
    j = 1
    while j <= i:
        print(i+j-1, end = '')
        j += 1
    
    k = 2*(i-1)
    while k >= i:
        print(k, end = '')
        k -= 1
    
    print()
    i += 1