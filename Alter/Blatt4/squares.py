# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 13:42:35 2022

@author: laurin
"""

import sys
import numpy as np
from numpy import median

def squares(x, y):
    res_x = median(x)
    res_y = median(y)
    return res_x, res_y

if __name__ == '__main__':
    tests = int(sys.stdin.readline())
    #number of test cases
    for i in range(tests):
        inputs = sys.stdin.readline().split()
        m = int(inputs[1])
        x = np.zeros(m)
        y = np.zeros(m)
        for j in range(m):
            friend = sys.stdin.readline().split()
            x[j] = int(friend[0])
            y[j] = int(friend[1])
            
        a,b = squares(x, y)
        sys.stdout.write(f'{int(a)} {int(b)}')
        if i != tests-1:
            sys.stdout.write("\n")
