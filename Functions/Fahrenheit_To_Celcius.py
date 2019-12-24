#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 07:44:35 2019

@author: suryakantkumar
"""

'''
Problem : Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), you need to convert all Fahrenheit values from Start to End at the gap of W, into their corresponding Celsius values and print the table.

Input Format : 3 integers - S, E and W respectively
Output Format : Fahrenheit to Celsius conversion table. One line for every Fahrenheit and Celsius Fahrenheit value. 

Fahrenheit value and its corresponding Celsius value should be separate by tab ("\t")

Sample Input :
0 
100 
20

Sample Output :
0   -17
20  -6
40  4
60  15
80  26
100 37
'''


s = int(input())
e = int(input())
w = int(input())

def f2c(s, e, w):
    for s in range(s, e+1, w):
        c = int((s-32)*5/9)
        print(s, '\t', c)
f2c(s, e, w)