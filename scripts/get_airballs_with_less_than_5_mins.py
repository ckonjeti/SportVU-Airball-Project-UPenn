from get_play_by_play_info import get_time_remaining_at_eventid, get_game_id
from get_airballs import get_airballs
import os

play_by_play_directory = 'C:/Users/Chaitu Konjeti/SportVU_Airball_Project/play-by-play'



def get_airballs_with_less_than_5_mins(play_by_play_directory):
    count = 0
    airball_list = get_airballs('airballs.csv')
    #print(airball_list)
    game_ids = []
    for id in airball_list:
        game_ids.append('00' + id)
    #print(game_ids)
    for file in os.listdir(play_by_play_directory):
        temp_game_id = get_game_id(play_by_play_directory + '/' + file)[2:12]
        if len(temp_game_id) != 10:
            temp_game_id = '00' + temp_game_id
        #print(temp_game_id)
        if temp_game_id in game_ids:
            #print(temp_game_id)
            event_ids = []
            for set in airball_list.get(temp_game_id[2:]):
                time_remaining = get_time_remaining_at_eventid(play_by_play_directory + '/' + file, set[0])
                #print(time_remaining)
                if (time_remaining < '00:03:00'):
                    #print(temp_game_id, time_remaining)
                    count += 1
    return count






print(get_airballs_with_less_than_5_mins(play_by_play_directory))