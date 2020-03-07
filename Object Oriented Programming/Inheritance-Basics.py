#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 10:35:47 2020

@author: suryakantkumar
"""

class Vehicle:
    
    def __init__(self, color, maxSpeed):
        self.color = color
        self.maxSpeed = maxSpeed
        
class Car(Vehicle):
    
    def __init__(self, color, maxSpeed, numGear, isConvertible):
        super().__init__(color, maxSpeed)
        self.numGear = numGear
        self.isConvertible = isConvertible
        
    def print_car(self):
        print('color :', self.color)
        print('maxSpeed :', self.maxSpeed)
        print('numGear :', self.numGear)
        print('isConvertible :', self.isConvertible)


c = Car('Red', 300, 4, True)
c.print_car()
