#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 07:47:27 2019

@author: suryakantkumar
"""

'''
Problem : Given a number N, figure out if it is a member of fibonacci series or not. Return true if the number is member of fibonacci series else false.
Fibonacci Series is defined by the recurrence
    F(n) = F(n-1) + F(n-2)
    
Input Format : Integer N
Output Format : true or false

Sample Input 1 :
5

Sample Output 1 :
true

Sample Input 2 :
14

Sample Output 2 :
false 
'''


n = int(input())

def fibonacci(n):
    n1 = 0
    n2 = 1
    n3 = 1
    
    while n3 < n:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        
    if (n3 == n):
        print("true")
    else:
        print("false")
        
fibonacci(n)