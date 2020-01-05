#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 22:31:23 2020

@author: suryakantkumar
"""

'''
Problem : Given a string, compute recursively a new string where identical chars that are adjacent in the original string are separated from each other by a "*".

Sample Input 1 :
hello

Sample Output 1:
hel*lo

Sample Input 2 :
xxyy

Sample Output 2:
x*xy*y

Sample Input 3 :
aaaa

Sample Output 3:
a*a*a*a

'''


def PairStar(s):
    if len(s) <= 1:
        return s
    
    if s[0] == s[1]:
        return s[0] + '*' + PairStar(s[1:])     # When adjacents are equal
    else:
        return s[0] + PairStar(s[1:])           # When adjacents are not equal
    
s = input()
result = PairStar(s)
print(result)