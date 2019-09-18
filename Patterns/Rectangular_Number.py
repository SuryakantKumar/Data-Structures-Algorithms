#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 01:50:32 2019

@author: suryakantkumar
"""
'''
Problem : Print Rectangular number Pattern for n = 4 as :
    
4444444
4333334
4322234
4321234
4322234
4333334
4444444

'''
p = int(input())

q = p
for i in range(1, q+1):
    for j in range(q, q-i , -1):
        print(j, end = '')
    for k in range(2*q - 2*i):
        print(q-i+1, end = '')
    for l in range(q-i+2, q+1):
        print(l, end = '')
    print()
    
r = p - 1
for i in range(1, r+1):
    for j in range(r+1, i+1-1, -1):
        print(j, end = '')
    for k in range(2*i-1):
        print(i+1, end = '')
    for l in range(i+1, r+2):
        print(l, end = '')
    print()