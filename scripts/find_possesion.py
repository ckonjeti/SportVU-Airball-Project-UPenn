from collections import defaultdict
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from scipy.spatial import euclidean as dist
import get_coordinates
import get_shot_list

player_coordinates = defaultdict(dict) #(playerID: game event id: [coordinates, time])

get_coordinates.main('game.json', player_coordinates)

shot_list = {}

get_shot_list.main('shots.csv', shot_list)

airball_arr = []

possesion = []
ballCoordinates = player_coordinates.get(-1)

#print(player_coordinates.get(-1).keys())

for key in player_coordinates:
        for keys in (player_coordinates.get(key)):
            if keys in player_coordinates.get(-1).keys():
                print(keys)
            #print("hi")
