#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 18:11:40 2020

@author: suryakantkumar
"""

'''
Problem : Given a string, compute recursively a new string where all 'x' chars have been removed.

Sample Input 1 :
xaxb

Sample Output 1:
ab

Sample Input 2 :
abc

Sample Output 2:
abc

Sample Input 3 :
xx

Sample Output 3:

    
'''


def RemoveX(string):
    if len(string) == 0:          # Base case
        return string
    
    output = RemoveX(string[1:])  # Induction hypothesis
    
    if string[0] == 'x':          # Induction step
        return output
    else:
        return string[0] + output
    
string = input()

result = RemoveX(string)
print(result)