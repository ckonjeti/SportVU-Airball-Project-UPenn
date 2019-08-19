import os
from get_events_after_5_mins import get_events_after_5_mins
from get_events_before_5_mins import get_events_before_5_mins
import matplotlib.pyplot as plt
from get_airballs import get_airballs
from get_play_by_play_info import get_game_id
import numpy as np


play_by_play_directory = 'C:/Users/Chaitu Konjeti/SportVU_Airball_Project/play-by-play'
plots_directory = 'C:/Users/Chaitu Konjeti/SportVU_Airball_Project/percentage_plots'

def get_percentage_of_events_after_airball(play_by_play_directory):
    total_num_of_airballs = 0
    event_totals = {'assist': 0, 'rebound': 0, 'free throw': 0, 'foul': 0, 'shot': 0, 'turnover': 0, 'sub': 0, 'miss': 0, 'violation': 0, 'nothing': 0, 'end of period': 0, 'jump ball': 0, 'start of period': 0, 'timeout': 0, 'unknown': 0}
    event_bools = event_totals.fromkeys(event_totals, False)
    event_percentages = event_bools.fromkeys(event_bools, 0)
    airball_list = get_airballs('airballs.csv')
    game_ids = []
    for id in airball_list:
        game_ids.append('00' + id)
    #print(airball_list)
    count = 0
    for file in os.listdir(play_by_play_directory):
        #print('game ', file)
        temp_game_id = get_game_id(play_by_play_directory + '/' + file)[2:12]
        events_for_game = get_events_after_5_mins(file, airball_list, game_ids, play_by_play_directory)
        #print(events_for_game)
        if temp_game_id in game_ids:
            #print('yes')
            try:
                for outer_arr in events_for_game:
                    total_num_of_airballs += 1
                    for arr in outer_arr:
                        event = arr[1]
                        #print(arr[5])
                        if event_bools.get(event) == False:
                            event_bools.update({event: True})
                        elif arr[8] != '':
                            #print(arr[8])
                            event_bools.update({'assist': True})

                #print(event_bools)
                for key in event_bools:
                    if event_bools.get(key) == True:
                        event_totals[key] += 1
                if True not in event_bools.values():
                    event_totals['nothing'] += 1
                event_bools = event_bools.fromkeys(event_bools, False)
                #print(event_totals)

            except:
                continue
    for key in event_totals:
        event_percentages.update({key: float(event_totals.get(key)/total_num_of_airballs)})
    return event_percentages

def plot_event_percentages_for_after():
    event_percentages = get_percentage_of_events_after_airball(play_by_play_directory)
    data = {"x": [], "y": [], "label": []}
    for key, val in event_percentages.items():
        data['x'].append(key)
        data['y'].append(val)

    plt.figure(figsize=(20, 15))
    plt.title('Percentage of Events Happening After a Player Shoots an Airball (5 Minutes After)', fontsize=20)
    plt.xlabel('events', fontsize=15)
    plt.ylabel('percentage', fontsize=15)
    plt.ylim([0, 1])
    plt.yticks(np.arange(0, 1, .05))
    plt.bar(data["x"], data["y"])
    plt.savefig(plots_directory + '/plot_5_minute_after.png')
    plt.show()

def get_percentage_of_events_before_airball(play_by_play_directory):
    total_num_of_airballs = 0
    event_totals = {'assist': 0, 'rebound': 0, 'free throw': 0, 'foul': 0, 'shot': 0, 'turnover': 0, 'sub': 0, 'miss': 0, 'violation': 0, 'nothing': 0, 'end of period': 0, 'jump ball': 0, 'start of period': 0, 'timeout': 0, 'unknown': 0}
    event_bools = event_totals.fromkeys(event_totals, False)
    event_percentages = event_bools.fromkeys(event_bools, 0)
    airball_list = get_airballs('airballs.csv')
    game_ids = []
    for id in airball_list:
        game_ids.append('00' + id)
    #print(airball_list)
    count = 0
    for file in os.listdir(play_by_play_directory):
        #print('game ', file)
        temp_game_id = get_game_id(play_by_play_directory + '/' + file)[2:12]
        events_for_game = get_events_before_5_mins(file, airball_list, game_ids, play_by_play_directory)
        #print(events_for_game)
        if temp_game_id in game_ids:
            #print('yes')
            try:
                for outer_arr in events_for_game:
                    total_num_of_airballs += 1
                    for arr in outer_arr:
                        event = arr[1]
                        #print(arr[5])
                        if event_bools.get(event) == False:
                            event_bools.update({event: True})
                        elif arr[8] != '':
                            #print(arr[8])
                            event_bools.update({'assist': True})

                #print(event_bools)
                for key in event_bools:
                    if event_bools.get(key) == True:
                        event_totals[key] += 1
                if True not in event_bools.values():
                    event_totals['nothing'] += 1
                event_bools = event_bools.fromkeys(event_bools, False)
                #print(event_totals)

            except:
                continue
    for key in event_totals:
        event_percentages.update({key: float(event_totals.get(key)/total_num_of_airballs)})
    return event_percentages

def plot_event_percentages_for_before():
    event_percentages = get_percentage_of_events_before_airball(play_by_play_directory)
    data = {"x": [], "y": [], "label": []}
    for key, val in event_percentages.items():
        data['x'].append(key)
        data['y'].append(val)

    plt.figure(figsize=(20, 15))
    plt.title('Percentage of Events Happening Before a Player Shoots an Airball (5 Minutes Before)', fontsize=20)
    plt.xlabel('events', fontsize=15)
    plt.ylabel('percentage', fontsize=15)
    plt.ylim([0, 1])
    plt.yticks(np.arange(0, 1, .05))
    plt.bar(data["x"], data["y"])
    plt.savefig(plots_directory + '/plot_5_minute_before.png')
    plt.show()


plot_event_percentages_for_after()
plot_event_percentages_for_before()