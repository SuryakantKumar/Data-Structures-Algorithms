#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 04:33:27 2020

@author: suryakantkumar
"""

'''
Problem : Given a string and a character x. Write a function to remove all occurrences of x character from the given string.
Leave the string as it is, if the given character is not present in the string.

Input format : Line 1 : Input string
               Line 2 : Character x
               
Sample Input :
welcome to coding ninjas
o

Sample Output :
welcme t cding ninjas

'''


string = input()
character = input()

new_string = ""
for char in string:
    if character != char:
        new_string += char

print(new_string)