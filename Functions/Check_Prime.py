#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 05:36:47 2019

@author: suryakantkumar
"""

'''
Problem : Write a function to check whether the number N is prime or not.

Sample Input 1 : 
5

Sample output 1 : 
prime

Sample input 2 :
4

Sample output 2:
Not Prime
'''


def IsPrime(n):
    if n < 2:
        return False
    
    d = 2
    while d < n:
        if n % d == 0:
            return False
        d += 1
    return True

n = int(input())
result = IsPrime(n)
if result:
    print('prime')
else:
    print('Not Prime')