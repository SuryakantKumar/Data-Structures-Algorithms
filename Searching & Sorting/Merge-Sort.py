#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 18:23:47 2020

@author: suryakantkumar
"""

'''
Problem : Sort an array A using Merge Sort.
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


def Merge(li1, li2, li):         # Merge two sorted array
    i = 0
    j = 0
    k = 0
    
    while i < len(li1) and j < len(li2):
        if li1[i] < li2[j]:
            li[k] = li1[i]
            k += 1
            i += 1
        else:
            li[k] = li2[j]
            k += 1
            j += 1
    
    while i < len(li1):
        li[k] = li1[i]
        k += 1
        i += 1
    
    while j < len(li2):
        li[k] = li2[j]
        k += 1
        j += 1 

def MergeSort(li):
    if len(li) == 0 or len(li) == 1:       # Base Case
        return 
    
    mid = len(li)//2
    
    li1 = li[0:mid]                    # Dividing into two arrays
    li2 = li[mid:]
    
    MergeSort(li1)                         # Call merge sort on both divided arrays
    MergeSort(li2)
    
    Merge(li1, li2, li)                    # Call mege on both divided array which has been sorted now

n = int(input())
li = [int(x) for x in input().strip().split()]

MergeSort(li)
print(*li)