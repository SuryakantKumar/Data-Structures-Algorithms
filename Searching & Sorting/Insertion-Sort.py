#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 08:42:58 2020

@author: suryakantkumar
"""

'''
Problem : Given a random integer array. Sort this array using insertion sort.
Change in the input array itself. You don't need to return or print elements.

Input format : Line 1 : Integer N, Array Size
               Line 2 : Array elements (separated by space)
Constraints : 1 <= N <= 10^3

Sample Input 1:
7
2 13 4 1 3 6 28

Sample Output 1:
1 2 3 4 6 13 28

Sample Input 2:
5
9 3 6 2 0

Sample Output 2:
0 2 3 6 9

'''


def InsertionSort(n, li):
    for i in range(1, n):
        consider = li[i]        # Choose one element 
        j = i - 1               # Last index of sorted lements
        
        while j >= 0 and li[j] > consider:     # Compare considered element with sorted elements in reverse
            li[j+1] = li[j]                    # Shift element one index right
            j = j - 1
        li[j+1] = consider                     # Put considered element on right position

n = int(input())
li = [int(x) for x in input().strip().split()]

InsertionSort(n, li)
print(*li)