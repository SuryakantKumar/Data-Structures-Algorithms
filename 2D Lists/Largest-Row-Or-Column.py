#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 03:05:55 2020

@author: suryakantkumar
"""

'''
Problem : Given an NxM 2D array, you need to find out which row or column has largest sum (sum of its elements) overall amongst all rows and columns.

Input Format : Line 1 : 2 integers N and M respectively, separated by space
               Line 2: Single line having N*M elements entered in row wise manner, each separated by space.
Output Format : If row sum is maximum then - "row" row_num max_sum
                If column sum is maximum then - "column" col_num max_sum
                
Note : If there are more than one rows/columns with maximum sum consider the row/column that comes first. And if ith row and jth column has same sum (which is largest), consider the ith row as answer.

Sample Input 1 :
2 2 
1 1 1 1

Sample Output 1 :
row 0 2

Sample Input 2 :
3 3
3 6 9 1 4 7 2 8 9

Sample Output 2 :
column 2 25

'''


n, m = (int(x) for x in input().strip().split())

array = [int(x) for x in input().split()]
array_2d = [[array[m*i+j] for j in range(m)] for i in range(n)]

max_row_sum = 0
row_no = -1
for i in range(n):
    row_sum = 0
    for j in range(m):
        row_sum += array_2d[i][j]
    if max_row_sum < row_sum:
        max_row_sum = row_sum
        row_no = i

max_col_sum = 0
col_no = -1
for j in range(m):
    col_sum = 0
    for i in range(n):
        col_sum += array_2d[i][j]
    if max_col_sum < col_sum:
        max_col_sum = col_sum
        col_no = j
        
if max_row_sum >= max_col_sum:
    print("row" + " " + str(row_no) + " " + str(max_row_sum))
else:
    print("column" + " " + str(col_no) + " " + str(max_col_sum))