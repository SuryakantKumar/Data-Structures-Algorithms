#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 08:52:27 2020

@author: suryakantkumar
"""

'''
Problem : Given a random integer array, push all the zeros that are present to end of the array. The respective order of other elements should remain same.
Change in the input array itself. You don't need to return or print elements. Don't use extra array.

Note : You need to do this in one scan of array only.

Input format : Line 1 : Integer N, Array Size 
               Line 2 : Array elements (separated by space)
Output Format : Array elements (separated by space)
Constraints : 1 <= N <= 10^6

Sample Input 1:
7
2 0 4 1 3 0 28

Sample Output 1:
2 4 1 3 28 0 0

Sample Input 2:
5
0 3 0 2 0

Sample Output 2:
3 2 0 0 0

'''


#### Solution 01 : Fill new array with non-zero elements first and fill rest with zero

def PushZeroesToEnd(n, li):
    new_li = [0]*n
    
    nonZero = 0                        # Fill new list with all non-zero elements first
    for i in range(n):
        if li[i] != 0:
            new_li[nonZero] = li[i]
            nonZero += 1
    
    for k in range(nonZero+1, n):      # Fill all zeroes after all non-zeroes elements
        new_li[k] = 0
    return new_li
    
n = int(input())
li = [int(x) for x in input().strip().split()]

result = PushZeroesToEnd(n, li)
print(*result)



#### Solution 02 : Optimal Approach is, by comaparing non-zero elements with zero elements and change in the given array without taking new array

n = int(input())
li = [int(x) for x in input().strip().split()]

def PushZeroesToEnd(n, li):
    i = 0
    j = 0
    while i < n:
        if li[i] != 0 and li[j] != 0:
            i += 1
            j += 1
        elif li[i] == 0 and li[j] == 0:
            i += 1
        elif li[i] != 0 and li[j] == 0:
            li[i], li[j] = li[j], li[i]
            i += 1
            j += 1 

PushZeroesToEnd(n, li)
print(*li) 