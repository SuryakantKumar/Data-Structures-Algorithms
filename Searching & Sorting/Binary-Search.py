#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 08:25:09 2020

@author: suryakantkumar
"""

'''Problem : Given a sorted integer array (in ascending order) and an element x. You need to search this element x in the given input array using binary search. Return the index of element in the input.
Indexing starts from 0.
Return -1 if x is not present in the input array. 

Input format : Line 1 : Integer N, Array Size
               Line 2 : Array elements (separated by space)
               Line 3 : Element to be searched (i.e. x)
Output Format : Index
Constraints : 1 <= N <= 10^6

Sample Input 1:
7
1 3 7 9 11 12 45
3

Sample Output 1:
1

Sample Input 2:
7
1 2 3 4 5 6 7
9

Sample Output 2:
-1

'''



n = int(input())
li = [int(x) for x in input().strip().split()]
ele = int(input())

def BinarySeach(n, li, ele):
    start = 0
    end = n - 1

    if ele < li[start] or ele > li[end]:      # If element not in list
        return -1
    
    while start <= end:
        mid = (start + end)//2                # Mid
        
        if li[mid] == ele:                    # Element Found
            return mid
        elif li[mid] < ele:                   # Element is on the right of mid
            start = mid + 1
        elif li[mid] > ele:                   # Element is on the left of mid
            end = mid - 1
    else:
        return -1

ans = BinarySeach(n, li, ele)
print(ans)