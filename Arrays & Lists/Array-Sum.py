#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 12:56:45 2019

@author: suryakantkumar
"""

'''
Problem : Given an array of length N, you need to find and print the sum of all elements of the array.

Input Format : Line 1 : An Integer N i.e. size of array
               Line 2 : N integers which are elements of the array, separated by spaces

Output Format : Sum
Constraints : 1 <= N <= 10^6

Sample Input :
3
9 8 9

Sample Output :
26
'''


def ArraySum(li):
    sum = 0
    for i in li:
        sum += i
    return sum

n = int(input())
li = [int(x) for x in input().strip().split()]
ans = ArraySum(li)
print(ans)