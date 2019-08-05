from get_airballs import get_airballs
from get_play_by_play_info import get_game_id, get_type_of_shot
import matplotlib.pyplot as plt
import os
import numpy as np

plots_directory = 'C:/Users/Chaitu Konjeti/SportVU_Airball_Project/plots'
play_by_play_directory = 'C:/Users/Chaitu Konjeti/SportVU_Airball_Project/play-by-play'


airball_list = get_airballs('airballs.csv')
game_ids = []
for id in airball_list:
    game_ids.append('00' + id)
def plot_most_common_airball_shots():
    shot_types = {}
    for file in os.listdir(play_by_play_directory):
        temp_game_id = get_game_id(play_by_play_directory + '/' + file)[2:12]
        if temp_game_id in game_ids:
            event_ids = []
            for set in airball_list.get(temp_game_id[2:]):
                event_ids.append([set[0], set[2]])
            for arr in event_ids:
                type_of_shot = get_type_of_shot(play_by_play_directory + '/' + file, arr[0])
                if type_of_shot not in shot_types.keys():
                    shot_types.update({type_of_shot: 1})
                else:
                    shot_types.update({type_of_shot: shot_types[type_of_shot] + 1})
    data = {"x": [], "y": [], "label": []}
    for key, val in shot_types.items():
        data['x'].append(key)
        data['y'].append(val)

    plt.figure(figsize=(50, 40))
    plt.title('Most Common Types of Airballs', fontsize=20)
    plt.xlabel('types', fontsize=15)
    plt.ylabel('# of occurrences', fontsize=15)
    plt.ylim([0, 5000])
    plt.yticks(np.arange(0, 5000, 200))
    plt.bar(data["x"], data["y"])
    plt.savefig(plots_directory + '/plot_types_of_shots.png')
    plt.show()
    #print(shot_types)
    return shot_types

plot_most_common_airball_shots()