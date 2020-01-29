#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 15:02:08 2020

@author: suryakantkumar
"""

'''
Print all the words of a given string s column wise.
'''


def ColumnWiseWord(s):
    w = s.strip().split()
    
    l = 0
    string = ''
    for e in w:
        if len(e) > len(string):
            string = e
            l = len(e)
         
    length = len(w) if len(w) > l else l
    
    matrix = [[' ' for j in range(length)] for i in range(l)]    
    
    for i in range(len(w)):
        for j in range(len(w[i])):
            matrix[j][i] = w[i][j]
    
    for e in matrix:
        print(*e)
        
s = input()
ColumnWiseWord(s)