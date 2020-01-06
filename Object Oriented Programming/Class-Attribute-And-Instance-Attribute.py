#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 05:36:23 2020

@author: suryakantkumar
"""

class Student():
    passingPercentage = 60
    
s1 = Student()                      # Creation of object / instance
s2 = Student()

print(Student.passingPercentage)    # Accessing class Attirbute

s1.name = 'suryakant'               # Instance Attribute
print(s1.name)

s1.passingPercentage = 80           # Instance Attribute now
print(s1.passingPercentage)         # At first, It access the instance attribute; if not present then it access the class attribute 

print(s2.passingPercentage)         # Accessing Class attribute because it's common for all the objects

s2.age = 21
print(s2.age)

# print(s1.age)                     # Error because object 's1' don't have any age attribute