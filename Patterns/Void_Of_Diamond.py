#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 06:55:30 2019

@author: suryakantkumar
"""

'''
Problem : Print the following pattern for the given number of rows. N should be odd.
Pattern for N = 5 is :
    
*****
** **
*   *
** **
*****

Input format : N (Total no. of rows and N can only be odd)
Output format : Pattern in N lines

Sample Input :
9

Sample Output :
*********
**** ****
***   ***
**     **
*       *
**     **
***   ***
**** ****
*********

'''


n = int(input())

n1 = ((n-2)//2) + 1
n2 = n1 - 1

print(n*'*')

i = 1
while i <= n1:
    
    print((n1-i+1)*'*', end = '')
    
    print((2*i-1)*' ', end = '')
    
    print((n1-i+1)*'*', end = '')
    
    print()
    i += 1
    

i = 1
while i <= n2:
    print((i+1)*'*', end = '')
    
    print((2*(n2-i)+1)*' ', end = '')
    
    print((i+1)*'*', end = '')
    
    print()
    i += 1
    
print(n*'*')
