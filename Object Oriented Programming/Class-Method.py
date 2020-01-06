#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 06:20:20 2020

@author: suryakantkumar
"""

from datetime import date
class Student:
    def __init__(self, name, age, percentage = 80):        # Init method
        self.name = name
        self.age = age
        self.percentage = percentage
    
    @classmethod                       # Class method are factory methods which returns object of the class specified
    def FromBirthYear(cls, name, year, percentage):
        return cls(name, date.today().year - year, percentage)       # class method returns object of the class
    
    def StudentDetails(self):
        print('name :', self.name)
        print('age :', self.age)
        print('percentage :', self.percentage)
        
    def IsPassed(self):
        if self.percentage > 40:
            print(self.name, 'is passed')
        else:
            print(self.name, 'is not passed')
            
    @staticmethod
    def WelcomeToSchool():
        print('Welcome to School')
        
    @staticmethod
    def IsTeen(age):                    # Static methods are used as utility functions, used to check some functionalities
        return age >= 16
        
s = Student('Suryakant', 21, 90)
s.StudentDetails()

print()

s1 = Student.FromBirthYear('shashikant', 2000, 70)        # Object creation from class method
s1.StudentDetails()