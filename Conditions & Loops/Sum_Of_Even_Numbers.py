#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 03:27:51 2019

@author: suryakantkumar
"""

'''
Problem : Given a number N, print sum of all even numbers from 1 to N.

Input Format : Integer N
Output Format : Required Sum 

Sample Input 1 :
6

Sample Output 1 :
12
'''

n = int(input("Enter value of n : "))

sum = 0
while n > 0:
    if n%2 == 0:
        sum += n
        n -= 1
    else:
        n -= 1
print("Sum is : ", sum)