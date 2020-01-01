#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 02:29:52 2020

@author: suryakantkumar
"""

'''
Problem : Given an integer array, which is sorted (in increasing order) and has been rotated by some number k in clockwise direction. Find and return the k.

Input format : Line 1 : Integer n (Array Size)
               Line 2 : Array elements (separated by space)
Output Format : Integer k
Constraints : 1 <= n <= 1000

Sample Input 1:
6
5 6 1 2 3 4

Sample Output 1:
2

Sample Input 2:
5
3 6 8 9 10

Sample Output 2:
0

'''

def ArrayRotation(n, li):
    min_ele = li[0]
    for i in range(0, n):
        if min_ele > li[i]:
            return i
    return 0
        
n = int(input())
li = [int(x) for x in input().strip().split()]

ans = ArrayRotation(n, li)
print(ans)