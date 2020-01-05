#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 18:20:04 2020

@author: suryakantkumar
"""

'''
Problem : Given a sorted integer array (in ascending order) and an element x. You need to search this element x in the given input array using binary search recursively. Return the index of element in the input.
Indexing starts from 0.
Return -1 if x is not present in the input array. 

Input format : Line 1 : Array elements (separated by space)
               Line 2 : Element to be searched (i.e. x)
Output Format : Index
Constraints : 1 <= N <= 10^6

Sample Input 1:
1 3 7 9 11 12 45
3

Sample Output 1:
1

Sample Input 2:
1 2 3 4 5 6 7
9

Sample Output 2:
-1

'''


def BinarySearch(li, x, si, ei):
    if si > ei:                  # Base Case
        return -1
    
    mid = (si + ei)//2
    
    if li[mid] == x:
        return mid
    
    elif li[mid] < x:
        return BinarySearch(li, x, mid+1, ei)
    
    else:
        return BinarySearch(li, x, si, mid-1)
        
li = [int(x) for x in input().strip().split()]
x = int(input())

si = 0
ei = len(li) - 1
result = BinarySearch(li, x, si, ei)
print(result)