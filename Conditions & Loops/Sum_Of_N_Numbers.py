#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 03:22:11 2019

@author: suryakantkumar
"""

'''
Problem : Given an integer n, find and print the sum of numbers from 1 to n.
Note : Use while loop only.

Input Format : Integer n
Output Format : Sum
Constraints : 1 <= n <= 100

Sample Input :
10

Sample Output :
55
'''

n = int(input("Enter value of n : "))

sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("Sum is : ", sum)