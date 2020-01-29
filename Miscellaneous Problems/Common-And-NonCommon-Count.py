#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 12:45:25 2020

@author: suryakantkumar
"""

'''
Problem : Find the count in the given two arrays as:
• First count common index same value pair
• Then count diffenet indexsame value pair
'''


def CommonAndNoncommon(x, y):    
    count = 0
    
    x1 = {}
    for ele in x:
        if ele in x1:
            x1[ele] += 1
        else:
            x1[ele] = 1
            
    y1 = {}
    for ele in y:
        if ele in y1:
            y1[ele] += 1
        else:
            y1[ele] = 1
            
    for e in x1:
        if e in y1:
            if x1[e] == y1[e]:
                count += x1[e]
            else:
                count += min(x1[e], y1[e])
    
    return count

x = [int(x) for x in input().strip().split()]
y = [int(x) for x in input().strip().split()]
result = CommonAndNoncommon(x, y)
print(result)