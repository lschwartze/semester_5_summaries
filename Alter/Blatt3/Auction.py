# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 11:13:23 2022

@author: laurin
"""

import sys
import bisect

def auction(rows):
    min_price = []
    max_offer = []
    minp = 0
    maxo = 0
    
    for k in range(rows):
        input_stuff = sys.stdin.readline().split()
        offer = [int(input_stuff[1]), input_stuff[0]]

        if offer[0] < 0:
            if -offer[0]>=minp and minp != 0:
                print(f'{min_price[0][1]},{offer[1]},{minp}')
                del min_price[0]
                
                if len(min_price) != 0:
                    minp = min_price[0][0]
                else:
                    minp = 0                    
                continue     
            
            bisect.insort(max_offer, offer)
            maxo = max_offer[0][0]
        else:
            if -maxo>=offer[0]:
                print(f'{offer[1]},{max_offer[0][1]},{offer[0]}')
                del max_offer[0]
                
                if len(max_offer) != 0:
                    maxo = max_offer[0][0]
                else:
                    maxo = 0              
                continue
            
            bisect.insort(min_price, offer)
            minp = min_price[0][0]

if __name__ == '__main__':
    tests = int(input())
    #number of test cases
    for i in range(tests):
        rows = int(input())
        auction(rows)
        