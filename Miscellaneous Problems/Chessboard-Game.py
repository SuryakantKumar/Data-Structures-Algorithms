#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 13:32:07 2020

@author: suryakantkumar
"""
from functools import lru_cache

@lru_cache
def chessboardGame(x, y):
    print(x, y)
    if x <= 2 or y <= 2:
        return 'Second'
    
    if chessboardGame(x - 2, y + 1) == True or chessboardGame(x - 2, y - 1) == True or chessboardGame(x + 1, y - 2) == True or chessboardGame(x - 1, y - 2) == True:
        return 'Second'
    
    else:
        return 'First'
    
if __name__ == '__main__':
    xy = input().split()
    x = int(xy[0])
    y = int(xy[1])
    result = chessboardGame(x, y)
    print(result)