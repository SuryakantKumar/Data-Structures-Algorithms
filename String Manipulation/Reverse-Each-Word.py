#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 04:29:20 2020

@author: suryakantkumar
"""

'''
Problem : Given a string S, reverse each word of a string individually. For eg. if a string is "abc def", reversed string should be "cba fed".

Input Format : String S
Output Format : Updated string
Constraints : 1 <= Length of S <= 1000

Sample Input :
Welcome to Coding Ninjas

Sample Output:
emocleW ot gnidoC sajniN

'''


#### Solution 01

string = input()

words = string.split()
words_new = ""

for word in words:
    for char in range(len(word)-1, -1, -1):
        words_new += word[char]
    words_new += " "
    
print(words_new)



#### Solution 02

string = input()
words = string.split()

new_word = ""

for word in words:
    word = word[::-1]
    new_word += word + " "
    
print(new_word)
