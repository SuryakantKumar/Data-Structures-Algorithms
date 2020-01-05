#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 22:38:55 2020

@author: suryakantkumar
"""

'''
Problem : A child is running up a staircase with N steps, and can hop either 1 step, 2 steps or 3 steps at a time. Implement a method to count how many possible ways the child can run up to the stairs. You need to return number of possible ways W.

Input format : Line 1 : Integer N (No. of steps) 

Output Format : Line 1 : Integer W i.e. Number of possible ways

Constraint : (1 <= N <= 30)

Sample Input 1:
4

Sample Output :
7

'''


def Staircase(n):
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    if n == 2:
        return 2
    
    if n == 3:
        return 4
    
    return Staircase(n-1) + Staircase(n-2) + Staircase(n-3)

n = int(input())
result = Staircase(n)
print(result)