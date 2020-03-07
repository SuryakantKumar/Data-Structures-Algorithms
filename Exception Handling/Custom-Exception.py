#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 14:31:04 2020

@author: suryakantkumar
"""

class ZeroDenominatorError(Exception):      # Creating class and inheriting properties of Exception class
                                            # So we can give messages into custom exception
    pass


while True:
    try:
        numerator = int(input('Enter numerator : '))
        denominator = int(input('Enter denominator : '))
        
        if denominator == 0:        # Raising our own exception using raise keyword
            raise ZeroDenominatorError('Denominator should not be zero')
        
        division = numerator / denominator
        
        print(division)
        break
    
    except ValueError:          # handling ValueError exception explicitly
        print('Numerator and denominator should be integers')
    
    except ZeroDivisionError:   # handling ZeroDivisionError exception explicitly
        print('Division is not allowed')
        
    except (ValueError, ZeroDivisionError):     # Handling multiple exceptions at a time
        print('Numerator and denominator should be integers and Denominator should not bee zero')

    except ZeroDenominatorError:            # Custom exception handling
        print('ZeroDenominatorError has been raised')        
    