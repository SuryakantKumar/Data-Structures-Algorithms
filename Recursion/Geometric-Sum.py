#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 18:59:42 2020

@author: suryakantkumar
"""

'''
Problem : Given k, find the geometric sum i.e. 1 + 1/2 + 1/4 + 1/8 + ... + 1/(2^k) using recursion. Return the answer.

Sample Input :
3

Sample Output :
1.875

'''


k = int(input())

def GeometricSum(k):
    if k == 0:
        return 1
    
    return 1/(2**k) + GeometricSum(k-1)

result = GeometricSum(k)
print("%.3f" %result)