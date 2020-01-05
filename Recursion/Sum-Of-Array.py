#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 10:42:39 2020

@author: suryakantkumar
"""

'''
Problem : Given an array of length N, you need to find and return the sum of all elements of the array.
Do this recursively.

Input Format : Line 1 : An Integer N i.e. size of array
               Line 2 : N integers which are elements of the array, separated by spaces
Output Format : Sum
Constraints : 1 <= N <= 10^3

Sample Input :
3
9 8 9

Sample Output :
26

'''


def ArraySum(n, li):
    if n == 0:
        return 0
    
    if n == 1:
        return li[0]
    
    smallerList = li[1:]
    return li[0] + ArraySum(n - 1, smallerList)

n = int(input())
li = [int(x) for x in input().strip().split()]
result = ArraySum(n, li)
print(result)