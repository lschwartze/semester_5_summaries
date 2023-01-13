# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 16:34:50 2023

@author: laurin
"""

import sys
import numpy as np

if __name__ == '__main__':
    t = int(sys.stdin.readline())
    for i in range(t):
        (x,y) = sys.stdin.readline().split()
        x = int(x); y = int(y)
        res = np.gcd(x,y)
        sys.stdout.write(str(int((x*y)/(res**2))))
        if i != t-1:
            sys.stdout.write("\n")