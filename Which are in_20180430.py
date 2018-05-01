# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 20:17:05 2018

@author: Richard Lee
"""

import numpy
import string
def in_array(array1,array2):
    r = []
    for i in array1:
        for j in array2:
            x = string.find(j,i)
            if x >= 0:
                r.append(i)
                break
    r = list(set(r))
    r.sort()
    return r

a1 = ["arp", "arp", "strong"]
a2 = ['arp', 'bull', 'mice']
y = in_array(a1,a2)
print y
