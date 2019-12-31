#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 14:37:41 2019

@author: suryakantkumar
"""

'''
Problem : Given a random integer array and a number x. Find and print the triplets of elements in the array which sum to x.
While printing a triplet, print the smallest element first.
That is, if a valid triplet is (6, 5, 10) print "5 6 10". There is no constraint that out of 5 triplets which have to be printed on 1st line. You can print triplets in any order, just be careful about the order of elements in a triplet.

Input format : Line 1 : Integer N (Array Size)
               Line 2 : Array elements (separated by space)
               Line 3 : Integer x
Output format : Line 1 : Triplet 1 elements (separated by space)
                Line 2 : Triplet 3 elements (separated by space)
                Line 3 : and so on
Constraints : 1 <= N <= 1000
              1 <= x <= 100
Sample Input:
7
1 2 3 4 5 6 7 
12

Sample Output ;
1 4 7
1 5 6
2 3 7
2 4 6
3 4 5

'''


n = int(input())
li = [int(x) for x in input().strip().split()]
x = int(input())

def printOrder(i, j, k):
    if i <= j and i <= k:
        if j <= k:
            print(i, j, k , sep = " ")
        else:
            print(i, k, j , sep = " ")
            
    elif(j <= i and j <= k):
        if i <= k:
            print(j, i, k, sep = " ")
        else:
            print(j, k, i, sep = " ")
            
    else:
        if i <= j:
            print(k, i, j, sep = " ")
        else:
            print(k, j, i, sep = " ")

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if li[i] + li[j] + li[k] == x:
                printOrder(li[i], li[j], li[k])