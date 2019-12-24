#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 07:55:10 2019

@author: suryakantkumar
"""

'''
Problem : Write a Program to determine if the given number is Armstrong number or not. Print true if number is armstrong, otherwise print false.

An Armstrong number is a number (with digits n) such that the sum of its digits raised to nth power is equal to the number itself.

For example,
371, as 3^3 + 7^3 + 1^3 = 371
1634, as 1^4 + 6^4 + 3^4 + 4^4 = 1634

Input Format : Integer n
Output Format : true or false

Sample Input 1 :
1

Sample Output 1 :
true

Sample Input 2 :
103

Sample Output 2 :
false
'''


n = int(input())

def armstrong(n):
    real = n
    new_number = 0
    digits = len(str(n))
    
    while n != 0:
        ls = n // 10
        ms = n % 10
        n = ls
        term =((ms)**(digits))
        new_number = new_number + term
        
    if (new_number == real):
        return True
    else:
        return False
        
if armstrong(n):
    print('true')
else:
    print('false')