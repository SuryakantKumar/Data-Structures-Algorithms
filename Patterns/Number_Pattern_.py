#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 04:34:06 2019

@author: suryakantkumar
"""

'''
Problem : Print the following pattern for the given N number of rows.

Pattern for N = 4 is :
    
1
11
202
3003

Input format : Integer N (Total no. of rows)
Output format : Pattern in N lines

Sample Input :
5

Sample Output :
1
11
202
3003
40004
'''

n = int(input())

print(1)

i = 1
while i <= n-1:
    print(i, end = '')
  
    j = 1
    while j <= i-1:
        print(0, end = '')
        j = j + 1
        
    print(i, end = '')
    print()
    i = i + 1
