#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 07:18:40 2019

@author: suryakantkumar
"""

'''
Problem : Given a number N, find its square root. You need to find and print only the integral part of square root of N.
For eg. if number given is 18, answer is 4.

Input format : Integer N
Output Format : Square root of N (integer part only)

Sample Input 1 :
10

Sample Output 1 :
3
'''


def squareRoot(n):
    for i in range(1, n//2):
        val = i*i
        if val == n:
           	return i
        elif val > n:
            return i - 1
	
n = int(input())
ans = squareRoot(n)
print(ans)