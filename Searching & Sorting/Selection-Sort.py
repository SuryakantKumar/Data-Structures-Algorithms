#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 08:28:32 2020

@author: suryakantkumar
"""

'''
Problem : Given a random integer array. Sort this array using Selection sort.
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


def SelectionSort(n, li):
    for i in range(n-1):                # Run it n-1 times because last elemet will automatically be sorted
        
        minIndex = i                    # Let first index is index with mininum value element
        for j in range(i+1, n):
            if li[j] < li[minIndex]:    # If element we found is less than the minimum element then update min index
                minIndex = j
        li[i], li[minIndex] = li[minIndex], li[i]     # Swap minimum index value to put it on its correct place

n = int(input())
li = [int(x) for x in input().split()]

SelectionSort(n, li)
print(*li)