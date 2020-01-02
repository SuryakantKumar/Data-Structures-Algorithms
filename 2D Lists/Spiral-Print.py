#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 03:17:02 2020

@author: suryakantkumar
"""

'''
Problem : Given an N*M 2D array, print it in spiral form. That is, first you need to print the 1st row, then last column, then last row and then first column and so on.
Print every element only once.

Input format : Line 1 : N and M, No. of rows & No. of columns (separated by space) followed by N*M  elements in row wise fashion.

Sample Input :
4 4 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16

Sample Output :
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10

'''


n_m_array = [int(x) for x in input().strip().split()]
n, m = n_m_array[0], n_m_array[1] 
array = n_m_array[2:]

array_2d = [[array[m*i+j] for j in range(m)] for i in range(n)]

new_arr = []

def SpiralPrint(array_2d):
    cs = 0
    ce = m - 1
    rs = 0
    re = n - 1
    
    count = 0
    while (count < m * n):
        for i in range(cs, ce + 1):
            new_arr.append(array_2d[rs][i])
            count += 1
        rs += 1
        
        for j in range(rs, re + 1):
            new_arr.append(array_2d[j][ce])
            count += 1
        ce -= 1
        
        for k in range(ce, cs - 1, -1):
            new_arr.append(array_2d[re][k])
            count += 1
        re -= 1
        
        for l in range(re, rs - 1, -1):
            new_arr.append(array_2d[l][cs])
            count += 1
        cs += 1
        
    return
  
SpiralPrint(array_2d)
print(*new_arr)