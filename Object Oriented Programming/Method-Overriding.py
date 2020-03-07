#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 16:50:09 2020

@author: suryakantkumar
"""

class Vehicle:
    
    def __init__(self, color, maxSpeed):
        self.color = color
        self.__maxSpeed = maxSpeed          # private attribute
        
    def print_vehicle(self):
        print(self.color)
        print(self.__maxSpeed)
        

class Car(Vehicle):
    '''self.common_function() calls the child class first.
    If the function is unavailable in child class then it searches in parent class.
    It means if same function present in both of the classes then,
    super().common_function() will override the child class common function.
    '''
    
    def __init__(self, color, maxSpeed, numGears, isConvertible):
        super().__init__(color, maxSpeed)   # Inheriting some properties from vehicle class
        self.numGears = numGears
        self.isConvertible = isConvertible
        
    def print_vehicle(self):
        # self.print_vehicle()    # It is calling the Child class print_vehicle() function recursively
        super().print_vehicle()     # It is accessing Vehicle class i.e, super class print_vehicle() function
        print(self.numGears)
        print(self.isConvertible)
        
c = Car('Red', 240, 4, True)        
c.print_vehicle()