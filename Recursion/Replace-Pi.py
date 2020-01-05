#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 18:12:52 2020

@author: suryakantkumar
"""

'''
Problem : Given a string, Compute recursively a new string where all 'pi' (i.e, multiple characters) have been replaced with 'k'.

Sample Input 1 :
ppi3.14

Sample Output 1:
p3.143.14

'''


def ReplacePi(s):
    if len(s) == 0 or len(s) == 1:      # Base Case
        return s
    
    if s[0] == 'p' and s[1] == 'i':     
        return '3.14' + ReplacePi(s[2:])
    else:
        return s[0] + ReplacePi(s[1:])

s = input()

result = ReplacePi(s)
print(result)