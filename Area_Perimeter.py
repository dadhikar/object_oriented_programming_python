#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 14:21:29 2019

@author: dasharath
"""
#import numpy as np

class Area_Perimeter():
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def Area(self):
        return self.length * self.width 
    def Perimeter(self):
        return 2 * (self.length + self.width)
    
Playground = Area_Perimeter(4, 5)

print("The area of the playground: ", Playground.Area())   
print("The perimeter of the playground:", Playground.Perimeter()) 
        