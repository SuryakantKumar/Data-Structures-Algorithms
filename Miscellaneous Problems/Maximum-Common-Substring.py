#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 15:10:29 2020

@author: suryakantkumar
"""

'''
Given a sentence w, find maximum length substring out of its words.
'''

def MaximumCommonSubstring(w):
    li = w.strip().split()
    
    l = 12345
    string = ''
    for e in li:
        if len(e) < l:
            string = e
            l = len(e)
    
    substr = []
    for i in range(l):
        for j in range(i+1, l+1):
            substr.append(string[i:j])
            
    max_substr = ''
    max_len = 0
    for ele in substr:
        flag = True
        for e in li:
            if ele not in e:
                flag = False
        if flag == True and len(ele) > max_len:
            max_substr = ele
            max_len = len(ele)
            
    return max_substr, max_len

w = input()
max_substr, max_len = MaximumCommonSubstring(w)
print(max_substr)
print(max_len)