#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 18:17:33 2020

@author: suryakantkumar
"""

'''
Problem : Given a string S, remove consecutive duplicates from it recursively.

Input Format : String S
Output Format : Output string
Constraints : 1 <= Length of String S <= 10^3

Sample Input :
aabccba

Sample Output :
abcba

'''


def RemoveConsecutiveDuplicates(string):
    if len(string) == 0 or len(string) == 1:         # Base Case
        return string
    
    smallOutput = RemoveConsecutiveDuplicates(string[1:])
    
    if string[0] != string[1] :
        return string[0] + smallOutput
    else:
        return smallOutput
    
string = input().strip()

result = RemoveConsecutiveDuplicates(string)
print(result)