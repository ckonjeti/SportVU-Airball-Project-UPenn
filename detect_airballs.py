import get_coordinates
import get_shot_list 
from collections import defaultdict


player_coordinates = defaultdict(dict) #(playerID: game event id: [coordinates, time])

get_coordinates.main('game.json', player_coordinates)

shot_list = {}

get_shot_list.main('shots.csv', shot_list)

airball_arr = []



def detect_airballs(coord_arr, shot_arr, airball_arr, gameID):
    game_event_list = []
    for key in shot_arr:
        if key == gameID:
            for shot in shot_arr.get(str(key)):
                game_event_list.append(str(shot[0]))
    ball_coord_list = {}
    ball_coords = coord_arr.get(-1)
    for event in game_event_list:
        if event in ball_coords.keys():
            ball_coord_list[event] = (list(coord_arr.get(-1).get(event)))
            
    
detect_airballs(player_coordinates, shot_list, airball_arr, '21500493')