# -*- coding: utf-8 -*-
"""
Created on Mon May 20 13:32:21 2019

@author: Chaitu Konjeti
"""

import json
from collections import defaultdict


#opens game file
with open ("game.json") as f:
    data = json.load(f)
    
#enters event section of file
events = data["events"]

#gets coordinates for specified player and appends to playerCoordinates dictionary
def get_coordinates(arr):

    for x in range (0, len(events)) :
        
        visitors = []
        home = []
        
        for a in range (0, len(events[x]['visitor']['players'])):
            visitors.append(events[x]['visitor']['players'][a])
            
        for b in range (0, len(events[x]['home']['players'])):
            home.append(events[x]['home']['players'][b])
            
        for c in range(0, len(visitors)):
            if visitors[c]['playerid'] in arr.keys():
                pass
            else:
                arr[visitors[c]['playerid']] = []
                
        for d in range(0, len(home)):
            if home[d]['playerid'] in arr.keys():
                pass
            else:
                arr[home[d]['playerid']] = []
                
        try:
            for r in range(len(events[x]['moments'])):
                coords = events[x]['moments'][r][5]
                time = events[x]['moments'][r][2]
                for j in range (0, len(coords)):
                    playerID = coords[j][1]
                    temp = [coords[j][2:], time]
                    arr[playerID].append(temp)
        except:
            pass
    

playerCoordinates = defaultdict(list)

get_coordinates(playerCoordinates)

playerIDs = playerCoordinates.keys()

