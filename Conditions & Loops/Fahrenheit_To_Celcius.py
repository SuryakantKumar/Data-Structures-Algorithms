#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 03:43:26 2019

@author: suryakantkumar
"""

'''
Problrm : Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), you need to convert all Fahrenheit values from Start to End at the gap of W, into their corresponding Celsius values and print the table.

Input Format : 3 integers - S, E and W respectively 
Output Format : Fahrenheit to Celsius conversion table. One line for every Fahrenheit and corresponding Celsius value. On Fahrenheit value and its corresponding Celsius value should be separate by tab ("\t")

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

sf = int(input('Enter start fahrenheit Value : '))
ef = int(input('Enter end fahrenheit Value : '))
step = int(input('Enter step size : '))

while sf <= ef:
    celcius = int((sf - 32) * 5/9)              # Formula for converting fahrenheit to celcius
    print(sf, "\t", celcius)
    sf += step
