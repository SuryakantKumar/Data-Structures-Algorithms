#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 14:56:28 2020

@author: suryakantkumar
"""

'''
Given a number n, we have to find all the prime factors of n.
'''
def PrimeFactors(n):
    li = []
    for i in range(1, int(n**0.5) +1):
        if n % i == 0:
            if i == n // i:
                li.append(i)
            else:
                li.append(i)
                li.append(n//i)
    
    primes = []
    for x in li:
        if x >= 2:
            flag = True
            for i in range(2, x):
                if x % i == 0:
                    flag = False
                    break
            if flag == True:
                primes.append(x)
    return primes

n = int(input())
primes = PrimeFactors(n)
print(*primes)