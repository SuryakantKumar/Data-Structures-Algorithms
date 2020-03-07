#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 14:42:20 2020

@author: suryakantkumar
"""

while True:
    try:
        numerator = int(input('Enter numerator : '))
        denominator = int(input('Enter denominator : '))
        
        division = numerator / denominator
    
    except ValueError:          # handling ValueError exception explicitly
        print('Numerator and denominator should be integers')
    
    except ZeroDivisionError:   # handling ZeroDivisionError exception explicitly
        print('Denominator should not bee zero')
        
    except (ValueError, ZeroDivisionError):     # Handling multiple exceptions at a time
        print('Numerator and denominator should be integers and Denominator should not bee zero')
        
    except:
        print('Another exception has been raised')
        
    else:       # Else will execute when no any exception will be raised
        print(division)
        break
    
    finally:    # Finally block will execute whether exception will be raised or not
        print('Exception raised or not')
    