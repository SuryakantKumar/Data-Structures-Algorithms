#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 10:00:03 2020

@author: suryakantkumar
"""

class Circle(object):
    
    def __init__(self, radius):
       self.__radius = radius
       
    def __str__(self):
        return "This is a circle class inheriting properties of object class."
    
c = Circle(5)
print(c)        # "It was printing memory address of object until __str__ overrides it"