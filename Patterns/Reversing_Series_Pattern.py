#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 06:47:39 2019

@author: suryakantkumar
"""

'''
Problem : Print the following pattern for the given number of rows.
Pattern for N = 5 is :
    
1 
3 2 
4 5 6 
10 9 8 7 
11 12 13 14 15

'''


n = int(input())

ele = 0
for i in range(1, n+1):
    if i % 2 != 0:
        ele = ele + i
        for j in range(1, i+1):
            print(ele, end = ' ')
            ele += 1
        print()
    else:
        ele = ele + i - 1
        for j in range(i, 0, -1):
            print(ele, end = ' ')
            ele -= 1
        print()