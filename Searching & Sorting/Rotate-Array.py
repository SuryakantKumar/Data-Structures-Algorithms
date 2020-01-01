#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 08:57:02 2020

@author: suryakantkumar
"""

'''
Problem : Given a random integer array of size n, write a function that rotates the given array by d elements (towards left)
Change in the input array itself. You don't need to return or print elements.

Input format : Line 1 : Integer n (Array Size)
               Line 2 : Array elements (separated by space)
               Line 3 : Integer d
Output Format : Updated array elements (separated by space)
Constraints : 1 <= N <= 1000
              1 <= d <= N
Sample Input :
7
1 2 3 4 5 6 7
2

Sample Output :
3 4 5 6 7 1 2

'''


#### Solution 01 : Rotate the array in d rounds and shift one element each time

def Rotate(arr, d):
    k = 0
    while k < d:                   # Loop runs as same time as the position of shifting
        temp = arr[0]              # Storing first element to be rotated
        
        for i in range(0, n-1):    # Shift n-1 elements to left
            arr[i] = arr[i+1]
            
        arr[n-1] = temp            # Restore first element to last index
        k = k + 1

n = int(input())
arr = list(int(i) for i in input().strip().split(" "))
d = int(input())
Rotate(arr, d)
print(*arr)



#### Solution 02 : Rotate the array by shifting d element at a time

def Rotate(n, li, d):
    storage = [0]*d               # Store first d elements
    for i in range(d):
        storage[i] = li[i]
        
    for j in range(n-d):          # Shift elemets to d position left
        li[j] = li[j+d]
    
    count = 0                     # Fill storage elements at the end
    for k in range(n-d, n):
        li[k] = storage[count]
        count += 1

n = int(input())
li = [int(x) for x in input().strip().split()]
d = int(input())

Rotate(n, li, d)
print(*li)



#### Solution 03 : Raverse the array first then, Reverse n-d elements and d element respectively.

n = int(input())
li = [int(x) for x in input().strip().split()] 
d = int(input())

def RotateArray(n, li, d):
    for i in range(0, n//2):                         #Reverse all elements
        li[i], li[n-i-1] = li[n-i-1], li[i]
        
    for j in range(0, (n-d)//2):                     #Reverse n-d elements
        li[j], li[n-d-j-1] = li[n-d-j-1], li[j]
        
    for k in range((d)//2):                          #Reverse last d elements
        li[n-d+k], li[n-k-1] = li[n-k-1], li[n-d+k]
    
RotateArray(n, li, d)
print(*li)