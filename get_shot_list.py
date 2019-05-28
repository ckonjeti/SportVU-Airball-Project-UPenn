import csv
#from collections import defaultdict
#from operator import itemgetter

def get_shot_list(file, arr):
    #opens file
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
                #gets gameID, playerID, and game-event-ID
                temp = arr.get(row[1])
                temp.append([int(row[2]), row[3]])
                arr[row[1]] = temp
        #sort the list
        sorted(arr.items(), key = lambda item: (item[0]))
        for key in arr:
            arr[key].sort() 
                    

def main(file, arr):
    get_shot_list(file, arr)