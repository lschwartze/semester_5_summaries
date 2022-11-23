# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 12:20:01 2022

@author: laurin
"""

import sys

def hashing(m,keys,s):
    values = [0]*m
    for key in keys:
        val = key % m
        while values[val] != 0:
            val += 1
        values[val] = 1
        if key == s:
            return val

def double_hashing(m,keys,s):
    values = [0]*m
    for key in keys:
        val = key % m
        i = 1
        while values[val] != 0:
            step = (key+i*(1+(key % (m-1))) % m)
            val = (val+step) % m
            i += 1
        values[val] = 1
        if key == s:
            return val

if __name__ == '__main__':
    tests = int(sys.stdin.readline())
    for j in range(tests):
        [m,n,s] = sys.stdin.readline().split()
        keys = []
        for i in range(int(n)):
            key = int(sys.stdin.readline())
            keys.append(key)
            
        val1 = hashing(int(m), keys, int(s))
        val2 = double_hashing(int(m), keys, int(s))
        
        sys.stdout.write(f"{val1}\n{val2}")
        if j != tests-1:
            sys.stdout.write("\n")