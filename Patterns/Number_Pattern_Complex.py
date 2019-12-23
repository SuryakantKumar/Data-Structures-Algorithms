#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 02:13:06 2019

@author: suryakantkumar
"""
'''
Problem : Print the number pattern for n = 5 as:

1 2 3 4 5 
11 12 13 14 15 
21 22 23 24 25 
16 17 18 19 20 
6 7 8 9 10 

for n = 4 as:
    
1 2 3 4 
9 10 11 12 
13 14 15 16 
5 6 7 8 

'''
row = int(input())

if row % 2 == 0:
    first_half = row//2 
else:
    first_half = (row + 1)//2
    
no = 1
for i in range(1, first_half + 1):
    if i > 1:
        no += (2 * row)
        
    for j in range(no, no + row):
        print(j, end = ' ')
    print()
    
if row % 2 == 0:            # Intermediate jump for even rows
    no += row
else:                       # Intermediate jump for odd rows
    no -= row   

for k in range(row - first_half):
    for l in range(no, no+row):
        print(l, end = ' ')
    print()
    no -= (2 * row)
