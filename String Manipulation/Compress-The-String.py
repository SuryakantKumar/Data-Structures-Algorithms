#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 04:37:17 2020

@author: suryakantkumar
"""

'''
Problem : Write a program to do basic string compression. For a character which is consecutively repeated more than once, replace consecutive duplicate occurrences with the count of repetitions.
For e.g. if a String has 'x' repeated 5 times, replace this "xxxxx" with "x5".

Note : Consecutive count of every character in input string is less than equal to 9.
    
Input Format : Input string S
Output Format : Compressed string 
    
Sample Input:
aaabbccdsa

Sample Output:
a3b2c2dsa

'''


string = input()

def compress(string):
    count = 1
    result = string[0]
    
    for i in range(len(string) - 1):
        if(string[i] == string[i+1]):
            count += 1
        else:
            if(count > 1):
                result += str(count)
            result += string[i+1]
            count = 1
            
    if(count > 1):                    # For Last repeating character
        result += str(count)
    return result

result = compress(string)
print(result)