#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 19:27:20 2020

@author: suryakantkumar
"""

'''
Problem : Given two integers m & n, calculate and return their multiplication using recursion. 
You can only use subtraction and addition for your calculation. No other operators are allowed.

Input format : m and n (in different lines)

Sample Input :
3 
5

Sample Output -
15

'''


def Multiplication(m, n):
    if m == 0 or n == 0:
        return 0
    
    if m == 1:
        return n
    
    if n == 1:
        return m
    
    return m + Multiplication(m, n-1)

m = int(input())
n = int(input())

result = Multiplication(m, n)
print(result)