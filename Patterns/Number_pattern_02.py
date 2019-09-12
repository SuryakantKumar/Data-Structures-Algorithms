#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 16:14:43 2019

@author: suryakantkumar
"""
'''
Problem : Print triangular number pattern for n = 5:

                                    12345
                                    1234
                                    123
                                    12
                                    1
'''

n = int(input())

i = 1
while i <= n:
    j = 1
    while j <= n - i + 1:
        print(j, end = '')
        j += 1
    print()
    i += 1