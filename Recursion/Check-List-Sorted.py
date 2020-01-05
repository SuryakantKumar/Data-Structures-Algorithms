#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 10:38:21 2020

@author: suryakantkumar
"""

'''
Problem : Given a list. Check if it is sorted or not ?

Sample Input 1 :
5 7 9 10

Sample Output 1 :
true

Sample Input 2 :
5 7 3 11 2

Sample Output 2 :
false

'''

#### Solution 01 : Creating New list on every recursion call

def isSorted(li):
    length = len(li)
    
    if length == 0 or length == 1:
        return True
    
    if li[0] > li[1]:
        return False
    
    smallerList = li[1:]
    return isSorted(smallerList)
    
li = [int(x) for x in input().strip().split()]

if isSorted(li):
    print('true')
else:
    print('false')
    
#### Solution 02 : Optimal Solution

def isSorted(li, si):
    length = len(li)
    
    if si == length or si == length - 1:
        return True
    
    if li[si] > li[si + 1]:
        return False
    
    return isSorted(li, si + 1)

li = [int(x) for x in input().strip().split()]

si = 0
if isSorted(li, si):
    print('true')
else:
    print('false')