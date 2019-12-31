#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 14:31:32 2019

@author: suryakantkumar
"""

'''
Problem : Given a random integer array A and a number x. Find and print the pair of elements in the array which sum to x.
Array A can contain duplicate elements.
While printing a pair, print the smaller element first.
That is, if a valid pair is (6, 5) print "5 6". There is no constraint that out of 5 pairs which have to be printed in 1st line. You can print pairs in any order, just be careful about the order of elements in a pair.

Input format : Line 1 : Integer N (Array size)
               Line 2 : Array elements (separated by space)
               Line 3 : Integer x
Output format : Line 1 : Pair 1 elements (separated by space)
                Line 2 : Pair 2 elements (separated by space)
                Line 3 : and so on
Constraints : 1 <= N <= 1000
              1 <= x <= 100
Sample Input:
9
1 3 6 2 5 4 3 2 4
7

Sample Output :
1 6
3 4
3 4
2 5
2 5
3 4
3 4

'''


def PairSum(n, li, x):
    for i in range(n):
        for j in range(i+1, n):
            if li[i] + li[j] == x:
                if li[i] > li[j]:
                    print(li[j], li[i])
                else:
                    print(li[i], li[j])
    
n = int(input())
li = [int(x) for x in input().strip().split()]
x = int(input())
PairSum(n, li, x)