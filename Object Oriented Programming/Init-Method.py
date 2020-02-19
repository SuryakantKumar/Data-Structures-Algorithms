#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 06:17:34 2020

@author: suryakantkumar
"""

class Student:
    def __init__(self, name, age, percentage = 80):         # Init method with default argument 'percentage'
        self.name = name            # Instance attributes    
        self.age = age
        self.percentage = percentage
    
    def StudentDetails(self):
        print('name :', self.name)
        print('age :', self.age)
        print('percentage :', self.percentage)
        
    def IsPassed(self):
        if self.percentage > 40:
            print(self.name, 'is passed')
        else:
            print(self.name, 'is not passed')
            
    @staticmethod           # static method does not need to pass default argument self
    def WelcomeToSchool():
        print('Welcome to School')
        
s = Student('Suryakant', 21)

s.WelcomeToSchool()
s.StudentDetails()
s.IsPassed()

print()

s1 = Student('shashikant', 18, 90)
s1.StudentDetails()
s1.IsPassed()
