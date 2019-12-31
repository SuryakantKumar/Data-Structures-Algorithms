#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 14:38:38 2019

@author: suryakantkumar
"""

'''
Problem : Print the square character pattern for n = 5:

ABCDE
ABCDE
ABCDE
ABCDE
ABCDE

'''
n = int(input())                        # User Input

i = 1
while i <= n:                           # loop for rows
    j = 1
    while j <= n:                       # loop for columns
        char = chr(ord('A') + j - 1)    # character to be printed
        print(char, end = '')
        j += 1
    print()                             # New line after each row
    i += 1
