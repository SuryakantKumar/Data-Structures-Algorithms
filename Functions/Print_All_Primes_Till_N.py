#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 07:05:27 2019

@author: suryakantkumar
"""

'''
Problem : Write a function to Print all prime numbers till given number N.

Sample Input 1 : 
15

Sample output 1 : 
2 3 5 7 11 13

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

def PrimeTillN(n):
    k = 2
    while k <= n:
        if IsPrime(k) == True:
            print(k, end = ' ')
        k += 1
        
n = int(input())

PrimeTillN(n)