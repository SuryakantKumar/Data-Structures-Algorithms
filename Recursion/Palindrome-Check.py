#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 19:13:36 2020

@author: suryakantkumar
"""

'''
Problem : Check if a given String S is palindrome or not (using recursion). Return true or false.

Input Format : String S

Output Format : true or false

Sample Input 1 :
racecar

Sample Output 1:
true

Sample Input 2 :
ninja

Sample Output 2:
false

'''


def CheckPalindrome(s):
    length = len(s)
    
    if length <= 1:
        return True
    
    if s[0] != s[-1]:
        return False
    
    return CheckPalindrome(s[1:-1])
    
s = input()

result = CheckPalindrome(s)
if result:
    print('true')
else:
    print('false')