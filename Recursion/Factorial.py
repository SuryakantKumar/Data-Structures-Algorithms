#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 09:55:01 2020

@author: suryakantkumar
"""

'''
Problem : Find Factorial of a number given as the input using recursion.

Input format : One integer x
Output Format : x! (i.e. factorial of x)

Sample Input 1 :
5

Sample Output 1 :
120

'''


def Factorial(n):
    if n == 0:                      # Base Case
        return 1
    
    smallOutput = Factorial(n-1)    # Induction Hypothesis
    return n * smallOutput          # Induction Step

n = int(input())
result = Factorial(n)
print(result)