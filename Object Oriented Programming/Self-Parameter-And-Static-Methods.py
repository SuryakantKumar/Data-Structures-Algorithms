#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 05:52:01 2020

@author: suryakantkumar
"""

class Student:
    
    passingPercentage = 40                # Class Attribute
    
    def StudentDetails(self):             # Instance Methods (With self parameter, we are passing the objects to the function)
        self.name = 'Suryakant'           # Instance attribute (life of instance attribute is lifespan of that object)
        print('name :', self.name)
        
        self.percentage = 80              # Instance attribute
        print('percentage :', self.percentage)
    
    def IsPassed(self):
        if self.percentage > Student.passingPercentage:
            print(self.name, 'is passed')
        else:
            print(self.name, 'is not passed')
    
    @staticmethod                         # This decorator doesn't need to pass default self argument to the function.
    def WelcomeToSchool():                # Static method, not an instance method
        print('Welcome to school')
        
    @staticmethod
    def IsTeen(age):                      # Static method
        return age >= 16

s1 = Student()             # Object creation
s1.StudentDetails()        # method calling over object s1
Student.StudentDetails(s1) # Method calling internally over the object s1 (same as above line)

print()

s1.IsPassed()
s1.WelcomeToSchool()       # Static method calling

print()

s = Student.IsTeen(18)     # Static method calling from student class directly
print(s)