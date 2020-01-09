#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 12:15:53 2020

@author: suryakantkumar
"""

'''
Problem : Watson likes to challenge Sherlock's math ability.
He will provide a starting and ending value describing a range of integers. 
Sherlock must determine the number of square integers within that range, 
inclusive of the endpoints.

Note : A square integer is an integer which is the square of an integer, e.g. 1, 4, 9, 16, 25.

For example, the range is a = 24 and b = 49, inclusive. There are three square integers in the range:25, 36 and 49.

Sample Input : 
2
3 9
17 24

Sample Output  :
2
0

'''
import math 

#### Solution 01 : Using Ordinary Method

def IsSquare(a):
    if a == 1:
        return True
    
    for i in range(2, (a//2)+1):
        if i * i == a:
            return True
    return False

def squares(a, b):
    count = 0
    for ele in range(a, b+1):
        if IsSquare(ele) == True:
            count += 1
    return count

n = int(input())
for i in range(n):
    a, b = (int(x) for x in input().strip().split())
    value = squares(a, b)
    print(value)



#### Solution 02 : Using sqrt() function

def squares(a, b):
    count = 0
    for ele in range(a, b+1):
        ps = math.sqrt(ele)
        if ps - int(ps) == 0:
            count += 1
    return count

n = int(input())
for i in range(n):
    a, b = (int(x) for x in input().strip().split())
    value = squares(a, b)
    print(value)



#### Solution 03 : Optimal Solution For bigger Inputs
    
def squares(a, b):
    a_sq = math.ceil(math.sqrt(a))
    b_sq = math.floor(math.sqrt(b))
    
    return b_sq - a_sq + 1

n = int(input())
for i in range(n):
    a, b = (int(x) for x in input().strip().split())
    value = squares(a, b)
    print(value)
