#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 03:57:43 2019

@author: suryakantkumar
"""

'''
Problem : Write a program to input an integer N and print the sum of all its even digits and sum of all its odd digits separately.
Digits means numbers not the places. That is, if the given integer is "13245", even digits are 2 & 4 and odd digits are 1, 3 & 5.

Input format : Integer N
Output format : Sum_of_Even_Digits Sum_of_Odd_Digits (Print first even sum and then odd sum separated by space)

Sample Input :
1234

Sample Output :
6 4
'''

n = int(input('Enter Number : '))

even_sum = 0                # Sum of even digits of number
odd_sum = 0             # Sum of odd digits of number
while n != 0:
    ls = n % 10             # Least significant digit
    ms = n // 10                # Most significant digits
    n = ms              # Update original number with most significant digits
    
    if ls % 2 == 0:             # If last digit is even
        even_sum = even_sum + ls
        
    else:               # If last digit is odd
        odd_sum = odd_sum + ls
        
print(even_sum, " ", odd_sum)
