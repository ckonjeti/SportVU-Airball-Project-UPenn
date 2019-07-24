import matplotlib.pyplot as plt
import get_events_after_5_mins
import get_all_events_before_airball
from get_airballs import get_airballs
import os
from get_plays import get_period, get_time_remaining_at_eventid, get_game_id
from collections import defaultdict


plots_directory = 'C:/Users/Chaitu Konjeti/SportVU_Airball_Project/plots'
play_by_play_directory = 'C:/Users/Chaitu Konjeti/SportVU_Airball_Project/play-by-play'

airball_list = defaultdict(list)
get_airballs('airballs.csv', airball_list)
#print(airball_list)
def plot_points(val, events_after_5):
    plt.bar(range(len(val)), list(val), align='center')
    plt.xticks(range(len(val)), list(events_after_5.get(key).keys()))
    plt.yticks(range(1,10))
    plt.show()
# # for python 2.x:
# plt.bar(range(len(D)), D.values(), align='center')  # python 2.x
# plt.xticks(range(len(D)), D.keys())  # in python 2.x







def plot_after_airball(date, events_after_5, period, time_remaining):
    for key, val in events_after_5.items():
        data = {"x":[], "y":[], "label":[]}
        data['label'].append(key)
        #print(key, val)
        for key, val in val.items():
            #print(key,val)
            data['x'].append(key)
            data['y'].append(val)
        #print(data['label'])
        plt.figure(figsize=(20,15))
        plt.title(data['label'][0] + ': Events after Airball at Period ' + period + ' with ' + time_remaining + ' Time Remaining', fontsize=20)
        plt.xlabel('events', fontsize=15)
        plt.ylabel('# of occurrences', fontsize=15)
        plt.bar(data["x"], data["y"])
        #plt.savefig(plots_directory + '/' + data['label'][0] + '_' + date + '_Events_After_Airball.png')
        plt.close()
        data = data.fromkeys(data, [])

def plot_before_airball(date, events_before, period, time_remaining):
    for key, val in events_before.items():
        data = {"x":[], "y":[], "label":[]}
        data['label'].append(key)
        #print(key, val)
        for key, val in val.items():
            #print(key,val)
            data['x'].append(key)
            data['y'].append(val)
        #print(data)
        plt.figure(figsize=(20,15))
        plt.title(data['label'][0] + ': Events before Airball at Period ' + period + ' with ' + time_remaining + ' Time Remaining', fontsize=20)
        plt.xlabel('events', fontsize=15)
        plt.ylabel('# of occurrences', fontsize=15)
        plt.bar(data["x"], data["y"])
        #plt.savefig(plots_directory + '/' + data['label'][0] +  '_' +  date + '_Events_Before_Airball.png')
        plt.close()
        data = data.fromkeys(data, [])

count = 0
for file in os.listdir(play_by_play_directory):
    try:
        print(file)
        id = get_game_id(play_by_play_directory + '/' + file)
        id = id[2:12]
        eventid = airball_list.get(id[2:])[0][0]
        period = get_period(play_by_play_directory + '/' + file, eventid)
        time_remaining = get_time_remaining_at_eventid(play_by_play_directory + '/' + file, eventid)
        events_after_5 = get_events_after_5_mins.output_list_for_5_mins_after_airball(file)
        events_before = get_all_events_before_airball.output_list_for_before_airball(file)
        date = file[1:11]
        print('date', date)
        print(events_after_5)
        plot_after_airball(date, events_after_5, period, time_remaining)
        plot_before_airball(date, events_before, period, time_remaining)
    except:
        continue


