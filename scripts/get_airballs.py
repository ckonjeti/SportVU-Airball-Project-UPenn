import csv
from collections import defaultdict

airball_list = defaultdict(list)

def get_airballs(file):
    arr = defaultdict(list)
    with open(file) as f:
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:
            temp = arr[row[0]]
            temp.append([row[1], row[2], str(row[3]) + ' ' +  str(row[4])])
            arr[row[0]] = temp
    return arr

