#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 19:25:02 2020

@author: suryakantkumar
"""

'''''
Write a recursive function that returns the sum of the digits of a given integer.

Sample Input :
12345

Sample Output :
15

'''''


n = int(input())

def SumOfDigits(n):
    if n == 0:
        return 0
    
    return (n%10) + SumOfDigits(n//10)

result = SumOfDigits(n)
print(result)