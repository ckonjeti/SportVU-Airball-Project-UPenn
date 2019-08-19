import json
from collections import defaultdict

#Array: {playerID: {game-event-ID: [coordinates, time]}}

#gets coordinates for specified player and appends to specified defaultdict(dict)
def get_coordinates(file, arr):
    
    #opens game file
    with open(file) as f:
        data = json.load(f)
        
    #enters event section of file
    events = data["events"]
    for x in range (0, len(events)):
        
        visitors = []
        home = []
        
        #gets playerIDs for the keys for dict
        for a in range (0, len(events[x]['visitor']['players'])):
            visitors.append(events[x]['visitor']['players'][a])
            
        for b in range (0, len(events[x]['home']['players'])):
            home.append(events[x]['home']['players'][b])
        
        #creates empty dictionary for key if key does not exist
        for c in range(0, len(visitors)):
            if visitors[c]['playerid'] in arr.keys():
                pass
            else:
                arr[visitors[c]['playerid']] = {}
                
        for d in range(0, len(home)):
            if home[d]['playerid'] in arr.keys():
                pass
            else:
                arr[home[d]['playerid']] = {}
        #appends a list containing the coordinates and time to corresponding playerID key
        try:
            for r in range(len(events[x]['moments'])):
                coords = events[x]['moments'][r][5]
                time = events[x]['moments'][r][2]
                for j in range (0, len(coords)):
                    temp = defaultdict(list)
                    playerID = coords[j][1]
                    
                    if events[x]['eventId'] in arr[playerID].keys():
                        pass
                    else:
                        temp = []
                        
                    if events[x]['eventId'] not in arr[playerID].keys():
                        temp = [[coords[j][2:], time]]
                    else:
                        temp = arr[playerID][events[x]['eventId']];
                        temp.append([coords[j][2:], time])
                        
                        
                    arr[playerID][events[x]['eventId']] = temp
        except:
            pass
        
        
def main(file, arr):
    get_coordinates(file, arr)
