#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 04:34:49 2020

@author: suryakantkumar
"""

'''
Problem : Given a string, find and return the highest occurring character present in the given string.
If there are 2 characters in the input string with same frequency, return the character which comes first.

Note : Assume all the characters in the given string are lowercase.

Sample Input 1:
abdefgbabfba

Sample Output 1:
b

Sample Input 2:
xy

Sample Output 2:
x

'''


string = input()

freq = [0]*256

for char in string:
    freq[ord(char)] += 1
    
most = string[0]

for char in string[1:len(string)]:
    if freq[ord(char)] > freq[ord(most)]:
        most = char

print(most)