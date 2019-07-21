from get_airballs import get_airballs
from get_plays import get_rebounds, get_assists, get_fouls, get_freethrows, get_turnovers, get_game_id, get_time_remaining_at_eventid, get_plays_within_times, get_period
import os
from collections import defaultdict

main_directory = 'C:/Users/Chaitu Konjeti/SportVU_Airball_Project'
play_by_play_directory = 'C:/Users/Chaitu Konjeti/SportVU_Airball_Project/play-by-play'

airball_list = defaultdict(list)
get_airballs('airballs.csv', airball_list)

game_ids = []
for id in airball_list:
    game_ids.append('00'+id)

count = 0
for filename in os.listdir(play_by_play_directory):
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
                    list_of_plays = get_plays_within_times(play_by_play_directory + '/' + filename, arr[1], time_remaining, final_time, period, {})
                    print(list_of_plays)
                    count += 1
                else:
                    list_of_plays = get_plays_within_times(play_by_play_directory + '/' + filename, arr[1], time_remaining, "00:00:01", period, {})
                    print(list_of_plays)
                    count += 1
            except:
                continue
        event_ids.clear()

print('count ', count)

'''
rebounds = get_rebounds(play_by_play_directory + '/' + filename, [])
        assists = get_assists(play_by_play_directory + '/' + filename, [])
        fouls = get_fouls(play_by_play_directory + '/' + filename, [])
        turnovers = get_turnovers(play_by_play_directory + '/' + filename, [])
        freethrows = get_freethrows(play_by_play_directory + '/' + filename, [])
'''