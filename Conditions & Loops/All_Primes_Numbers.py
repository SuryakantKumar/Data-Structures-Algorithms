#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 03:39:00 2019

@author: suryakantkumar
"""

'''
Problem : Print all prime numbers till given number N.

Sample Input 1 : 
15

Sample output 1 : 
2 3 5 7 11 13
'''

n = int(input('Enter Value of N : '))

k = 2
while k <= n:
    d = 2
    flag = False
    while d < k:
        if k % d == 0:
            flag = True
        d += 1
    if flag == False:
        print(k, end = ' ')
    k += 1
