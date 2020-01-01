#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 02:18:19 2020

@author: suryakantkumar
"""

'''
Problem : Given a random integer array of size n, find and return the second largest element present in the array.
If n <= 1 or all elements are same in the array, return -2147483648 i.e. -2^31.

Input format : Line 1 : Integer n (Array Size)
               Line 2 : Array elements (separated by space)
Output Format : Second largest element
Constraints : 1 <= N <= 10^6

Sample Input 1:
7
2 13 4 1 3 6 28

Sample Output 1:
13

Sample Input 2:
5
9 3 6 2 9

Sample Output 2:
6

Sample Input 3:
2
6 6

Sample Output 3:
-2147483648

'''


#### Solution 01 : Sort the array first then find second largest

def SecondLargest(n, li):
    for i in range(n-1):                # Sort the array first
        for j in range(n-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    
    largest = li[-1]
    for ele in li[::-1]:                # find second largest from the end of the array
        if ele < largest:
            return ele
    
n = int(input())
li = [int(x) for x in input().strip().split()]

result = SecondLargest(n, li)
print(result)



#### Solution 02 : Optimal Approach

def SecondLargest(n, li):
    largest = -2**31
    sec_largest = -2**31
    
    for i in range(n):
        if li[i] > largest:                # Update largest and second largest when (element > largest element)
            sec_largest = largest
            largest = li[i]
            
        elif  li[i] < largest:             # Update second largest only if (element < largest element but element > second largest)
            if li[i] != largest and li[i] > sec_largest:
                sec_largest = li[i]
                
    return sec_largest
    
n = int(input())
li = [int(x) for x in input().strip().split()]
ans = SecondLargest(n, li)
print(ans)