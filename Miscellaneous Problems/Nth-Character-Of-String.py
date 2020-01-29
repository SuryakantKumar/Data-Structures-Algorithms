#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 11:57:24 2020

@author: suryakantkumar
"""

'''
Problem : Given a string s, start with nth chaarcter and print every nth chaarcter till the length of the string becomes zero.

input: suryakantkumar
       3
       
output : rktmsyakauanur
'''


def NamePattern(s, n):
    li = [x for x in s]
    
    result = ''
    
    count = len(s)
    i = n - 1
    while count > 0:
        result += li[i]
        count -= 1
        if i + n < len(li):
            i += n
        else:
            i = (i+n) - len(li)
        
    return result

s = input()
n = int(input())

result = NamePattern(s, n)
print(result)