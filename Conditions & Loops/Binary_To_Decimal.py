#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 07:13:51 2019

@author: suryakantkumar
"""

'''
Problem : Given a binary number as an integer N, convert it into decimal and print.

Input format : An integer N
Output format : Corresponding Decimal number (as integer)

Sample Input 1 :
1100

Sample Output 1 :
12

'''


n = int(input())

def B2D(n):
    decimal = 0
    
    i = 0
    while n != 0:
        ls = n % 10                 # Least significant digit
        ms = n // 10                # Most significant digits or number formed by rest digits
        n = ms                  # Update original number with rest digits
        if ls == 1:
        	decimal += 2**i             # Updating decimal when binary digit is 1
        	i += 1
        else:
            i += 1
    
    return decimal

result = B2D(n)
print(result)
