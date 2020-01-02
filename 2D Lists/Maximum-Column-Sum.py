#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 02:44:58 2020

@author: suryakantkumar
"""

'''
Problem : Given an NxM 2D array, you need to find out which column has largest sum (sum of its elements) overall amongst all columns.

Input Format : Line 1 : 2 integers N and M respectively, separated by space
               Line 2: Single line having N*M elements entered in row wise manner, each separated by space.
Output Format : Maximum_Sum Column_number
                
Sample Input :
3 3
3 6 9 1 4 7 2 8 9

Sample Output 2 :
25 2
'''


n, m = (int(x) for x in input().strip().split())
li = [int(x) for x in input().strip().split()]

li_2d = [[li[m * i + j] for j in range(m)] for i in range(n)]

def MaximumColumnSum(li_2d, n, m):
    max_sum = 0
    max_sum_index = -1
    for j in range(m):
        sum = 0
        for i in range(n):
            sum += li_2d[i][j]
        if sum > max_sum:
            max_sum = sum
            max_sum_index = j
            
    return max_sum, max_sum_index

max_sum, max_sum_index = MaximumColumnSum(li_2d, n, m)
print(max_sum, max_sum_index)