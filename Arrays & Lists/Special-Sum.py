#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 14:56:36 2019

@author: suryakantkumar
"""

'''
Problem : Given an array of length N, which contains single digit elements at every index. You need to find and return the sum of all elements of the array. But the final sum should also be single digit.
In order to keep the output single digit - you need to keep adding the output number digits till single digit is left.

Input Format : Line 1 : An Integer N i.e. size of array
               Line 2 : N integers which are elements of the array, separated by spaces
Output Format : Single digit sum
Constraints : 1 <= N <= 10^6

Sample Input :
5
1 7 8 5 9

Sample Output :
3

Sample Output Explanation :
1 + 7 + 8 + 5 + 9 = 30
3 + 0 = 3
Hence, ans is 3.

'''


n = int(input())
li = [int(x) for x in input().strip().split()]

sum1 = 0
for ele in li:
    sum1 += ele

sum = str(sum1)
while len(sum) > 1:
    final = 0
    for i in range(len(sum)):
        final += int(sum[i])
    sum = str(final)
    
print(int(sum))