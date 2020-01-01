#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 07:59:23 2020

@author: suryakantkumar
"""

'''
Problem : Given an unsorted array of numbers, write a function that returns true if complete array consists of consecutive numbers. That means if we sort the array, all the elements are consecutive. Array contains only positive numbers.
Try doing it in O(n), where n is the size of given array.

Input Format : Line 1 : An Integer N i.e. size of array
               Line 2 : N integers which are elements of the array, separated by spaces
Output Format : true or false
Constraints : 1 <= N <= 10^6

Sample Input 1 :
6
3 7 2 5 4 6

Sample Output 1 :
true

Sample Input 2 :
6
1 9 2 4 0 3

Sample Output 2 :
false
'''


def ConsecutiveSort(li, n):
    smallest = li[0]
    for ele in li:
        if ele < smallest:
            smallest = ele
    
    sum1 = 0
    sum2 = 0
    for i in range(smallest, smallest + n):
        sum1 += i
        sum2 += li[i - smallest]
        
    if sum1 == sum2:
        return True
    else:
        return False

n = int(input())
li = [int(x) for x in input().strip().split()]

result = ConsecutiveSort(li, n)
if result == True:
    print('true')
else:
    print('false')