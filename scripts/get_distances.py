import get_coordinates
from collections import defaultdict
from scipy.spatial import distance
import matplotlib.patches as patches 
from matplotlib import animation
import matplotlib.pyplot as plt

player_coordinates = defaultdict(dict) #(playerID: game event id: [coordinates, time])

get_coordinates.main('game.json', player_coordinates)

distance_arr = defaultdict(list)

def get_distances(distance_arr, player_coordinates):
    for playerID in player_coordinates:
        dist = 0
        dist_arr = []
        for gameID in player_coordinates.get(playerID):
            coords = player_coordinates.get(playerID).get(gameID)
            for coord, time in coords:
                dist += distance.euclidean(coord[0], coord[1])
                dist_arr.append(dist)
        if playerID != -1:
            distance_arr[playerID] = dist_arr
    #print(distance_arr)
    #for playerID in distance_arr:
    plt.plot(distance_arr.items())
    plt.ylabel('Distance traveled')
    plt.show()

        
get_distances(distance_arr, player_coordinates)