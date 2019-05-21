import csv
#from operator import itemgetter

def get_shot_list(file, arr):
    with open(file) as f:
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:
            if (row[10] == 'Missed Shot'):
                temp = [row[1], int(row[2]), row[3]]
                arr.append(temp)
        
shot_list = []

get_shot_list('shots.csv', shot_list)

shot_list = sorted(shot_list, key = lambda x: (x[0], x[1]))

print(shot_list[:300])