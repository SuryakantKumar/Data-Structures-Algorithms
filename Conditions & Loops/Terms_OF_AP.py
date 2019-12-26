#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 07:10:40 2019

@author: suryakantkumar
"""

'''
Problem : Write a program to print first x terms of the series 3N + 2 which are not multiples of 4.
N varies from 1 to 1000.

Sample Input 1 :
10

Sample Output 1 :
5 11 14 17 23 26 29 35 38 41
'''


x = int(input())

if x >= 1:
    val = 5
    
count = 1
while count <= x:
    if val % 4 != 0:
        print(val, end = ' ')
        val += 3
        count += 1
    else:
        val += 3