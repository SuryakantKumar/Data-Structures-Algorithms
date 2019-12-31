#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 03:12:16 2019

@author: suryakantkumar
"""

def LinearSearch(li, ele):
    for i in range(len(li)):
        if li[i] == ele:
            return i
    return -1

li = [int(x) for x in input().strip().split()]
ele = int(input())

result = LinearSearch(li, ele)
print(result)