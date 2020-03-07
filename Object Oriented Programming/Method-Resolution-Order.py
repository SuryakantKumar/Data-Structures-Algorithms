#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 10:24:02 2020

@author: suryakantkumar
"""

class Father:
    
    def __init__(self):
        self.name = 'Ajay'
        super().__init__()      # Nothing will happen after this because ther is no parent class after this
        
    def print(self):
        print('print of father called')
        
class Mother:
    
    def __init__(self):
        self.name = 'Manju'
        super().__init__()      # Access father class property according to inherit order of child
        
    def print(self):
        print('print of mother called')
        
class Child(Mother, Father):
    
    def __init__(self):
        super().__init__()      # Accessing mother class property

    def print(self):
        print('Name of the child is : ', self.name)
        
        
c = Child()
c.print()       # Its returning mother class property first, then father class proprty
print(Child.mro())      # It will tell the order of method execution according to Child class