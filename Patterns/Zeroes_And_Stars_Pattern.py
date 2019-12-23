#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 04:44:29 2019

@author: suryakantkumar
"""

'''
Problem : Print the following pattern

Pattern for N = 4 is : 
    
*000*000*
0*00*00*0
00*0*0*00
000***000

Input Format : N (Total no. of rows)
Output Format : Pattern in N lines

Sample Input 1 :
3

Sample Output 1 :
*00*00*
0*0*0*0
00***00

'''


n = int(input())

i = 1
while i<= n:
    j = 1
    while j <= i-1:
        print('0', end = '')
        j = j + 1
        
    print('*', end = '')
    
    zeroes = 1
    while zeroes <= n-i:
        print('0', end = '')
        zeroes = zeroes + 1
    
    print('*', end = '')
  
    zeroes = 1
    while zeroes <= n-i:
        print('0', end = '')
        zeroes = zeroes + 1
        
    print('*', end = '')
    
    zeroes = 1
    while zeroes <= i-1:
        print('0', end = '')
        zeroes = zeroes + 1
        
    print()
    i = i + 1