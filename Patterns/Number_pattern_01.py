#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 15:59:01 2019

@author: suryakantkumar
"""
'''
Problem : Print the triangualar number pattern for n = 5:
    
                                1
                                11
                                121
                                1221
                                12221
'''

n = int(input())

if n > 0:
    print('1')                  # First row
    
i = 1
while i < n :
    j = 1
    print("1", end = '')        # print 1 at the beginning
    while j <= i - 1:
        print('2', end = '')    # print 2 in the middle
        j += 1
    print('1')                  # print 1 at the end and new line
    i += 1