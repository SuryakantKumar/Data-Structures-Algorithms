#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 06:58:36 2019

@author: suryakantkumar
"""

'''
Problem : Print the following pattern for the given number of rows.
Pattern for N = 3 (No. of rows = 5, No. of columns = 5)

1   1
 2 2
  3
 2 2
1   1

Input format : Integer N (Total no. of rows)
Output format : Pattern in N lines

Sample Input :
5

Sample Output : No. of rows = 9, No. of columns = 9

1       1
 2     2
  3   3
   4 4
    5
   4 4
  3   3
 2     2
1       1

'''


n = int(input())

i = 1
while i <= n:
    print((i-1)*' ', end = '')
    j = 1
    while j <= n:
        if i == j:
            print(i, end = '')
        j += 1
    
    print((2*(n-i)-1)*' ', end= '')
    
    k = n-1
    while k >= 1:
        if i == k:
            print(i, end = '')
        k -= 1
        
    print((i-1)*' ', end = '')
    
    print()
    i += 1
    
n2 = n - 1

i = n2
while i >=1:
    
    print((i-1)*' ', end = '')
    
    j = 1
    while j <= n2:
        if i == j:
            print(i, end = '')
        j += 1
    
    print((2*(n2-i)+1)*' ', end= '')
    
    k = n2
    while k >= 1:
        if i == k:
            print(i, end = '')
        k -= 1
        
    print((i-1)*' ', end = '')
    
    print()
    i -= 1