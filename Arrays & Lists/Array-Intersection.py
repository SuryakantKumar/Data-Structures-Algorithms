#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 14:21:58 2019

@author: suryakantkumar
"""

'''
Problem : Given two random integer arrays of size m and n, print their intersection. That is, print all the elements that are present in both the given arrays.
Input arrays can contain duplicate elements.

Note : Order of elements are not important

Input format : Line 1 : Array 1 Size
               Line 2 : Array 1 elements (separated by space)
               Line 3 : Array 2 Size
               Line 4 : Array 2 elements (separated by space)
Output format : Print intersection elements in different lines
Constraints : 1 <= m, n <= 10^3

Sample Input :
4
2 6 1 2
5
1 2 3 4 2

Sample Output :
2 
2
1

'''


def ArrayIntersection(li1, m, li2, n):
    for i in range(m):
        for j in range(n):
            if li1[i] == li2[j]:
                print(li1[i])
                li2[j] = -12345678
    
m = int(input())
li1 = [int(x) for x in input().strip().split()]
n = int(input())
li2 = [int(x) for x in input().strip().split()]
ArrayIntersection(li1, m, li2, n)