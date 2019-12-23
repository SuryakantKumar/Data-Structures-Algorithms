#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 03:51:11 2019

@author: suryakantkumar
"""

'''
Problem : Write a program to generate the reverse of a given number N. Print the corresponding reverse number.

Input format : Integer N
Constraints: Time Limit: 1 second
Output format : Corresponding reverse number

Sample Input 1 :
1234

Sample Output 1 :
4321

Sample Input 2 :
1980

Sample Output 2 :
891
'''

n=int(input('Enter Number : '))

reverse = 0
while n != 0:
    ls = n // 10
    ms = n % 10     # Most significant digit
    n = ls
    reverse = (reverse * 10) + ms
print('Reverse of Number is :', reverse)