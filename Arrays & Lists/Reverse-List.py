#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 13:00:35 2019

@author: suryakantkumar
"""

'''
Problem : Given an array of length N, Reverse the elements of the array.
You don't need to print or return anything, just change in the input array itself.

Input Format : Line 1 : An Integer N i.e. size of array
               Line 2 : N integers which are elements of the array, separated by spaces
Output Format : Elements after reversing, separated by space.

Sample Input 1:
6
9 3 6 12 4 32

Sample Output 2 :
32 4 12 6 3 9

'''

#### Solution 01 : Using length of List
def ReverseList(li, n):
    for i in range(n//2):
        li[i], li[n-i-1] = li[n-i-1], li[i]
    return

n = int(input())
li = [int(x) for x in input().strip().split()]
ReverseList(li, n)
print(*li)

#### Solution 02 : Using Negative Indexing Concept

def ReverseList(li):
    for i in range(n//2):
        li[i], li[-i-1] = li[-i-1], li[i]
    return

n = int(input())
li = [int(x) for x in input().strip().split()]
ReverseList(li)
print(*li)

#### Solution 03 : Using List Slicing Concept

def ReverseList(li):
    li = li[::-1]
    return li

n = int(input())
li = [int(x) for x in input().strip().split()]
result = ReverseList(li)
print(*result)