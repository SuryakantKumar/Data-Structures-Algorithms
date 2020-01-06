#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 10:26:33 2020

@author: suryakantkumar
"""

'''
Problem : find nth fibonacci number of fibonacci series using recursion.
Fibonacci series : 1, 1, 2, 3, 5, 8, 13 .....

Sample Input 1 :
5

Sample Output 1 :
5

'''


def Fibonacci(n):
    if n == 1 or n == 2:            # Fibonacci series : 1,1,2,3,5,8,13...
        return 1
    
    return Fibonacci(n - 1) + Fibonacci(n - 2)

n = int(input())
result = Fibonacci(n)
print(result)
