#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 07:07:03 2019

@author: suryakantkumar
"""

'''
Problem : Write a program to calculate the total salary of a person. The user has to enter the basic salary (an integer) and the grade (an uppercase character), and depending upon which the total salary is calculated as -
    totalSalary = basic + hra + da + allow – pf
where :
hra   = 20% of basic
da    = 50% of basic
allow = 1700 if grade = ‘A’
allow = 1500 if grade = ‘B’
allow = 1300 if grade = ‘C' or any other character
pf    = 11% of basic.
Round off the total salary and then print the integral part only.

Input format : Basic salary & Grade (separated by space)
Output Format : Total Salary

Sample Input 1 :
10000 A

Sample Output 1 :
17600

Sample Input 2 :
4567 B

Sample Output 2 :
8762
'''

basic, grade = (x for x in input().strip().split())
basic = int(basic)

hra = (basic * 20)/100
da = (basic * 50)/100

if grade == 'A':
    allow = 1700
elif grade == 'B':
    allow = 1500
else:
    allow = 1300
    
pf = (basic * 11)/100

totalsalary = round(basic + hra + da + allow - pf)
print(totalsalary)