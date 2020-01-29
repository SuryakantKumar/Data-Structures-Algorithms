#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 10:08:17 2020

@author: suryakantkumar
"""

'''
Problem : Given Array of words, find maximum length common subsequence out of all words of array.
'''

def LogestSubsequenceEachPair(x, y):
    m = len(x)
    n = len(y)
    
    li = [[None]*(n+1) for i in range(m+1)]     # 2d array of None type elements
    
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:            # Fill first row and first column with all zeroes
                li[i][j] = 0
                
            elif x[i-1] == y[j-1]:          # If characters of two words are same then next count will be diagonal + 1
               li[i][j] = li[i-1][j-1] + 1
               
            else:                           # If characters of two words are not same then next count will be maximum of left and above count
                li[i][j] = max(li[i-1][j], li[i][j-1])
                
    p = m
    q = n
    new = ''
    while p >= 0 and q >= 0:        # For finding the subsequence string we will trace the count from bottom right corner
        if li[p][q] != li[p-1][q] and li[p][q] != li[p][q-1]:   # If count is not equal to left and above both, consider the character and move diagonally up
            new += x[p-1]
            p -= 1
            q -= 1
            
        elif li[p][q] == li[p][q-1]:     # If count is equal to above count, move above
            q -= 1
            
        elif li[p][q] == li[p-1][q]:    # If count is equal to left count, move left
            p -= 1
            
    
    return li[m][n], new[::-1]      # Returning subsequence lenth and respective common subsequence

def LongestCommonSubsequence(l):
    length = []             # lengths of common subsequence of two words
    string = []             # common subsequence of two words
    
    for i in range(len(l) - 1):     # Find subsequence of every two words
        for j in range(i + 1, len(l)):
            subseq_len, subseq = LogestSubsequenceEachPair(l[i], l[j])  # length and subsequence of two words
            length.append(subseq_len)
            string.append(subseq)
    
    x = 12345
    result_str = ''
    for ele in string:      # Finding minimum length subsequence which will be the final subsequence of all
        if len(ele) < x:
            x = len(ele)
            result_str = ele
            
    if min(length) == 0:    # if length of subsequence is 0, then we will return empty string
        return 0, ''
    else:
        return min(length), result_str

l = [x for x in input().strip().split()]
length, string = LongestCommonSubsequence(l)
print(length)
print(string)