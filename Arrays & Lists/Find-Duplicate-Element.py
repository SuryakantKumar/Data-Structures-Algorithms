#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 14:10:56 2019

@author: suryakantkumar
"""

'''
Problem : Given an array of integers of size n which contains numbers from 0 to n - 2. Each number is present at least once. That is, if n = 5, numbers from 0 to 3 is present in the given array at least once and one number is present twice. You need to find and return that duplicate number present in the array.
Assume, duplicate number is always present in the array.

Input format : Line 1 : Size of input array 
               Line 2 : Array elements (separated by space)
Output Format : Duplicate element
Constraints : 1 <= n <= 10^3

Sample Input:
9
0 7 2 5 4 7 1 3 6

Sample Output:
7

'''


#### Solution 01

def DuplicateElement(li, n):
    for i in range(n):
        for j in range(i+1, n):
            if li[i] == li[j]:
                return li[i]
    
n = int(input())
li = [int(x) for x in input().strip().split()]
result = DuplicateElement(li, n)
print(result)


#### Solution 02

def DuplicateElement(n, li):
    sum1 = 0
    for i in range(n):
        sum1 += i
        
    sum2 = 0
    for i in range(n):
        sum2 += li[i]
    
    diff = sum1 - sum2
    duplicate = n - diff - 1
    return duplicate


n = int(input())
li = [int(x) for x in input().strip().split()]
ans = DuplicateElement(n, li)
print(ans)