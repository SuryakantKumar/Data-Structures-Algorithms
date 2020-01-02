#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 02:40:35 2020

@author: suryakantkumar
"""

'''
Problem : Given a 2D integer array of size M*N, find and print the sum of ith row elements separated by space.

Input Format : Line 1 : Two integers M and N (separated by space) 
               Line 2 : Matrix elements of each row (separated by space)
Output Format : Sum of every ith row elements (separated by space)
Constraints : 1 <= M, N <= 10^3

Sample Input :
4 2 
1 2 3 4 5 6 7 8

Sample Output :
3 7 11 15

'''


mn_value = [int(ele) for ele in input().strip().split()]
n ,m = mn_value[0], mn_value[1]

# n, m = (int(ele) for ele in input().strip().split())

array_input = [int(x) for x in input().strip().split()]
array_2d = [[array_input[m * i + j] for j in range(m)] for i in range(n)]

for i in range(n):
    sum = 0
    for j in range(m):
        sum += array_2d[i][j]
    print(sum, end = " ")