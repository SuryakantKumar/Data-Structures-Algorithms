#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 05:08:40 2019

@author: suryakantkumar
"""

'''
Problem : Print the following pattern for the given number of rows.
Pattern for N = 4 is :
    
****
****
****
****

'''

n = int(input())

i = 1
while i <= n:
    j = 1
    while j <= n:
        print('*', end = '')
        j += 1
    print()
    i += 1