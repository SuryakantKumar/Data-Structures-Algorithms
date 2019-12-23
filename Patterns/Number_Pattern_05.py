#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 01:28:00 2019

@author: suryakantkumar
"""
'''
Problem : Print Number Pattern for n = 5 as : 
    
1        1
12      21
123    321
1234  4321
1234554321

'''

n = int(input())

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end = '')
    for k in range(2*n - 2*i):
        print(' ', end = '')
    for l in range(i, 0, -1):
        print(l, end = '')
    print()
