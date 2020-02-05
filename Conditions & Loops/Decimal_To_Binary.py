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


# Solution 01

n = int(input())

string = ''
while n != 0:
    ms = n // 2             # Least significant digit
    ls = n % 2              # Most significant digits 
    n = ms              # Update original number with most significant digits
    string += str(ls)               # Update binary string
    
new_str = string[::-1]              # Result will be reverse of binary string
result = int(new_str)
print(result)  



# Solution 02 : Simple approach to find binary

n = int(input())

i = 1
val = 0
while n != 0:
    if n % 2 != 0:              # if remainder is 1
        val += i
    n = n // 2              
    i *= 10

print(val)
