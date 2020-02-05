#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 04:02:38 2019

@author: suryakantkumar
"""

'''
Problem : Nth term of fibonacci series F(n) is calculated using following formula -
    F(n) = F(n-1) + F(n-2), 
Provided N you have to find out the Nth Fibonacci Number. Also F(1) = F(2) = 1.

Input Format : Integer n
Constraints: Time Limit: 1 second
Output Format : Nth Fibonacci term i.e. F(n)
    
Sample Input :
4

Sample Output :
3
'''

n = int(input('Enter Number : '))

n1 = 1              # First fibonacci number
n2 = 1              # Second fibonacci number
if n == 1 or n == 2:
    print(1)
    
elif n >= 3:
    count = 3               # Next fibonacci count
    while count <= n:
        fn = n1 + n2                # Next fibonacci number
        
        if count == n:              # Nth fibonacci number
            print(fn)
        n1 = n2             # Update first number with second number
        n2 = fn             # Update second number with next number
        count = count + 1
