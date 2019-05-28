import get_coordinates
import get_shot_list 
from collections import defaultdict
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy.interpolate import *
from scipy.stats import *



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
    xs, ys, zs, times = [], [], [], []
    for key in ball_coord_list:
        for coords, time in ball_coord_list.get(key):
            for arr in coords:
                if (coords[2] > 9):
                    times.append(time)
                    xs.append(coords[0])
                    ys.append(coords[1])
                    zs.append(coords[2])
                else:
                    try:
                        if (len(xs) != 0):
                            print(xs)
                            print('-----------------')
                            print(times)
                            print('-----------------')
                        xy = polyfit(xs, ys, 2)
                        xz = polyfit(xs, zs, 2)
                        yz = polyfit(ys, zs, 2)
                        if (xy > .75 and xz > .75 and yz > .75):
                            #print(xy, xz, yz)
                            airball_arr.append(times[0])
                        xs.clear()
                        ys.clear()
                        zs.clear()
                        times.clear()
                    except:
                        pass
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    ax.scatter(xs, ys, zs)
    plt.ylim(0, 13)
    
    plt.show()
    print(airball_arr)
    
def polyfit(x, y, degree):
    try:
        results = {}
    
        coeffs = np.polyfit(x, y, degree)
    
         # Polynomial Coefficients
        results['polynomial'] = coeffs.tolist()
    
        # r-squared
        p = np.poly1d(coeffs)
        # fit values, and mean
        yhat = p(x)                         # or [p(z) for z in x]
        ybar = np.sum(y)/len(y)          # or sum(y)/len(y)
        ssreg = np.sum((yhat-ybar)**2)   # or sum([ (yihat - ybar)**2 for yihat in yhat])
        sstot = np.sum((y - ybar)**2)    # or sum([ (yi - ybar)**2 for yi in y])
        results['determination'] = ssreg / sstot
    
        return results['determination']
    except: 
        pass

detect_airballs(player_coordinates, shot_list, airball_arr, '21500493')