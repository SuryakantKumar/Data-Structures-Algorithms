#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 06:44:53 2019

@author: suryakantkumar
"""

'''
Problem : Print the following pattern for the given number of rows.
Pattern for N = 5 is :

E
DE
CDE
BCDE
ABCDE

'''

n = int(input())

char = ord('A')
for i in range(1, n+1):
    for j in range(i, 0, -1):
        string = char + n - j
        print(chr(string), end = "")
    print()