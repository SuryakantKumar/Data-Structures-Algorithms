#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 02:43:34 2020

@author: suryakantkumar
"""

'''
Problem : Two random integer arrays are given A1 and A2, in which numbers from 0 to 9 are present at every index (i.e. single digit integer is present at every index of both given arrays).
You need to find sum of both the input arrays (like we add two integers) and put the result in another array i.e. output array (output arrays should also contain only single digits at every index).
The size A1 & A2 can be different.

Note : Output array size should be 1 more than the size of bigger array and place 0 at the 0th index if there is no carry. No need to print the elements of output array.

Input format : Line 1 : Integer n1 (A1 Size)
               Line 2 : A1 elements (separated by space)
               Line 3 : Integer n2 (A2 Size)
               Line 4 : A2 elements (separated by space)
Output Format : Output array elements (separated by space)
Constraints : 1 <= n1, n2 <= 10^6

Sample Input 1:
3
6 2 4
3
7 5 6

Sample Output 1:
1 3 8 0

Sample Input 2:
3
8 5 2
2
1 3

Sample Output 2:
0 8 6 5

'''


n1 = int(input())
li1 = [int(x) for x in input().strip().split()]
n2 = int(input())
li2 = [int(x) for x in input().strip().split()]

def SumOfTwoArrays(n1, li1, n2, li2):
    n3 = n1 if n1 > n2 else n2                          
    li3 = [0] * (n3+1)                    # Including one carry digit in final sum
    
    carry = 0
    i1 = n1 - 1
    i2 = n2 - 1
    i3 = n3 -1
    
    while i3 >= 0:
        sum = 0
        
        if i1 >= 0 :                      # Adding elements of first array from the end
            sum += li1[i1]
            i1 -= 1
            
        if i2 >= 0:                       # Adding elements of second array from the end
            sum += li2[i2]
            i2 -= 1
            
        sum += carry                      # Adding the carry to find final sum
        carry = sum // 10                 # finding the most significant digit as carry
        li3[i3] = sum % 10                # Least significant digit will get stored in the result array from end 
        i3 -= 1
    return li3

ans = SumOfTwoArrays(n1, li1, n2, li2)
print(*ans)