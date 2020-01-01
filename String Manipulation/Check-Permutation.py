#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 04:16:29 2020

@author: suryakantkumar
"""

'''
Problem : Given two strings, check if they are permutations of each other. Return true or false.
Permutation means - length of both the strings should same and should contain same set of characters. Order of characters doesn't matter.

Note : Input strings contain only lowercase english alphabets.

Input format : Line 1 : String 1 
               Line 2 : String 2
               
Sample Input 1 :
abcde
baedc

Sample Output 1 :
true

Sample Input 2 :
abc
cbd

Sample Output 2 :
false

'''


#### Solution 01 : Using frequency Array

string1 = input()
string2 = input()

if len(string1) == len(string2):
    li = [0]*256
    origional = [0]*256
    
    for char in string1:            # Adding frequency of characters using first string
        li[ord(char)] += 1
        
    for char in string2:            # Removing frequency of characters using Second string
        li[ord(char)] -= 1
        
    if li == origional:
        print("true")
    else:
        print("false")
        
else:
    print("false")
    
    
    
#### Solution 02 : Using Dictionary
    
string1 = input()
string2 = input()

def Permutation(string1, string2):
    frequency = {}
    
    for char in string1:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
            
    for char in string2:
        if char in frequency:
            if frequency[char] == 1:
                del frequency[char]
            else:
                frequency[char] -= 1
        else:
            return False
        
    if frequency:
        return False
    else:
        return True

if Permutation(string1, string2):
    print("true")
else:
    print("false")