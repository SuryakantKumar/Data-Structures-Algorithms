#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 17:59:22 2020

@author: suryakantkumar
"""

'''
Problem : Given a string, Compute recursively a new string where all 'x' char have been replaced with 'k'.

Sample Input 1 :
xaxb
x
c

Sample Output 1:
cacb

'''


def ReplaceChar(string, x, k):
    if len(string) == 0:         # Base Case
        return string
    
    output = ReplaceChar(string[1:], x, k)        # Induction Hypothesis
    
    if string[0] == x:           # Induction Step 
        return k + output
    else:
        return string[0] + output
    
string = input()
x = input()
k = input()

result = ReplaceChar(string, x, k)
print(result)