#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 08:05:54 2020

@author: suryakantkumar
"""

'''
Problem : You are given an array and indices of the array represent minutes and data values represent prices of a stock as they were yesterday . You need to figure out and return the maximum profit you can make by buying and selling of the stock. You can buy and sell the stock only once.

Input Format : Line 1 : An integer N i.e. size of the array
               Line 2 : N integers which are elements of the array, separated by spaces
Output Format : Single integer i.e. Maximum Profit

Sample Input :
4 
2 100 150 120

Sample Output :
148

Sample Output Explanation :
Maximum profit can be achieved by buying stock at minute 0 when its price is Rs. 2 and selling it at minute 2 when its price is Rs 150. Hence profit is Rs. (150 - 2) = Rs. 148

'''

# We can gain maximum profit in two ways : 
# 1. We can sell at highet price
# 2. We can Buy at lowest price
                                         
def ProfitableStock(li, n):
    smallest = li[0]
    small_time = 0
    largest = li[0]
    large_time = 0
    for i in range(n):
        if li[i] <= smallest:
            smallest = li[i]
            small_time = i
        elif li[i] >= largest:
            largest = li[i]
            large_time = i
            
    small_max = smallest
    for i in range(small_time, n):
        if li[i] > small_max:
            small_max = li[i]
            
    large_min = largest
    for i in range(0, large_time):
        if li[i] < large_min:
            large_min = li[i]
            
            
    small_profit = small_max - smallest
    large_profit = largest - large_min
    
    if small_profit > large_profit:
        print(small_profit)
    else:
        print(large_profit)
        
n = int(input())
li = [int(x) for x in input().strip().split()]
ProfitableStock(li, n)