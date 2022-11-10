# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 14:26:30 2022

@author: laurin
"""
import sys

def master(k,m,a):
    factors = [1/element**k for element in a]
    s = sum(factors) 
    if s == 1:
        return 0
    elif s<1:
        if k==2:
            return 1
        else:
            return 0
    else:
        factors = [1/element**2 for element in a]
        if sum(factors) == 1:
            return 1
        else:
            return 0

if __name__ == '__main__':
    tests = int(input())
    #number of test cases
    for i in range(tests):
        input_stuff = sys.stdin.readline().split()
        k = int(input_stuff[0])
        m = int(input_stuff[1])
        a = sys.stdin.readline().split()
        a = list(map(float, a))
        print(master(k,m,a))