#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 16:32:08 2019

@author: suryakantkumar
"""
'''
Problem : Print triangualar chaarcter pattern for n = 5:
    
A
BB
CCC
DDDD
EEEEE

'''
n = int(input())

i = 1 
while i <= n:
    j = 1
    while j <= i:
        char = chr(ord('A') + i - 1)    # Same chaaracter in every row
        print(char, end = '')
        j += 1
    print()
    i += 1
