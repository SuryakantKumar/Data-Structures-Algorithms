#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 06:31:52 2020

@author: suryakantkumar
"""

class Student:
    __school = 'Adarsh Avasiya Vidyalaya'                  # Private variable
    
    def __init__(self, name, age, percentage = 80):        # Init method
        self.__name = name                                 # Private variable, we can't access outside the class
        self.age = age                                     # Public Variable
        self.percentage = percentage
    
    def StudentDetails(self):
        print('name :', self.__name)
        print('age :', self.age)
        print('percentage :', self.percentage)
        
    def IsPassed(self):
        if self.percentage > 40:
            print(self.name, 'is passed')
        else:
            print(self.name, 'is not passed')
    
        
s = Student('Suryakant', 21, 90)
# print(s.__name)                  # We can not access private variables through object
s.StudentDetails()                 # We can access private variables through function call

print(s._Student__name)            # we can access private variable through name mangling concept (syntax : objectName._className__variableName)

print(Student._Student__school)    # Accesssing private variables (making public)

