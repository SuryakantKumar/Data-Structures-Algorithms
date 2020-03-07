#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 10:07:49 2020

@author: suryakantkumar
"""

class Father:
    
    def __init__(self):
        self.name = 'Ajay'
        
    def print(self):
        print('print of father called')
        
class Mother:
    
    def __init__(self):
        self.name = 'Manju'
        
    def print(self):
        print('print of mother called')
        
class Child(Mother, Father):
    
    def __init__(self):
        super().__init__()      # Accessing parent class property

    def printChild(self):
        print('Name of the child is : ', self.name)
        
        
c = Child()
c.printChild()          # Its returning mother class property because Mother comes first in the child class inheriting property