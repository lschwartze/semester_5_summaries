# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 18:51:17 2022

@author: laurin

for a given graph on n vertices and m edges, find a minimum spanning tree using 
Kruskals algorithm. Implemented via a union-find datastructure
"""
import sys

#kruskals algorithm
def kruskal(vertices, edges):
    #initialize the size array for a union-find datastructure
    size = [1]*len(vertices)
    edges.sort()
    min_weight = 0
    for edge in edges:
        canon_nodes = [find(vertices, edge[1]), find(vertices, edge[2])]
        #if the canonical vertices are the same, adding the current edge
        #would result in a cycle
        if canon_nodes[0] != canon_nodes[1]:
            min_weight += edge[0]
            [vertices, size] = union(vertices, size, canon_nodes[0], canon_nodes[1])
    return min_weight
    
#union function to append two components
def union(arr, size, i, j):
    if size[i] < size[j]:
        arr[i] = arr[j]
        size[j] = size[i] + size[j]
    else:
        arr[j] = arr[i]
        size[i] = size[i] + size[j]
    return arr, size

#find function to return the canonical node for a given vertex
def find(arr, i):
    if i != arr[i]:
        arr[i] = find(arr, arr[i])
    return arr[i]
    

if __name__ == '__main__':
    #number of test cases
    t = int(sys.stdin.readline())
    for i in range(t):
        #input of graph
        [n,m] = sys.stdin.readline().split()
        edges = []
        vertices = [i for i in range(int(n))]
        #an edge is characterized by two vertices and a weight
        for j in range(int(m)):
            [u,v,d] = sys.stdin.readline().split()
            edges.append([int(d), int(u)-1, int(v)-1])
            
        weight = kruskal(vertices, edges)
        #return weight
        sys.stdout.write(str(weight))
        if i != t-1:
            sys.stdout.write("\n")

            