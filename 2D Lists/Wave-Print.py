#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 03:08:53 2020

@author: suryakantkumar
"""

'''
Problem : Given a two dimensional n*m array, print the array in a sine wave order. i.e. print the first column top to bottom, next column bottom to top and so on.

Note : Print the elements separated by space.

Input format : n, m, array elements (separated by space)

Sample Input : 
3 4 1 2 3 4 5 6 7 8 9 10 11 12

Sample Output :
1 5 9 10 6 2 3 7 11 12 8 4

'''


n_m_array = [int(x) for x in input().strip().split()]
n, m = n_m_array[0], n_m_array[1] 
array = n_m_array[2:]

array_2d = [[array[m*i+j] for j in range(m)] for i in range(n)]

for j in range(m):
    if j % 2 == 0:
        for i in range(n):
            print(array_2d[i][j], end = " ")
    else:
        for k in range(n-1, -1, -1):
            print(array_2d[k][j], end = " ")