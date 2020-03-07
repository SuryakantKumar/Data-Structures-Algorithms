#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 11:05:35 2020

@author: suryakantkumar
"""

from abc import ABC, abstractmethod

class Automobile(ABC):      # inheriting the ABC(abstract base class) class property so its an abstract class
                            # we can't create objects of abstract class
    def __init__(self, no_of_wheels):
        self.no_of_wheels = no_of_wheels
        print('Automobile created')
        
    @abstractmethod         # abstract method should be implemented in every child class which is inheriting this class property
    def start(self):
        print('Start of abstract class')
    
    @abstractmethod
    def stop(self):
        pass
    
    @abstractmethod
    def drive(self):
        pass
    
    @abstractmethod
    def get_no_of_wheels(self):
        return self.no_of_wheels
    
class Car(Automobile):
    
#    def __init__(self, name):
#        print('Car created')
#        self.name = name
        
    def start(self):        # If we are inheriting abstract class property then we have to implement all the abstractmethods
        pass
    
    def stop(self):
        pass
    
    def drive(self):
        pass
    
    def get_no_of_wheels(self):
        return super().get_no_of_wheels()
    
class Bus(Automobile):
    
#    def __init__(self, name):
#        print('Bus created')
#        self.name = name
        
    def start(self):
        super().start()
        print('Start of bus class')
    
    def stop(self):
        pass
    
    def drive(self):
        pass
    
    def get_no_of_wheels(self):
        return super().get_no_of_wheels()
        
b = Bus(8)
c = Car(4)
b.start()
print(b.get_no_of_wheels())