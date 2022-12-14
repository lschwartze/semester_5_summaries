# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 18:50:37 2022

@author: laurin
"""

import sys

def existsCycle(vertices, u):
    cycle = False
    vertices[u][1] = 1
    for v in vertices[u][0]:
        if vertices[v][1] == 1:
            cycle = True
        if vertices[v][1] == 0 and not cycle:
            cycle = existsCycle(vertices, v)
    vertices[u][1] = 2
    return cycle

if __name__ == '__main__':
    #number of test cases
    t = int(sys.stdin.readline())
    for i in range(t):
        #input of graph
        [n,m] = sys.stdin.readline().split()
        vertices = [[[],0] for i in range(int(n))]
        for j in range(int(m)):
            [x,y] = sys.stdin.readline().split()
            vertices[int(y)-1][0].append(int(x)-1)
        cycle = existsCycle(vertices, 0)
        if cycle:
            sys.stdout.write("irre")
        else:
            sys.stdout.write("1")
        if i != t-1:
            sys.stdout.write("\n")