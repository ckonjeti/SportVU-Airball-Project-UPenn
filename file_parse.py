# -*- coding: utf-8 -*-
"""
Created on Mon May 20 13:32:21 2019

@author: Chaitu Konjeti
"""

import json


#opens game file
with open ("game.json") as f:
    data = json.load(f)
    
#enters event section of file
events = data["events"]

#gets coordinates for specified player and appends to playerCoordinates list
def get_coordinates(playerNum, arr):
    temp = []
    for x in range (0, len(events)) :
        #print(x)
        try:
            players = events[x]['moments'][0][5]
            for element in players:
                temp.append(players[playerNum])
            arr.append(temp)
        except:
            pass
    


playerCoordinates = []


for i in range (0, len(events[0]['moments'][0][5])):
    get_coordinates(i, playerCoordinates)
    
