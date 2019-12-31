#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 13:58:44 2019

@author: suryakantkumar
"""

'''
Problem : Given an integer array of size 2N + 1. In this given array, N numbers are present twice and one number is present only once in the array.
You need to find and return that number which is unique in the array.

Note : Given array will always contain odd number of elements.

Input format : Line 1 : Array size i.e. 2N+1
               Line 2 : Array elements (separated by space)
Output Format : Unique element present in the array
Constraints : 1 <= N <= 10^3

Sample Input :
7
2 3 1 6 3 6 2

Sample Output :
1
'''


def UniqueElement(li, n):
    for i in range(n):
        if li[i] not in li[:i] and li[i] not in li[i+1:]:
            return li[i]
    
n = int(input())
li = [int(x) for x in input().strip().split()]
result = UniqueElement(li, n)
print(result)