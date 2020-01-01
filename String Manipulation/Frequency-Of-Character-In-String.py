#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 03:54:08 2020

@author: suryakantkumar
"""

'''
Problem : Given a string S, Count the frequency of each character in S and print accordingly.

Input :
the quick brown fox jumps over the lazy dog

Outpit : 
a        1
b        1
c        1
d        1
e        3
f        1
g        1
h        2
i        1
j        1
k        1
l        1
m        1
n        1
o        4
p        1
q        1
r        2
s        1
t        2
u        2
v        1
w        1
x        1
y        1
z        1
    
'''


def FrequenctCount(s):
    li = [0]*256
    
    for char in s:
        li[ord(char)] += 1
        
    for i in range(ord('a'), ord('z') + 1):
        print(chr(i), '\t', li[i])

string = input()
FrequenctCount(string)