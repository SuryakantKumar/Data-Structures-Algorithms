#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 15:52:17 2020

@author: suryakantkumar
"""

'''
Problem : Given an array, Print all the permutations of that array.
'''

def permute(s):
    out = []

    if len(s) <= 1:
        out = [s]
    else:
        for i,let in enumerate(s):
            for perm in permute(s[:i]+s[i+1:]):
                out += [let+perm]
    return out

li = [int(x) for x in input().split()]
string = ''
for e in li:
    string += str(e)
    
ans = permute(string)

for i in ans:
    for j in i:
        print(int(j), end = ' ')
    print()