#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 12:06:37 2020

@author: suryakantkumar
"""

while True:
    try:
        numerator = int(input('Enter numerator : '))
        denominator = int(input('Enter denominator : '))
        
        division = numerator / denominator
        
        print(division)
        break
    
    except ValueError:          # handling ValueError exception explicitly
        print('Numerator and denominator should be integers')
    
    except ZeroDivisionError:   # handling ZeroDivisionError exception explicitly
        print('Denominator should not bee zero')
        
    except (ValueError, ZeroDivisionError):     # Handling multiple exceptions at a time
        print('Numerator and denominator should be integers and Denominator should not bee zero')
        
    except:
        print('Another exception has been raised')