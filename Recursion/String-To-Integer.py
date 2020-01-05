#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 19:32:04 2020

@author: suryakantkumar
"""

'''
Problem : Write a recursive function to convert a given string into the number it represents. That is input will be a numeric string that contains only numbers, you need to convert the string into corresponding integer and return the answer.

Input format : Numeric string (string, Eg. "1234")

Output format : Corresponding integer (int, Eg. 1234)

Sample Input 1 :
1231

Sample Output 1:
1231

Sample Input 2 :
12567

Sample Output 2 :
12567

'''


#### Solution 01

def StringToInteger(s):
    if len(s) == 1:                    # We are working on first character at first
        return ord(s) - ord('0')
    
    output = StringToInteger(s[1:])    # Apply recursion on rest of the string
    return (ord(s[0]) - ord('0'))* (10**(len(s[1:]))) + output
    
s = input()
result = StringToInteger(s)
print(result)



#### Solution 02

def StringToIntegerEasy(s):
    if len(s) == 1:
        return ord(s) - ord('0')
    
    output = StringToIntegerEasy(s[:-1])             # Recursion will do their work first 
    return (output * 10) + (ord(s[-1]) - ord('0'))   # then we will do our work for last character
    
s = input()
result = StringToIntegerEasy(s)
print(result)