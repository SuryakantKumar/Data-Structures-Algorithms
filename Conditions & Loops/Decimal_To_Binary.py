#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 07:16:14 2019

@author: suryakantkumar
"""

'''
Problem : Given a decimal number (integer N), convert it into binary and print.
The binary number should be in the form of an integer.
Note : The given input number could be large, so the corresponding binary number can exceed the integer range. So take the answer as long.

Input format : Integer N
Output format : Corresponding Binary number (long)

Sample Input 1 :
12

Sample Output 1 :
1100
'''


# Solution code 1
n = int(input())

string = ''
while n != 0:
    ls = n // 2
    ms = n % 2
    n = ls
    string += str(ms)
    
new_str = string[::-1]
result = int(new_str)
print(result)  


# Solution code 2
n = int(input())

i = 1
val = 0
while n != 0:
    if n % 2 != 0:
        val += i
    n = n // 2
    i *= 10

print(val)