# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 11:13:23 2022

@author: laurin
"""

from sys import stdin, stdout

def auction(rows, first):
    min_price = []
    max_offer = []
    minp = 0
    maxo = 0
    min_index = 0
    max_index = 0
    
    for k in range(rows):
        input_stuff = stdin.readline().split()
        offer = [int(input_stuff[1]), input_stuff[0]]
        #print(f'max_offer: {max_offer}')
        #print(max_index)
        #print(maxo)
        #print(f'min_price: {min_price}')
        #print(min_index)
        #print(minp)
        if offer[0] < 0:
            if -offer[0]>=minp and minp != 0:
                if not first:
                    stdout.write("\n")
                stdout.write(f'{min_price[min_index][1]},{offer[1]},{minp}')
                del min_price[min_index]
                first = False
                if len(min_price) != 0:
                    tmp = min_price[0][0]
                    min_index = 0
                    for index in range(len(min_price)):
                        if min_price[index][0] < tmp:
                            min_index = index
                            tmp = min_price[index][0]
                    minp = tmp
                else:
                    minp = 0                    
                continue
            
            max_offer.append(offer)
            if offer[0]<maxo:
                max_index = len(max_offer)-1
                maxo = max_offer[max_index][0]
                
        else:
            if -maxo>=offer[0]:
                if not first:
                    stdout.write("\n")
                stdout.write(f'{offer[1]},{max_offer[max_index][1]},{offer[0]}')
                del max_offer[max_index]
                first = False
                if len(max_offer) != 0:
                    tmp = max_offer[0][0]
                    max_index = 0
                    for index in range(len(max_offer)):
                        if max_offer[index][0] < tmp:
                            max_index = index
                            tmp = max_offer[index][0]
                    maxo = tmp
                else:
                    maxo = 0              
                continue
            
            min_price.append(offer)
            if len(min_price) == 1:
                minp = min_price[0][0]
                min_index = 0
            elif offer[0] < minp:
                min_index = len(min_price)-1
                minp = min_price[min_index][0]

if __name__ == '__main__':
    tests = int(input())
    #number of test cases
    for i in range(tests):
        rows = int(input())
        auction(rows, i==0)
        