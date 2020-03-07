#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 11:00:09 2020

@author: suryakantkumar
"""

class Vehicle:
    
    def __init__(self, color, maxSpeed):
        self.color = color              # Instance attribute
        self.__maxSpeed = maxSpeed
        
    def get_max_speed(self):
        return self.__maxSpeed          # Getter for child class
    
    def print_vehicle(self):
        print('Color :', self.color)
        print('maxSpeed :', self.__maxSpeed)    # We can access private values inside the class
        
class Car(Vehicle):

    def __init__(self, color, maxSpeed, numGear, isConvertible):
        super().__init__(color, maxSpeed)       # Accessing the parent class properties
        self.numGear = numGear
        self.isConvertible = isConvertible
        
    def print_car(self):
        super().print_vehicle()         # Accessing parent class method using super()
        self.print_vehicle()            # We can call print_vahicle() using both super() and self
        print('numGear :', self.numGear)
        print('isConvertible :', self.isConvertible)
        

c = Car('Red', 300, 4, True)
c.print_car()
