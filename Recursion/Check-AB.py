#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 22:33:35 2020

@author: suryakantkumar
"""

'''
Problem : Suppose you have a string made up of only 'a' and 'b'. Write a recursive function that checks if the string was generated using the following rules:
a. The string begins with an 'a'
b. Each 'a' is followed by nothing or an 'a' or "bb"
c. Each "bb" is followed by nothing or an 'a'
If all the rules are followed by the given string, return true otherwise return false.

Sample Input:
abb

Sample Output:
true

'''


def CheckAB(s):
    if len(s) == 0:
        return True
    
    elif len(s) == 1 and s[0] == 'a':
        return True
    
    elif s[0] == 'a':
        if s[1] == 'a':
            return True and CheckAB(s[1:])
        
        if s[1] == 'b' and len(s) == 2:
            return False
        
        if s[1] == 'b' and s[2] == 'b':
            return True and CheckAB(s[3:])
    else:
        return False
    
s = input()

result = CheckAB(s)
print('true') if result == True else print('false')