#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 10:24:20 2020

@author: suryakantkumar
"""

'''
Problem : Print first n natural numbers in reverse using recursion.

Sample Input 1 :
5

Sample Output 1 :
5 4 3 2 1

'''


def PrintNaturalReverse(n):
    if n == 0:
        return 
    
    print(n, end = ' ')
    PrintNaturalReverse(n - 1)
    
n = int(input())
PrintNaturalReverse(n)