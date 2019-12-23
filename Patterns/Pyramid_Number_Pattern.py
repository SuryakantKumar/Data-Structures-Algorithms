#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 04:58:46 2019

@author: suryakantkumar
"""

'''
Problem : Print the following pattern for the given number of rows.
Pattern for N = 4 is :
    
   1
  212
 32123
4321234

Input format : N (Total no. of rows)
Output format : Pattern in N lines

Sample Input :
5

Sample Output :
    1
   212
  32123
 4321234
543212345
'''

n = int(input())

i = 1
while i <= n:
    space = 1
    while space <= n-i:
        print(' ', end = '')
        space += 1
        
    p = i
    while p >= 1:
        print(p, end = '')
        p = p - 1
        
    p = 1
    while p <= i-1:
        print(p+1, end = '')
        p = p + 1
    print()
    i = i + 1