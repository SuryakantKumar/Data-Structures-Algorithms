#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 08:40:02 2020

@author: suryakantkumar
"""

'''Problem : Given a random integer array. Sort this array using bubble sort.
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


def BubbleSort(n, li):
    for i in range(n-1):              # Run it n-1 times because first element will automatically be sorted
        for j in range(n-i-1):        # We need to go till the last unsorted element only
            if li[j] > li[j+1]:       # Compare two adjacent element
                li[j], li[j+1] = li[j+1], li[j]        # Put largest element at the end
           

n = int(input())
li = [int(x) for x in input().strip().split()]

BubbleSort(n, li)
print(*li)