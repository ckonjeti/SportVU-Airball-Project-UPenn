import csv
from collections import defaultdict

airball_list = defaultdict(list)

def get_airballs(file, arr):
    with open(file) as f:
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:
            temp = airball_list[row[0]]
            temp.append([row[1], row[2]])
            airball_list[row[0]] = temp

#get_airballs('airballs.csv', airball_list)
            