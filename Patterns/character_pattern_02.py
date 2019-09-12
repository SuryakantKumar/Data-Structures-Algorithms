#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 15:19:57 2019

@author: suryakantkumar
"""

'''
Problem : Print the square character patter for n = 4:
    
                                    ABCD
                                    BCDE
                                    CDEF
                                    DEFG
'''

n = int(input())

i = 1

while i <= n:
    j = 1
    start_char = chr(ord('A') + i - 1)      # Each row starting character
    while j <= n:
        char = chr(ord(start_char) + j - 1)     # character to be printed in each row
        print(char, end = '')
        j += 1
    print()
    i += 1
