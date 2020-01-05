#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 19:30:32 2020

@author: suryakantkumar
"""

'''
Problem : Given an integer n, count and return the number of zeros that are present in the given integer using recursion.

Input Format : Integer n

Output Format : No. of 0s

Sample Input :
10204

Sample Output
2

'''


def CountZero(n):
    if n == 0:
        return 0
    
    if n % 10 == 0:
        return 1 + CountZero(n // 10)
    else:
        return CountZero(n // 10)
    
n = int(input())

result = CountZero(n)
print(result)