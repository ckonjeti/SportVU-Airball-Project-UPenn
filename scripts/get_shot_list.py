import csv
#from collections import defaultdict
#from operator import itemgetter

def get_shot_list(file):
    #opens file
    arr = {}
    with open(file) as f:
        csv_reader = csv.reader(f, delimiter=',')
        #parse through each row of file
        for row in csv_reader:
            #only collect missed shot data
            if (row[10] == 'Missed Shot'):
                if row[1] not in arr.keys():
                    arr[row[1]] = []
                else:
                    pass
                #gets gameID, playerID, game-event-ID, period, minutes, seconds
                temp = arr.get(row[1])
                temp.append([int(row[2]), row[3], row[7], row[8], row[9]])
                arr['00' + row[1]] = temp
        #sort the list
        sorted(arr.items(), key = lambda item: (item[0]))
        for key in arr:
            arr[key].sort()
    return arr
                    
