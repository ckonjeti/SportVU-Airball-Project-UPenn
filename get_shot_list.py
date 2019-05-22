import csv
#from collections import defaultdict
#from operator import itemgetter

def get_shot_list(file, arr):
    with open(file) as f:
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:
            if (row[10] == 'Missed Shot'):
                if row[1] not in arr.keys():
                    arr[row[1]] = []
                else:
                    pass
                temp = arr.get(row[1])
                temp.append([int(row[2]), row[3]])
                arr[row[1]] = temp
               
                    

shot_list = {}

get_shot_list('shots.csv', shot_list)

sorted(shot_list.items(), key = lambda item: (item[0]))

for key in shot_list:
    shot_list[key].sort()

#print(shot_list)
