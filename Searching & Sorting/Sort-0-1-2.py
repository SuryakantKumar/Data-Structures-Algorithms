#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 02:31:29 2020

@author: suryakantkumar
"""

'''
Problem : You are given an integer array containing only 0s, 1s and 2s. Write a solution to sort this array using one scan only.
You need to change in the given array itself. So no need to return or print anything.

Input format : Line 1 : Integer n (Array Size)
               Line 2 : Array elements (separated by space)
Output Format : Updated array elements (separated by space)
Constraints : 1 <= n <= 10^6

Sample Input:
7
0 1 2 0 2 0 1

Sample Output:
0 0 0 1 1 2 2

'''


#### Solution 01 : Count No of 0's, 1's and 2's and put it in a new array

def Sort012(n, li):
    count0 = 0
    count1 = 0
    count2 = 0
    
    for i in range(n):             # First count no of Zeroes, One's and Two's
        if li[i] == 0:
            count0 += 1
        elif li[i] == 1:
            count1 += 1
        else:
            count2 += 1
            
    sorted_li = [0]*n              # Arrange Zeroes, One's and Two's
    for i in range(count0):
        sorted_li[i] = 0
        
    for j in range(count0, count0+count1):
        sorted_li[j] = 1
        
    for k in range(count0+count1, count0+count1+count2):
        sorted_li[k] = 2
        
    return sorted_li
    
n = int(input())
li = [int(i) for i in input().strip().split()]

x = Sort012(n, li)
print(*x)



#### Solution 02 : Place 0's and 2's by comparing them at start and end respectively then place 1's in the middle

def Sort012(n, li):
    nz = 0
    nt = n-1
    
    sorted_li = [0]*n
    for ele in li:                  # first start filling zeroes at the start and Two's at the end 
        if ele == 0:
            sorted_li[nz] = 0
            nz += 1
        elif ele == 2:
            sorted_li[nt] = 2
            nt -= 1
            
    while nz <= nt:                 # Fill One's in the middle of Zeroes and Two's
        sorted_li[nz] = 1
        nz += 1
    return sorted_li
    
n = int(input())
li = [int(i) for i in input().strip().split()]

x = Sort012(n, li)
print(*x)



#### Solution 03 : Optimal Approach

def Sort012(n, li):
    i = 0
    nz = 0
    nt = n - 1
    
    while i <= nt:                       # Increse count of i when found One's(1) or seach for zero to swap
        if li[i] == 1:
            i += 1
            
        elif li[i] == 0:                  # Swap Zeroes(0) element with nonZero(nz)
            li[i], li[nz] = li[nz], li[i]
            i += 1
            nz += 1
            
        elif li[i] == 2:                  # Swap Two's(2) elements with non-Two's(nt)
            li[i], li[nt] = li[nt], li[i]
            nt -= 1        

n = int(input())
li = [int(x) for x in input().strip().split()]
Sort012(n, li)
print(*li)