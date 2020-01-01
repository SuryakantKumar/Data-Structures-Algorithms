#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 02:49:47 2020

@author: suryakantkumar
"""

'''
Problem : Given a string S, Replace given character of the strings accordingly.

Input:
The quick brown fox jumps over the lazy dog
o
x

Output :
The quick brxwn fxx jumps xver the lazy dxg
    
'''

string = input()
character = input()
replace = input()

def ReplaceCharacter(string, character, replace):
    NewString = ''
    for i in range(len(string)):
        if string[i] == character:
            NewString += replace
        else:
            NewString += string[i]
            
    return NewString

result = ReplaceCharacter(string, character, replace)
print(result)