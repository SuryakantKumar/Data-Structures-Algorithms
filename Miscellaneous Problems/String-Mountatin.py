#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 14:48:02 2020

@author: suryakantkumar
"""

'''
Print characters of string rowwise if characters of string is like this for n = 4
   y     k
  r a   t u
 u   k n   m r 
s     a     a

Output for this string s = 'suryakantkumar' is 'ykratuuknmrsaa'.
'''


def StringMountain(n, s):
    if len(s) < n:
        n = len(s)
        
    for i in range(n-1, -1, -1):
        fstep = (n - i - 1)*2
        sstep = 2* i
        
        j = i
        print(s[j], end = '')
            
        while j < len(s):
            if fstep != 0:
                if j + fstep < len(s):
                    print(s[j + fstep], end = '')
                    j += fstep
                else:
                    break
                
            if sstep != 0:
                if j + sstep < len(s):
                    print(s[j + sstep], end = '')
                    j += sstep
                else:
                    break

n = int(input())           # Number of row
s = input()                # Spreadable string 
StringMountain(n, s)