#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 07:00:27 2019

@author: suryakantkumar
"""

'''
Problem : Print the following pattern for the given number of rows.
Pattern for N = 3 is :
    
1
23
4567

Input format : N (Total no. of rows)
Output format : Pattern in N lines

Sample Input :
5

Sample Output :
1
23 
4567
89123456
7891234567891234

'''


n = int(input())

val = 1
count = 1
for i in range(1, n+1):
    for j in range(1, count+1):
        if val <= 9:
            print(val, end = '')
            val += 1
        else:
            val = 1
            print(val, end = '')
            val += 1
    count *= 2
    print()