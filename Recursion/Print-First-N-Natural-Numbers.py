#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 10:15:09 2020

@author: suryakantkumar
"""

'''
Problem : Print first n natural numbers using recursion.

Sample Input 1 :
5

Sample Output 1 :
1 2 3 4 5

'''


def PrintNatural(n):
    if n == 0:
        return 
    
    PrintNatural(n - 1)
    print(n, end = ' ')
    
n = int(input())
PrintNatural(n)