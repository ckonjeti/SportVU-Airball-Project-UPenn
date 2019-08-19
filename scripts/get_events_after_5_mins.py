from get_airballs import get_airballs
from get_play_by_play_info import get_rebounds, get_assists, get_fouls, get_freethrows, get_turnovers, get_game_id, get_time_remaining_at_eventid, get_plays_within_times, get_period
import os
from collections import defaultdict

main_directory = 'C:/Users/Chaitu Konjeti/SportVU_Airball_Project'
play_by_play_directory = 'C:/Users/Chaitu Konjeti/SportVU_Airball_Project/play-by-play'


airball_list = get_airballs('airballs.csv')

game_ids = []
for id in airball_list:
    game_ids.append('00' + id)

def get_events_after_5_mins(filename, airball_list, game_ids, play_by_play_directory):
    list_of_lists = []
    count = 0
    temp_game_id = get_game_id(play_by_play_directory + '/' + filename,)[2:12]
    if temp_game_id in game_ids:
        event_ids = []
        for set in airball_list.get(temp_game_id[2:]):
            event_ids.append([set[0], set[2]])

        for arr in event_ids:
            period = get_period(play_by_play_directory + '/' + filename, arr[0])
            time_remaining = get_time_remaining_at_eventid(play_by_play_directory + '/' + filename, arr[0])

            try:
                edited_time = time_remaining[3:]
                begin_time = int(edited_time[0:2])
                if begin_time > 5:
                    end_time = begin_time - 5
                    final_time = '00:0' + str(end_time) + ':' + edited_time[3:]
                    list_of_plays = get_plays_within_times(play_by_play_directory + '/' + filename, arr[1], time_remaining, final_time, period, [])
                    list_of_lists.append(list_of_plays)
                    #print(list_of_plays)
                    count += 1
                else:
                    list_of_plays = get_plays_within_times(play_by_play_directory + '/' + filename, arr[1], time_remaining, "00:00:01", period, [])
                    list_of_lists.append(list_of_plays)
                    #print(list_of_plays)
                    count += 1
            except:
                continue
        event_ids.clear()
    return list_of_lists

    #print('count ', count)

def output_list_for_5_mins_after_airball(filename):

    list = get_events_after_5_mins(filename,airball_list, game_ids, play_by_play_directory)

    dict_of_nums = {}

    dict = {}

    for arr in list:
        for val in arr:
            if val[0] in dict.keys():
                old = dict.get(val[0])
                old += [val[1]]
                dict[val[0]] = old
            else:
                dict[val[0]] = [val[1]]

    counts = {'rebound': 0, 'free throw': 0, 'foul': 0, 'shot': 0, 'turnover': 0, 'sub': 0, 'miss': 0, 'violation': 0, 'end of period': 0, 'jump ball': 0, 'start of period': 0, 'timeout': 0, 'unknown': 0}

    for key in dict:
        for val in dict.get(key):
            try:
                #print('val', val)
                #print(counts)
                old = counts.get(val)
                #print(old)
                old += 1
                counts.update({val: old})
            except:
                continue
        dict_of_nums.update({key: counts})
        counts = counts.fromkeys(counts, 0)
    return dict_of_nums

#print(output_list_for_5_mins_after_airball('[2013-10-30]-0021300004-BKN@CLE.csv'))
#print(dict_of_nums)