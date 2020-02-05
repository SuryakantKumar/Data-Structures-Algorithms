#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 03:39:00 2019

@author: suryakantkumar
"""

'''
Problem : Print all prime numbers till given number N.

Sample Input 1 : 
15

Sample output 1 : 
2 3 5 7 11 13
'''

n = int(input('Enter Value of N : '))

k = 2               # First Prime number
while k <= n:
    d = 2               # Starting divisible as 2
    flag = False
    while d < k:                # We will check k by dividing all the numbers from 2 to k -1
        if k % d == 0:              # If k is divisible by any number then it is not a prime
            flag = True
        d += 1
        
    if flag == False:               # k will be prime if not any number from 2 to k-1 can divide k
        print(k, end = ' ')
    k += 1
