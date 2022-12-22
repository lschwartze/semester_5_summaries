# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 08:51:41 2022

@author: laurin
"""
import sys

#find shortest path using breadth first search -> Edmonds-Karp
def BFS(A, parent):
    s = 0
    n = len(A)
    t = n-1
    #remember nodes that have been visited -> color
    visited = [0]*n
    q = [s]
    visited[s] = 1
    
    #remove first element of queue and consider its neighbourhood
    while len(q) > 0:
        v = q.pop(0)
        row = A[v]
        for i in range(n):
            #if the node was not visited and an edge exists
            if visited[i] == 0 and row[i] > 0:
                #add to quere
                q.append(i)
                visited[i] = 1
                #adjust parent array
                parent[i] = v
                #if sink has been reached, return path
                if i == t:
                    return True, parent
    return False, parent

#Ford Fulkerson algorithm from source 0 to sink n-1
def fordfulkerson(A):
    n = len(A)
    t = n-1
    #memorize parents to search for a shortest path
    parent = [-1]*n
    flow = 0
    #breadth first search to find an augmenting path from s to t 
    bfs = BFS(A, parent)
    parent = bfs[1]
    #if such path exists
    while bfs[0]:
        path_flow = float("Inf")
        p = t
        #path is stored in parent array
        #walk path backwards to find the lowest capacity which is the flow of this path
        while(p != 0):
            path_flow = min(path_flow, A[parent[p]][p])
            p = parent[p]  
            
        #augmenting path increases current flow
        flow += path_flow
        v = t
        #walk path backwards again to change capacity of residual graph
        while v != 0:
            u = parent[v]
            A[u][v] -= path_flow
            A[v][u] += path_flow
            v = parent[v]
        #search for another augmenting path
        bfs = BFS(A, parent)
        parent = bfs[1]
    
    return flow
        

if __name__ == '__main__':
    #number of test cases
    t = int(sys.stdin.readline())
    for i in range(t):
        [G,K] = sys.stdin.readline().split()
        #create incidence matrix with source and sink
        #the vertex set is: source, one node per kid, one node per present, sink
        n = (int(G)+int(K)+2)
        A = [[0 for j in range(n)] for k in range(n)] 
        for j in range(int(K)):
            #from the source there is an edge with capacity 2 to each kid
            A[0][j+1] = 2
        amount = sys.stdin.readline().split()
        for j in range(int(G)):
            #there's a fixed amount of each individual present which is the capacity to the sink
            A[int(K)+1+j][n-1] = int(amount[j])
        for k in range(int(K)):
            kid = sys.stdin.readline().split()
            w = int(kid[1])
            #from each kid there is an edge of capacity 1 to each present on its wishlist
            presents = kid[2:]
            for l in range(w):
                A[k+1][int(K)+int(presents[l])] = 1
        #every child needs to recieve two presents, therefore maxflow needs to be 2*K
        if fordfulkerson(A) == 2*int(K):
            print(1)
        else:
            print(0)
        