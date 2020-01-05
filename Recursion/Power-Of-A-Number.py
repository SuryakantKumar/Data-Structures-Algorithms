#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 10:10:07 2020

@author: suryakantkumar
"""

'''
Problem : Write a program to find x to the power n (i.e. x^n). Take x and n from the user. You need to print the answer.

Input format : Two integers x and n (separated by space)
Output Format : x^n (i.e. x raise to the power n)

Sample Input 1 :
3 4

Sample Output 1 :
81

Sample Input 2 :
2 5

Sample Output 2 :
32

'''


x, n = (int(x) for x in input().strip().split())

def Power(x, n):
    if n == 0:
        return 1
    
    if n == 1:
        return x
    
    smallOutput = Power(x, n-1)
    return x * smallOutput

result = Power(x, n)
print(result)