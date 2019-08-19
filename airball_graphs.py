import matplotlib.pyplot as plt
from get_airballs import get_airballs
import os
from get_plays import get_period, get_time_remaining_at_eventid, get_game_id, get_assists, get_rebounds, get_turnovers, get_fouls
import csv
import time
from collections import defaultdict

startTime = time.time()
airballDictionary = defaultdict(list)
get_airballs("airballs.csv", airballDictionary)

play_by_play_directory = "C:/Users/Taylor Smith/Desktop/Code/SportVU_Airball_Project/play-by-play"

count = 0
x = 0

eventsBefore = []
eventsAfter = []
eventsDictionary = defaultdict(list)

#Add all required events to the event dictionary and initialize their lists
#Key = event type (rebound, sub, shot, etc.) Value = [# of times it happens before, # of times it happens after]
eventsDictionary["p.foul"] = [0, 0]
eventsDictionary["t.foul"] = [0, 0]
eventsDictionary["sub"] = [0, 0]
eventsDictionary["miss"] = [0, 0]
eventsDictionary["shot"] = [0, 0]
eventsDictionary["assist"] = [0, 0]
eventsDictionary["rebound"] = [0, 0]
eventsDictionary["turnover"] = [0, 0]
eventsDictionary["nothing"] = [0, 0]
eventsDictionary["foul"] = [0, 0]

#Minutes to look before and after the airball
minuteRange = 3
print("Minute Range: " + str(minuteRange) + " minute(s)\n")


for file in os.listdir(play_by_play_directory):
    try:
        #If the Keys (gameIDs) in the airballDictionary start with 00 put file[13:15], if they don't start with 00 put file[15:23]
        fileGameID = file[15:23]
        
        #if "21300014" in fileGameID:
        for airball in airballDictionary[fileGameID]:
            #First, find the time remaining and the quarter of the game in which the airball took place
            airballEventID = airball[0]
            airballPlayer = airball[2]
            airballTimeRemaining = get_time_remaining_at_eventid(play_by_play_directory + '/' + file, airballEventID)
            airballSecondsRemaining = int(airballTimeRemaining[3:5]) * 60 + int(airballTimeRemaining[6:])
            airballQuarter = get_period(play_by_play_directory + '/' + file, airballEventID)

            #If the airball took place within the time range specified above, append all events before and after into their respective lists
            if airballSecondsRemaining > minuteRange * 60 and airballSecondsRemaining < (720 - minuteRange * 60):
                with open(play_by_play_directory + '/' + file) as f:
                    csv_reader = csv.reader(f, delimiter=',')
                    for row in csv_reader:                               
                        if row[0] != 'game_id':
                            timeRemaining = row[16]
                            secondsRemaining = (int(timeRemaining[3:5]) * 60 + int(timeRemaining[6:]))
                            
                            #If the event is in the correct time range before the air ball, append the event to the list
                            if (secondsRemaining <= (airballSecondsRemaining + (minuteRange * 60))) and (secondsRemaining >= airballSecondsRemaining) and row[13] == airballQuarter and row[19] < airballEventID:
                                if row[21] == "shot":
                                    if row[22] == airballPlayer:
                                        eventsBefore.append('assist')
                                    elif row[31] == airballPlayer:
                                        eventsBefore.append(row[21])
                                else:
                                    if row[31] == airballPlayer:
                                        if row[21] == "foul":
                                            eventsBefore.append(row[21])
                                            #eventsBefore.append(row[34][:6]) #Type of foul
                                        else:
                                            eventsBefore.append(row[21]) #Type of event that occurs
                            
                            #If the event is in the correct time range after the air ball, append the event to the list
                            if (secondsRemaining >= (airballSecondsRemaining - (minuteRange * 60))) and (secondsRemaining <= airballSecondsRemaining) and row[13] == airballQuarter and row[19] > airballEventID:
                                if row[21] == "shot":
                                    if row[22] == airballPlayer:
                                        eventsAfter.append('assist')
                                    elif row[31] == airballPlayer:
                                        eventsAfter.append(row[21])
                                else:
                                    if row[31] == airballPlayer:
                                        if row[21] == "foul":
                                            eventsAfter.append(row[21])
                                            #eventsAfter.append(row[34][:6]) #Type of foul
                                        else:
                                            eventsAfter.append(row[21]) #Type of event that occurs

                #This code runs every air ball and determines if an event happens before and / or after an air ball and puts the results into a dictionary
                if len(eventsBefore) == 0:
                    eventsDictionary["nothing"][0] = eventsDictionary["nothing"][0] + 1
                if len(eventsAfter) == 0:
                    eventsDictionary["nothing"][1] = eventsDictionary["nothing"][1] + 1
                
                eventsOccurred = []
                #print("\nEvents Before: " + str(eventsBefore))
                for event in eventsBefore:
                    if (event in eventsDictionary.keys()) and (event not in eventsOccurred):
                        eventsDictionary[event][0] = eventsDictionary[event][0] + 1
                        eventsOccurred.append(event)
                        #print("Amount of events before: " + str(len(eventsOccurred)))

                eventsOccurred = []
                #print("\nEvents After: " + str(eventsAfter))
                for event in eventsAfter:
                    if (event in eventsDictionary.keys()) and (event not in eventsOccurred):
                        eventsDictionary[event][1] = eventsDictionary[event][1] + 1
                        eventsOccurred.append(event)
                        #print("Amount of events after: " + str(len(eventsOccurred)) + "\n")
                
                count = count + 1
                eventsBefore = []
                eventsAfter = []
    except:
        continue

for event in eventsDictionary:
    print(event + " percentage change before: " + str(100 * ((eventsDictionary[event][0] / count))) + " percentage after: " + str(100 * (eventsDictionary[event][1] / count)))

print("Number of Freethrow Airballs: " + str(x))
print("Number of Airballs: " + str(count) + "\n")
print("Time to execute program: " + str(int(time.time() - startTime)) + " seconds")