#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 03:46:58 2019

@author: suryakantkumar
"""

'''
Problem : Write a program that works as a simple calculator. It reads an integer for choice.
1. If the choice is 1, 2 integers are taken for input and their sum is printed.
2. If the choice is 2, 2 integers are taken for input and their difference is printed.
3. If  the choice is 3, 2 integers are taken for input and their product is printed.
4. If  the choice is 4, 2 integers are taken for input and their quotient is printed.
5. If  the choice is 5, 2 integers are taken for input and their remainder is printed.
6. If the choice is 6, the program exits, 
For any other choice, print "Invalid Operation" and ask for choice again.

Note: Each answer in next line.

Input format: Take integers as input, in accordance to the description of the question. 
Constraints: Time Limit: 1 second
Output format: The output lines must be as prescribed in the description of the question.

Sample Input:
3
1
2
4
4
2
1
3
2
7
6

Sample Output:
2
2
5
Invalid Operation
'''

c = int(input('Enter Choice : '))

while c != 6:
    if c >=1 and c <= 5:
        a = int(input('Enter First Value : '))
        b = int(input('Enter Second Value : '))
    if c == 1:
        print(a + b)
    elif c == 2:
        print(a - b)
    elif c == 3:
        print(a * b)
    elif c == 4:
        print(a // b)
    elif c == 5:
        print(a % b)
    elif c < 1 or c > 6:
        print("Invalid Operation")
    c = int(input('Enter Choice : '))