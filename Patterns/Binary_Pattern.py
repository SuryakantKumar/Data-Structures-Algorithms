#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 05:11:30 2019

@author: suryakantkumar
"""

'''
Problem : Print the following pattern for the given number of rows.
Pattern for N = 4 is :
    
1111
000
11
0

Input format : N (Total no. of rows)
Output format : Pattern in N lines

Sample Input :
5

Sample Output :
11111
0000
111
00
1

'''

n = int(input())

for i in range(1, n+1):
    for j in range (1, n-i+2):
        if(i%2 != 0):
            print("1", end = '')
        else:
            print("0", end = '')
    print()