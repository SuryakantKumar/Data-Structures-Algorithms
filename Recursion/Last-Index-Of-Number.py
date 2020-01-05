#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 17:41:39 2020

@author: suryakantkumar
"""

'''
Problem : Given an array of length N and an integer x, you need to find and
return the last index of integer x present in the array. Return -1 if it is not present in the array.

Last index means - if x is present multiple times in the array, return the index at which x comes last in the array.
You should start traversing your array from 0, not from (N - 1).
Do this recursively. Indexing in the array starts from 0.

Input Format : Line 1 : An Integer N i.e. size of array
               Line 2 : N integers which are elements of the array, separated by spaces
               Line 3 : Integer x
Output Format : last index or -1
Constraints : 1 <= N <= 10^3

Sample Input :
4
9 8 10 8
8

Sample Output :
3

'''


#### Solution 01 : Making Copy of Array everytime on function call on smaller sized list

def LastIndex(n, li, x):
    if n == 0:
        return -1
    
    smallOutput = LastIndex(n-1, li[1:], x)
    
    if smallOutput != -1:
        return 1 + smallOutput
    else:
        if li[0] == x:
            return 0
        else:
            return -1
    
n = int(input())
li = [int(x) for x in input().strip().split()]
x = int(input())

ans = LastIndex(n, li, x)
print(ans)



#### Solution 02 : Optimal Approach

def LastIndexOptimal(n, li, x, si):
    if si == n:
        return -1
    
    output = LastIndexOptimal(n, li, x, si+1)
    
    if output != -1:
        return output
    else:
        if li[si] == x:
            return si
        else:
            return -1

n = int(input())
li = [int(x) for x in input().strip().split()]
x = int(input())

si = 0
result = LastIndexOptimal(n, li, x, si)
print(result)