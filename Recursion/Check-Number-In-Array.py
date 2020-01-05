#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 10:49:24 2020

@author: suryakantkumar
"""

'''
Problem : Given an array of length N and an integer x, you need to find if x is present in the array or not. Return true or false.
Do this recursively.

Input Format : Line 1 : An Integer N i.e. size of array
               Line 2 : N integers which are elements of the array, separated by spaces
               Line 3 : Integer x
Output Format : true or false
Constraints : 1 <= N <= 10^3

Sample Input :
3
9 8 10
8

Sample Output :
true

'''


#### Solution 01 : Creating New array of lesser size everytime on recursion call

def CheckNumber(n, li, x):
    if n == 0:
        return False
    
    if li[0] == x:
        return True
    
    return CheckNumber(n-1, li[1:], x)

n = int(input())
li = [int(x) for x in input().strip().split()]
x = int(input())

ans = CheckNumber(n, li, x)
if ans:
    print("true")
else:
    print("false")
    
    

#### Solution 02 : Optimal Solution, instead of creating new array, we will cal recursion on specified array
    
def CheckNumber(n, li, x, si):
    if n == si:
        return False
    
    if li[si] == x:
        return True
    
    return CheckNumber(n, li, x, si + 1)

n = int(input())
li = [int(x) for x in input().strip().split()]
x = int(input())

si = 0
ans = CheckNumber(n, li, x, si)
if ans:
    print("true")
else:
    print("false")