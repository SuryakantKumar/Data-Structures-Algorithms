#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 03:33:52 2019

@author: suryakantkumar
"""

'''
Problem : Check whether the number N is prime or not.

Sample Input 1 : 
5

Sample output 1 : 
prime

Sample input 2 :
4

Sample output 2:
Not Prime
'''

n = int(input('Enter value of N : '))

d = 2               # Initial divisor is 2 because prime strts with 2
flag = False                # Initially flag is False
while d < n:
    if n % d == 0:              # If n is divisible by any number from 2 to n - 1 then it is not a prime
        flag = True             # Flag will become True if n is divisible by any number from 2 to n - 1
    d += 1
    
if flag:
    print('Not prime')
else:
    print('prime')
