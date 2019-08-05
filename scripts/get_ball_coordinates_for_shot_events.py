import json
from collections import defaultdict
from get_shot_list import get_shot_list


# Array: {playerID: {game-event-ID: [coordinates, time]}}

# gets coordinates for specified player and appends to specified defaultdict(dict)
def get_ball_coordinates_for_shot_events(file):
    # opens game file
    arr = {}
    with open(file) as f:
        data = json.load(f)
        gameid = data['gameid']
        #print(gameid)
    shot_arr = get_shot_list('shots.csv')
    #print(shot_arr)
    event_list = []

    shots = shot_arr.get(gameid)
    for list in shots:
        event_list.append(list[0])
    #print(event_list)
    # enters event section of file
    events = data["events"]
    #len(events)
    for x in range(0, len(events)):
        if x in event_list:
            #print('here')
            temp = []
            try:
                #len(events[x]['moments'])
                for i in range(0, len(events[x]['moments'])):
                    ball_coords = events[x]['moments'][i][5][0]
                    time = events[x]['moments'][i][2]
                    shot_clock = events[x]['moments'][i][3]
                    #print('here')
                    temp.append([ball_coords, time, shot_clock])
                    #print(temp)
                arr[x] = temp
            except:
                pass
    return arr

