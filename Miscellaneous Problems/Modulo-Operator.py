#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 15:44:48 2020

@author: suryakantkumar
"""

def modulous(m, n):
    if n == 0:
        return -1
    
    elif m == n:
        return 0
    
    elif m < n:
        return m
    
    else:
        sum = n
        original = sum    
        while sum < m:
            sum += n
            if sum < m:
                original = sum
                
        return m - original

m = int(input())
n = int(input())
result = modulous(m, n)
print(result)