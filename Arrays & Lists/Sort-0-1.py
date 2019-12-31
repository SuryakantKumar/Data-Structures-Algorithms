#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 14:40:00 2019

@author: suryakantkumar
"""

'''
Problem : You are given an integer array A that contains only integers 0 and 1. Write a function to sort this array. Find a solution which scans the array only once. Don't use extra array.
You need to change in the given array itself. So no need to return or print anything.

Input format : Line 1 : Integer N (Array Size)
               Line 2 : Array elements (separated by space)
Output format : Sorted array elements
Constraints : 1 <= N <= 10^6

Sample Input :
7
0 1 1 0 1 0 1

Sample Output :
0 0 0 1 1 1 1

'''


def Sort01(li, n):
    i = 0
    j = n-1
    while i < j:
        if li[i] == 0:
            i += 1
        elif li[j] == 1:
            j -= 1
        else:
            li[i], li[j] = li[j], li[i]
            i += 1
            j -= 1
    return

n = int(input())
li = [int(x) for x in input().strip().split()]
Sort01(li, n)
print(*li)