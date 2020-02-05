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

sum = 0             # Initial sum
i = 1               # First number
while i <= n:
    sum += i                # Updating Sum
    i += 1              # Increasing number to be added
print("Sum is : ", sum)
