# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 18:08:35 2022

@author: laurin
"""

import sys
import operator

def place_brackets(eq):
    ops = {"+": operator.add, "*": operator.mul}
    n = int((len(eq)+1)/2)
    res_max = [[0 for i in range(n)] for i in range(n)]
    res_min = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        res_max[i][i] = int(eq[2*i])
        res_min[i][i] = int(eq[2*i])
        
    for d in range(1,n):
        for i in range(n-d):
            j = i + d
            l_max = [ops[eq[2*x+1]](res_max[i][x],res_max[x+1][j]) for x in range(i,j)]
            l_min = [ops[eq[2*x+1]](res_min[i][x],res_min[x+1][j]) for x in range(i,j)]
            res_max[i][j] = max(l_max)
            res_min[i][j] = min(l_min)
    
    return [res_max[0][n-1], res_min[0][n-1]]

if __name__ == '__main__':
    tests = int(sys.stdin.readline())
    for j in range(tests):
        eq = sys.stdin.readline().strip()
        [max_val, min_val] = place_brackets(eq)
        sys.stdout.write(f'{max_val} {min_val}')
        if j != tests-1:
            sys.stdout.write("\n")