#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 04:26:27 2020

@author: suryakantkumar
"""

'''
Problem : Given a string, remove all the consecutive duplicates that are present in the given string. 
That means, if 'aaa' is present in the string then it should become 'a' in the output string.

Sample Input:
aabccbaa

Sample Output:
abcba

'''


string = input()
new_string = string[0]           # New String with consecutive duplicates removed

for char in string:
    if new_string[-1] != char:   # Last digit of new string compared to the character in string
        new_string += char       # If it is equal means duplicates are there and we should not add that character into our new string 

print(new_string)