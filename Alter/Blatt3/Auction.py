# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 08:51:17 2022

@author: laurin
"""

import sys

#decides whether a trade is possible
def auction(rows):
    #keep track of current bids
    trades = []
    for j in range(rows):
        input_stuff = sys.stdin.readline().split()
        input_stuff = [input_stuff[0], int(input_stuff[1])]
        
        #if a new number is a bid to buy
        if input_stuff[1] < 0:
            #append this new bid
            trades.append(input_stuff)
            #check if there was a seller who would agree to this price
            for idx in range(len(trades)):
                trader = trades[idx][0]
                price = trades[idx][1]
                #ignore other bidders
                if price < 0:
                    continue
                #this person agrees to the price
                if (-1)*input_stuff[1] >= price:
                    print(f'{trader},{input_stuff[0]},{price}')
                    #delete perso who sold
                    del trades[idx]
                    #delete the last element, who just bought
                    del trades[-1]
                    break
        
        #if the new offer is a price to sell   
        else:
            #keep track of possible buyers
            poss_buyers = []
            for idx in range(len(trades)):
                price = trades[idx][1]
                #ignore other sellers
                if price > 0:
                    continue
                #if a buyer agrees, store in possible buyers
                if input_stuff[1] <= (-1)*price:
                    #also keep track of the index to delete later on
                    poss_buyers.append([*trades[idx],idx])
                
            #check whether anybody agrees to the trade
            if len(poss_buyers) != 0:
                #get the highest bid
                #use min, because bids are stored as negative numbers
                max_price = min(b for [a,b,c] in poss_buyers)
                #get information on person who sells for this price
                for elem in poss_buyers:
                    if elem[1] == max_price:
                        print(f'{input_stuff[0]},{elem[0]},{input_stuff[1]}')
                        #delete trader
                        del trades[elem[2]]
                        break
            #if noone is willing to buy, append new element to open trades
            else:
                trades.append(input_stuff)     

if __name__ == '__main__':
    tests = int(input())
    #number of test cases
    for i in range(tests):
        rows = int(input())
        auction(rows)
            