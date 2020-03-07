#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 5 22:50:27 2020

@author: suryakantkumar
"""

class Student:
    name = 'Suryakant'               # Properties of student class
    age = 21
    percentage = 90
    
    def isPassed(self):              # Method of student class
        if self.percentage >= 40 :
            print(self.name, 'is passed')
        else:
            print(self.name, 'is not passed')
            
s1 = Student()                      # Object creation
print(s1.name)                      # properties of object
print(s1.age)
s1.isPassed()                       # Method calling over object

print()

s2 = Student()
print(s2.name)
print(s2.age)
s2.isPassed()
