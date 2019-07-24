import matplotlib.pyplot as plt
import get_events_after_5_mins
import get_all_events_before_airball

plots_directory = 'C:/Users/Chaitu Konjeti/SportVU_Airball_Project/plots'


def plot_points(val, events_after_5):
    plt.bar(range(len(val)), list(val), align='center')
    plt.xticks(range(len(val)), list(events_after_5.get(key).keys()))
    plt.yticks(range(1,10))
    plt.show()
# # for python 2.x:
# plt.bar(range(len(D)), D.values(), align='center')  # python 2.x
# plt.xticks(range(len(D)), D.keys())  # in python 2.x


events_after_5 = get_events_after_5_mins.output_list_for_5_mins_after_airball('[2013-10-29]-0021300002-CHI@MIA.csv')
events_before = get_all_events_before_airball.output_list_for_5_mins_after_airball('[2013-10-29]-0021300002-CHI@MIA.csv')
print(events_after_5)
print(events_before)
list_nums = []
#print(events_after_5.keys())


for key, val in events_after_5.items():
    data = {"x":[], "y":[], "label":[]}
    data['label'].append(key)
    #print(key, val)
    for key, val in val.items():
        #print(key,val)
        data['x'].append(key)
        data['y'].append(val)
    #print(data['label'])
    plt.figure(figsize=(10,8))
    plt.title(data['label'][0] + ': Events after Airball', fontsize=20)
    plt.xlabel('events', fontsize=15)
    plt.ylabel('# of occurrences', fontsize=15)
    plt.bar(data["x"], data["y"])
    plt.savefig(plots_directory + '/' + data['label'][0] + '_Events_After_Airball.png')
    #plt.show()

    data = data.fromkeys(data, [])

for key, val in events_before.items():
    data = {"x":[], "y":[], "label":[]}
    data['label'].append(key)
    #print(key, val)
    for key, val in val.items():
        #print(key,val)
        data['x'].append(key)
        data['y'].append(val)
    #print(data)
    plt.figure(figsize=(10,8))
    plt.title(data['label'][0] + ': Events before Airball', fontsize=20)
    plt.xlabel('events', fontsize=15)
    plt.ylabel('# of occurrences', fontsize=15)
    plt.bar(data["x"], data["y"])
    plt.savefig(plots_directory + '/' + data['label'][0] + '_Events_Before_Airball.png')
    #plt.show()

    data = data.fromkeys(data, [])

