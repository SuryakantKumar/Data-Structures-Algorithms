#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 08:46:15 2020

@author: suryakantkumar
"""

'''
Problem : Given two sorted arrays of Size M and N respectively, merge them into a third array such that the third array is also sorted.

Input Format : Line 1 : Size of first array i.e. M
               Line 2 : M elements of first array separated by space
               Line 3 : Size of second array i.e. N
               Line 2 : N elements of second array separated by space
Output Format : M + N integers i.e. elements of third sorted array separated by spaces.
Constraints : 1 <= M, N <= 10^6

Sample Input :
5
1 3 4 7 11
4
2 4 6 13

Sample Output :
1 2 3 4 4 6 7 11 13

'''


#### Solution 01 : Copy elements of both the arrays into one single array and sort that bigger array

def MergeTwoSortedArray(m, li1, n, li2):
    new_li = [0]*(m+n)                   # Take new list of size (m + n)
    
    for i in range(m):                   # Copy elements of both lists into new list
        new_li[i] = li1[i]
    for j in range(m, m+n):
        new_li[j] = li2[j-m]
    
    for i in range(len(new_li)-1):       # Apply Bubble Sort On New Array (Apply any sorting algorithm)
        for j in range(len(new_li)-i-1):
            if new_li[j] > new_li[j+1]:
                new_li[j], new_li[j+1] = new_li[j+1], new_li[j]
    return new_li

m = int(input())
li1 = [int(x) for x in input().strip().split()]
n = int(input())
li2 = [int(x) for x in input().strip().split()]

x = MergeTwoSortedArray(m, li1, n, li2)
print(*x)



#### Solution 02 : Optimal Approach is Compare elements of both arrays and put it on one single large array

m = int(input())
li1 = [int(x) for x in input(). strip().split()]
n = int(input())
li2 = [int(x) for x in input(). strip().split()]

def MergeTwoSortedArrays(m, li1, n, li2):
    mergedArray = []
    i = 0
    j = 0
    while i < m and j < n:                   # Fill new merged sorted array till one list is getting empty
        if li1[i] <= li2[j]:
            mergedArray.append(li1[i])
            i += 1
        else:
            mergedArray.append(li2[j])
            j += 1
            
    while i < m :                            # Fill with the elements directly if second array got empty
        mergedArray.append(li1[i])
        i += 1
        
    while j < n :                            # Fill with the elements directly if first array got empty          
        mergedArray.append(li2[j]) 
        j += 1
    return mergedArray
        
ans = MergeTwoSortedArrays(m, li1, n, li2)
print(*ans)