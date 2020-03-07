#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 10:37:04 2020

@author: suryakantkumar
"""

import math

class Point:
    
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        
        
    def __str__(self):
        return "This point is at (" + str(self.__x) + ', ' + str(self.__y) + ")"
    
    def __add__(self, point_object):    # first point will go into self and second will go into point_object
        return Point(self.__x + point_object.__x, self.__y + point_object.__y)
    
    def __lt__(self, point_object):
        return math.sqrt(self.__x**2 + self.__y**2) < math.sqrt(point_object.__x**2 + point_object.__y**2)
        
    
    
p1 = Point(1, 2)
p2 = Point(3, 4)

p3 = p1 + p2

print(p3)

print(p3 > p1)
        