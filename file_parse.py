# -*- coding: utf-8 -*-
"""
Created on Mon May 20 13:32:21 2019

@author: Chaitu Konjeti
"""

import json

with open ("game.json") as f:
    data = json.load(f)
    
events = data["events"]

#prints the times
for x in range (0, 453) :
    players = events[x]['moments']
    
    for element in players:
        print('time: ' + str(element[2]))

    
