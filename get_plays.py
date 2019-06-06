# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:44:38 2019

@author: Chaitu Konjeti
"""

import csv
from collections import defaultdict

arr = []

#[rebound, player, rebound type, period, time remaining]
def get_rebounds(file, arr):
    with open(file) as f:
        csv_reader = csv.reader(f, delimiter=',')
        #parse through each row of file
        for row in csv_reader:
            if row[21] == 'rebound':
                temp = [row[21], row[31], row[37], row[13], row[16]]
                arr.append(temp)
        print(arr)
            
#[assist player, shot player, period, time remaining]
def get_assists(file, arr):
    with open(file) as f:
        csv_reader = csv.reader(f, delimiter=',')
        #parse through each row of file
        for row in csv_reader:
            if row[22] != '':
                temp = [row[22], row[31], row[13], row[16]]
                arr.append(temp)
        print(arr)
        
#[foul, foul player, reason for foul, period, time remaining]
def get_fouls(file, arr):
    with open(file) as f:
        csv_reader = csv.reader(f, delimiter=',')
        #parse through each row of file
        for row in csv_reader:
            if row[21] == 'foul':
                temp = [row[21], row[31], row[34], row[13], row[16]]
                arr.append(temp)
        print(arr)
        
#[turnover, turnover player, reason for turnover, period, time remaining]
def get_turnovers(file, arr):
    with open(file) as f:
        csv_reader = csv.reader(f, delimiter=',')
        #parse through each row of file
        for row in csv_reader:
            if row[21] == 'turnover':
                temp = [row[21], row[31], row[34], row[13], row[16]]
                arr.append(temp)
        print(arr)
        
#[free throw, player, made or missed, period, time remaining]
def get_freethrows(file, arr):
    with open(file) as f:
        csv_reader = csv.reader(f, delimiter=',')
        #parse through each row of file
        for row in csv_reader:
            if row[21] == 'free throw':
                temp = [row[21], row[31], row[35], row[13], row[16]]
                arr.append(temp)
        print(arr)
        
get_freethrows('stats.csv', [])

    