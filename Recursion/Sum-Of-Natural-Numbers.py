#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 10:04:44 2020

@author: suryakantkumar
"""

'''
Problem : Find sum of n natural numbers using recursion.

Input format : One integer n
Output Format: ∑n (i.e, Sum of n natural numbers)

Sample Input 1 :
5

Sample Output 1 :
15

'''


def Sum(n):
    if n == 1:
        return 1
    
    smallSum = Sum(n-1)
    return smallSum + n
    
n = int(input())
result = Sum(n)
print(result)