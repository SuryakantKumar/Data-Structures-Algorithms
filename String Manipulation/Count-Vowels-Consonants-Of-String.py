#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 03:41:50 2020

@author: suryakantkumar
"""

'''
Problem : Given a string S, Count vowels and consonants present in the string.

Input :
The quick brown fox jumps over the lazy dog

Output :
11 24

'''


def CountVowelsConsonants(string):
    vowels = 0
    consonants = 0
    
    for i in range(len(string)):
        s = string[i]
        s = s.lower() 
        
        if s in ['a', 'e', 'i', 'o', 'u']:
            vowels += 1
        elif s >= 'a' and s <= 'z':
            consonants += 1
            
    return vowels, consonants


string = input()
Vowels, Consonants = CountVowelsConsonants(string)
print(Vowels, Consonants)