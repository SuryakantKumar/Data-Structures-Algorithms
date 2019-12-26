#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 06:50:59 2019

@author: suryakantkumar
"""

'''
Problem : Print the following pattern for the given number of rows.
Pattern for N = 7 is :
    
    1
   123
  12345
 1234567
  12345
   123
    1
    
'''


n = int(input())

n1 = (n//2) + 1

i = 1
while i <= n1:
    print((n1 - i)*' ', end = '')
    j = 1
    while j <= (2*i - 1):
        print(j, end = '')
        j += 1    
    print()
    i += 1
    
n2 = n1 - 1

i = n2
while i >= 1:
    print((n2-i+1)*' ', end = '')
    j = 1
    while j <= (2*i - 1):
        print(j, end = '')
        j += 1
    
    print()
    i -= 1