#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 08:01:45 2020

@author: suryakantkumar
"""

'''
Problem : Rearrange a given array (that contains equal number of positive & negative numbers) such that +ve and -ve are arranged alternatively. Respective order should be maintained.
Make changes in same array and no returning or printing in needed.

Input Format : Line 1 : N, size of array 
               Line 2 : N elements of array
Output Format : N numbers of output according to above description
Constraints : 1 <= N <= 10^6

Sample Input :
6
1 2 3 -1 -2 -3

Sample Output :
1 -1 2 -2 3 -3 

'''


def Alternatives(li, n):
    k = n//2	
    for i in range(n//2, n-1):
	    temp = li[i]
	    p = i
	    for j in range(k-1):
	        li[p] = li[p - 1]
	        p -= 1
	    li[p] = temp
	    k -= 1
        
    return
        
n = int(input())
li = [int(x) for x in input().strip().split()]

Alternatives(li, n)
print(*li)