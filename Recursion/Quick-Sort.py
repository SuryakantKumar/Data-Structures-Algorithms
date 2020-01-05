#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 18:33:30 2020

@author: suryakantkumar
"""

'''
Sort an array A using Quick Sort.
Change in the input array itself. So no need to return or print anything.

Input format : Line 1 : Integer n i.e. Array size
               Line 2 : Array elements (separated by space)
               
Output format : Array elements in increasing order (separated by space)

Constraints : 1 <= n <= 1000

Sample Input:
6 
2 6 8 5 4 3

Sample Output:
2 3 4 5 6 8

'''


def Partition(li, si, ei):
    pivot = li[si]                       # Pivot element
    
    count = 0                            # Count elements smaller than pivot element
    for i in range(si, ei + 1):
        if li[i] < pivot:
            count += 1
    
    li[si], li[si + count] = li[si + count], li[si]    # Move pivot element to its correct position
    
    pivot_index = si + count             # Index of pivot element now
    
    i = si                               # Move element less than pivot to left of it 
    j = ei                               # and elements greater than pivot to right of it 
    while i < j:
        if li[i] < pivot:
            i += 1
        elif li[j] >= pivot:
            j -= 1
        else:
            li[i], li[j] = li[j], li[i]
            i += 1
            j -= 1
    
    return pivot_index
        
def QuickSort(li, si, ei):
    if si >= ei:                         # Base Case when empty list(if si > ei) or when only 1 element left(if si == ei)
        return 
    
    pivot_index = Partition(li, si, ei)        # Find Pivot index
    
    QuickSort(li, si, pivot_index - 1)         # Call Quick sort on elements left to Pivot index element
    QuickSort(li, pivot_index + 1, ei)         # Call Quick sort on elements right to Pivot index element
    
n = int(input())
li = [int(x) for x in input().strip().split()]

si = 0
ei = n - 1
QuickSort(li, si, ei)
print(*li)