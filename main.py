from get_airballs import get_airballs
from get_plays import get_rebounds, get_assists, get_fouls, get_freethrows, get_turnovers, get_game_id
import os
from collections import defaultdict

main_directory = 'C:/Users/Chaitu Konjeti/SportVU_Airball_Project'
play_by_play_directory = 'C:/Users/Chaitu Konjeti/SportVU_Airball_Project/play-by-play'

airball_list = defaultdict(list)
get_airballs('airballs.csv', airball_list)



game_ids = []
for id in airball_list:
    game_ids.append('00'+id)

for filename in os.listdir(play_by_play_directory):
    temp_game_id = get_game_id(play_by_play_directory + '/' + filename,)[2:12]
    if temp_game_id in game_ids:
        rebounds = get_rebounds(play_by_play_directory + '/' + filename, [])
        assists = get_assists(play_by_play_directory + '/' + filename, [])
        fouls = get_fouls(play_by_play_directory + '/' + filename, [])
        turnovers = get_turnovers(play_by_play_directory + '/' + filename, [])
        freethrows = get_freethrows(play_by_play_directory + '/' + filename, [])

        event_ids = []

        for arr in airball_list.get(temp_game_id):
            event_ids.append(arr)


