# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 16:48:34 2019

@author: libingwei
"""

#def backwardsPrime_V0(start, stop):
#    test = []
#    for x in range(start,stop+1):
#        y = int(str(x)[::-1])
#        flag = 0
#        for i in range(2,x):
#            if x%i == 0:
#                flag = 1
#        for j in range(2,y):
#            if y%j == 0:
#                flag = 1
#        if flag == 0:
#            test.append(x)
#    return test

import math
def backwardsPrime(start,stop):
    test = []
    for x in range(start,stop+1):
        y = int(str(x)[::-1])
        flag = 0
        for i in range(2,int(math.sqrt(x))+1):
            if x%i == 0:
                flag = 1
                break
        if flag == 0:
            for j in range(2,int(math.sqrt(y))+1):
                if y%j == 0:
                    flag = 1
                    break
            if flag == 0 and x != y:
                test.append(x)
    return test

backwardsPrime_V1(1,100)
