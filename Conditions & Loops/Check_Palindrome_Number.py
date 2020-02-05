#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 03:54:26 2019

@author: suryakantkumar
"""

'''
Problem : Write a program to determine if given number is palindrome or not. Print true if it is palindrome, false otherwise.
Palindrome are the numbers for which reverse is exactly same as the original one. For eg. 121

Sample Input 1 :
121

Sample Output 1 :
true

Sample Input 2 :
1032

Sample Output 2 :
false
'''

n = int(input('Enter Number : '))

real = n

reverse = 0
while n != 0:               # Loop will run till n will become 0
    ls = n % 10             # Least significant digit
    ms = n // 10                # Most significant digits or rest digits number
    n = ms                  # Update original number with rest digits number
    reverse = (reverse * 10) + ls               # Update reverse
    
palindrome = (real == reverse)              # Checking for palindrome

if palindrome:
    print("true")
else:
    print("false")
