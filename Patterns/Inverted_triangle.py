#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 18:01:37 2019

@author: suryakantkumar
"""
'''
Problem : Print Inverted triangle pattern of stars for n = 5:
    
*****
****
***
**
*

'''

n = int(input())

i = 1
while i <= n:
    j = 1
    while j <= n - i + 1:
        print('*', end = '')
        j += 1
    print()
    i += 1