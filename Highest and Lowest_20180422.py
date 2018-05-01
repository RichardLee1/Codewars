# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 20:17:05 2018

@author: Richard Lee
"""

def high_and_low(numbers):
    x = numbers.split()
    y = []
    for i in x:
        y.append(int(i))
    y.sort()
    numbers = str(y[len(y)-1]) + ' ' + str(y[0])
    return numbers
