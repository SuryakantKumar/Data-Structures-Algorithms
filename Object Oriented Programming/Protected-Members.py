#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 02:15:57 2020

@author: suryakantkumar
"""

class Vehicle:
    
    def __init__(self, color, maxSpeed):
        self.color = color
        self._maxSpeed = maxSpeed       # Protected variable behaves same as public variables
        
    def get_max_speed(self):
        return self._maxSpeed           # There is no need of getter to access protected members
    
    def print_vehicle(self):
        print('Color :', self.color)
        print('maxSpeed :', self._maxSpeed)
        
class Car(Vehicle):

    def __init__(self, color, maxSpeed, numGear, isConvertible):
        super().__init__(color, maxSpeed)
        self.numGear = numGear
        self.isConvertible = isConvertible
        
    def print_car(self):
        super().print_vehicle()         # Accessing parent class method using super()
        print('numGear :', self.numGear)
        print('isConvertible :', self.isConvertible)
        

c = Car('Red', 300, 4, True)
c.print_car()

print()

c._maxSpeed = 320       # We can access and modify protected members outside its class
c.print_car()
