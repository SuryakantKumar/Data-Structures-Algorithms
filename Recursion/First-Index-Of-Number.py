#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 10:50:35 2020

@author: suryakantkumar
"""

'''
Problem : Given an array of length N and an integer x, you need to find and
return the first index of integer x present in the array. Return -1 if it is not present in the array.

First index means, the index of first occurrence of x in the input array.
Do this recursively. Indexing in the array starts from 0.

Input Format : Line 1 : An Integer N i.e. size of array
               Line 2 : N integers which are elements of the array, separated by spaces
               Line 3 : Integer x
Output Format : first index or -1
Constraints : 1 <= N <= 10^3

Sample Input :
4
9 8 10 8
8

Sample Output :
1

'''


#### Solution 01 : Making Copy everytime on recursion call

def FirstIndex(n, li, x):
    if n == 0:             # Base case when list will get empty
        return -1
    
    if li[0] == x:         # Base case when we found the element at 0th index of new array
        return 0
    
    smallList = li[1:]     # Smaller list input
    output = FirstIndex(n-1, smallList, x)
    
    if output == -1:
        return -1
    else:
        return output + 1
    
n = int(input())
li = [int(x) for x in input().strip().split()]
x = int(input())

result = FirstIndex(n, li, x)
print(result)



#### Solution 02 : Optimal Approach

def FirstIndexOptimal(n, li, x, si):
    if si == n:               # Base case for empty list when start index crosses the last element of list
        return -1
    
    if li[si] == x:           # When found the element at si 
        return si
    
    return FirstIndexOptimal(n, li, x, si+1)

n = int(input())
li = [int(x) for x in input().strip().split()]
x = int(input())

si = 0                                          # Start inex
ans = FirstIndexOptimal(n, li, x, si)
print(ans)