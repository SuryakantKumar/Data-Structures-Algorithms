#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 13:42:18 2019

@author: suryakantkumar
"""

'''
Problem : Given an array of length N, swap every pair of alternate elements in the array.
You don't need to print or return anything, just change in the input array itself.

Input Format : Line 1 : An Integer N i.e. size of array
               Line 2 : N integers which are elements of the array, separated by spaces
Output Format : Elements after swapping, separated by space.

Sample Input 1:
6
9 3 6 12 4 32

Sample Output 2 :
3 9 12 6 32 4

'''


def SwapAlternate(li, n):
    for i in range(0, n-1, 2):
        li[i], li[i+1] = li[i+1], li[i]
    return

n = int(input())
li = [int(x) for x in input().strip().split()]
SwapAlternate(li, n)
print(*li)