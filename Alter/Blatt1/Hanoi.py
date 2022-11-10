# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 19:48:37 2022

@author: laurin
"""
import sys

def solve_position(n, k, posts, start, via, goal):
    #if no moves were done, return current state
    if k == 0:
        return posts
    #if exactly 2^n-1 moves were done, the puzzle is solved
    elif k == 2**n-1:
        posts[goal] = posts[start]
        posts[start] = []
        return posts
    #it takes 2^(n-1)-1 moves to transport a heap of size n-1
    elif k >= 2**(n-1)-1:
        disks = len(posts[start])-(n-1)
        buf = posts[start][disks:]
        posts[start] = posts[start][:disks]
        posts[via] = posts[via] + buf
        #if this heap has be transported, reduce the number of moves left
        k = k - (2**(n-1)-1)
        #next, the largest disk from the start pole would have to be 
        #transported to the goal pole, therefore, check if another move was done
        if k !=0:
            buf = posts[start][-1]
            posts[start] = posts[start][:-1]
            posts[goal].append(buf)
            #the move the n-1 heap back to the goal pole
            return solve_position(n-1, k-1, posts, via, start, goal)
        return posts
    #if the n-1 heap can not be transported, try again with n-2
    else:
        return solve_position(n-1, k, posts, start, goal, via)
        

if __name__ == '__main__':
    m = int(input())
    #number of test cases
    for i in range(m):
        input_stuff = sys.stdin.readline().split()
        n = int(input_stuff[0])
        k = int(input_stuff[1])
        #every testcase consists of n, the number of disks and k, 
        #the number of moves
        
        posts = [list(range(n,0,-1)), [], []]
        #a list from n down to 1 lies on pole 1, empty lists else
        start = 0
        via = 2
        goal = 1
        
        res = solve_position(n, k, posts, start, via, goal)
        #print result to output txt file
        for i in range(3):
            pole = "|".join(map(str, res[i]))
            print(f'{i+1}: {pole}')