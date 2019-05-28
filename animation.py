import xml.etree.ElementTree as etree
import matplotlib.pyplot as plt
import numpy as np
import random
locationList = []
from matplotlib import animation
import math
import matplotlib.patches as patches 




#PLOT ANIMATION COURT
fig = plt.figure() #initializes the figure

ax = plt.axes(xlim = (0,120), ylim = (0,50)) #defines limits for graph of players, ball, and refs 

#Goals
leftGoal = plt.Circle((5,25), radius = 0.75, fc = 'w', ec = 'orange', lw = 3) #left goal
rightGoal = plt.Circle((89,25), radius = 0.75, fc = 'w', ec = 'orange', lw = 3) #right goal

plt.gca().add_patch(leftGoal)
plt.gca().add_patch(rightGoal)

#Line to Backboards
leftLine = plt.plot([4.1,4.15], [25,25], color = 'k', lw = 4)
rightLine = plt.plot([89.85,89.9], [25,25], color = 'k', lw = 4)


#Backboards
leftPost = plt.plot([4,4], [22,28], color = 'k', lw = 2)  #left backboard
rightPost = plt.plot([90,90],[22,28], color = 'k', lw = 2) #right backboard

#Court Lines
halfCourt = plt.plot([47,47], [0,50], color = 'k', lw = 2) #line for halfcourt 
leftSide = plt.plot([0,0], [0,50], color = 'k', lw = 4) #left sideline
rightSide = plt.plot([94,94], [0,50], color = 'k', lw = 4) #right sideline
topSide = plt.plot([0,94], [50,50], color = 'k', lw = 4) #top sideline
bottomSide = plt.plot([0,94], [0,0], color = 'k', lw = 4) #bottom sideline


#Rectangles
#Left 
bottomLeft = plt.plot([0,19], [19,19], color = 'k', lw = 2) 
topLeft = plt.plot([0,19], [31,31], color = 'k', lw = 2) 
rightLeft = plt.plot([19,19], [19,31], color = 'k', lw = 2)

#Right
bottomRight = plt.plot([75,94], [19,19], color = 'k', lw = 2)
topRight = plt.plot([75,94], [31,31], color = 'k', lw = 2)
leftRight = plt.plot([75,75], [19,31], color = 'k', lw = 2)


#Hash Lines
#Sidelines
leftBottom = plt.plot([28,28], [0,3], color = 'k', lw = 2)
leftTop = plt.plot([28,28], [47,50], color = 'k', lw = 2)
rightBottom = plt.plot([66,66], [0,3], color = 'k', lw = 2)
rightTop = plt.plot([66,66], [47,50], color = 'k', lw = 2)

#Left Rectangle
hash1Bottom = plt.plot([7,8], [18.67,18.67], color = 'k', lw = 9)
hash2Bottom = plt.plot([11.08,11.08], [18.33,18.9], color = 'k', lw = 2)
hash3Bottom = plt.plot([14.25,14.25], [18.33,18.9], color = 'k', lw = 2)
hash4Bottom = plt.plot([17.42,17.42], [18.33,18.9], color = 'k', lw = 2)
hash1Top = plt.plot([7,8], [31.33,31.33], color = 'k', lw = 9)
hash2Top = plt.plot([11.08,11.08], [31.1,31.67], color = 'k', lw = 2)
hash3Top = plt.plot([14.25,14.25], [31.1,31.67], color = 'k', lw = 2)
hash4Top = plt.plot([17.42,17.42], [31.1,31.67], color = 'k', lw = 2)

#Right Rectangle
hash1Bottom = plt.plot([86,87], [18.67,18.67], color = 'k', lw = 9)
hash2Bottom = plt.plot([82.92,82.92], [18.33,18.9], color = 'k', lw = 2)
hash3Bottom = plt.plot([79.75,79.75], [18.33,18.9], color = 'k', lw = 2)
hash4Bottom = plt.plot([76.58,76.58], [18.33,18.9], color = 'k', lw = 2)
hash1Top = plt.plot([86,87], [31.33,31.33], color = 'k', lw = 9)
hash2Top = plt.plot([82.92,82.92], [31.1,31.67], color = 'k', lw = 2)
hash3Top = plt.plot([79.75,79.75], [31.1,31.67], color = 'k', lw = 2)
hash4Top = plt.plot([76.58,76.58], [31.1,31.67], color = 'k', lw = 2)

#Three-Point Lines
#Left
bottomLine = plt.plot([0,5], [4.25,4.25], color = 'k', lw = 2)
topLine = plt.plot([0,5], [45.75,45.75], color = 'k', lw = 2)
leftArc = patches.Arc((5, 25), 41.5, 41.5, angle = 0.0, theta1 = 270.0, theta2 = 90.0,  linewidth = 2, fill=False, zorder=2)

ax.add_patch(leftArc)

#Right 
bottomLine = plt.plot([89,94], [4.25,4.25], color = 'k', lw = 2)
topLine = plt.plot([89,94], [45.75,45.75], color = 'k', lw = 2)
rightArc = patches.Arc((89, 25), 41.5, 41.5, angle = 0.0, theta1 = 90.0, theta2 = 270.0,  linewidth = 2, fill=False, zorder=2)

ax.add_patch(rightArc)

#Circles
#Center
centerCircle = plt.Circle((47,25), radius = 6, fc = 'w', lw = 2) 
plt.gca().add_patch(centerCircle)
#Left
for p in [
    patches.Wedge((19, 25), 6, 270, 90, fill = False, edgecolor = None, lw = 2), 

#Right  
    patches.Wedge((75, 25), 6, 90, 270, fill = False, edgecolor = None, lw = 2)

]:
    ax.add_patch(p)
fig.savefig('wedge.png', dpi=90, bbox_inches='tight')


#Three-Point Lines
#Left

#Right

#establishes the color, shape, and size of each item
#each team has a different color
#each player has a different shape to specify who is which 'item'
line, = plt.plot([],[], color = 'darkorange', marker = 'o', markersize = 18)#basketball
line2,= plt.plot([],[], color = 'lightblue', marker = 'o', markersize = 24)#Home team P1
line3, = plt.plot([],[], color = 'lightblue', marker = 'p', markersize = 24)#Home team P2
line4, = plt.plot([],[], color = 'lightblue', marker = '^', markersize = 24)#Home team P3
line5, = plt.plot([],[], color = 'lightblue', marker = 's', markersize = 24)#Home team P4
line6, = plt.plot([],[], color = 'lightblue', marker = 'd', markersize = 24)#Home team P5
line7, = plt.plot([],[], color = 'darkred', marker = 'o', markersize = 24)#Away team P1
line8, = plt.plot([],[], color = 'darkred', marker = 'p', markersize = 24)#Away team P2
line9, = plt.plot([],[], color = 'darkred', marker = '^', markersize = 24)#Away team P3
line10, = plt.plot([],[], color = 'darkred', marker = 's', markersize = 24)#Away team P4
line11, = plt.plot([],[], color = 'darkred', marker = 'd', markersize = 24)#Away team P5
line12, = plt.plot([],[], color = 'y', marker = 'o', markersize = 5)#Refs 
line13, = plt.plot([],[], color = 'y', marker = 'o', markersize = 5)
line14, = plt.plot([],[], color = 'y', marker = 'o', markersize = 5)


#LEGEND
#places the shape on the graph to identify individual players
gHP1,= plt.plot([96],[41], color = 'lightblue', marker = 'o', markersize = 14)#Home team
gHP2, = plt.plot([96],[38], color = 'lightblue', marker = 'p', markersize = 14)#Home team
gHP3, = plt.plot([96],[35], color = 'lightblue', marker = '^', markersize = 14)#Home team
gHP4, = plt.plot([96],[32], color = 'lightblue', marker = 's', markersize = 14)#Home team
gHP5, = plt.plot([96],[28], color = 'lightblue', marker = 'd', markersize = 14)#Home team
gAP1, = plt.plot([96],[19], color = 'darkred', marker = 'o', markersize = 14)#Away team
gAP2, = plt.plot([96],[16], color = 'darkred', marker = 'p', markersize = 14)#Away team
gAP3, = plt.plot([96],[13], color = 'darkred', marker = '^', markersize = 14)#Away team
gAP4, = plt.plot([96],[10], color = 'darkred', marker = 's', markersize = 14)#Away team
gAP5, = plt.plot([96],[7], color = 'darkred', marker = 'd', markersize = 14)#Away team

 
#initializes the game clock and gives it a location on the animation
#the text is the thing changing so desired location is specified
gc = plt.text(2,2, "Game clock = ", fontsize = 20)


#Establishes where the animation will be placed on the graph
aHP1 = plt.text(98,40, "Home player 1 = ")
aHP2 = plt.text(98,37, "Home player 2 = ")
aHP3 = plt.text(98,34, "Home player 3 = ")
aHP4 = plt.text(98,31, "Home player 4 = ")
aHP5 = plt.text(98,27, "Home player 5 = ")

aAP1 = plt.text(98,18, "Away player 1 = ")
aAP2 = plt.text(98,15, "Away player 2 = ")
aAP3 = plt.text(98,12, "Away player 3 = ")
aAP4 = plt.text(98,9, "Away player 4 = ")
aAP5 = plt.text(98,6, "Away player 5 = ")


#renames player, ball, and ref location lists into shorter variables 

#Lr2= R2Cord
#Lr3 = R3Cord

    
#for each player (a-n) x (x1) and y (y1) locations are paired with each person. At the end the x and y coordinates are yeilded. The zip() function creates a tupple out of, in this case, 14 seperate lists.
#For example the input could look something like a = [1, 2, 3] and b = [4, 5, 6]. The zip() function would combine them to look like [(1,4), (2, 5), (3, 6)]

def point_data():
   for a, b, c, d, e, f, g, h, i, j, k in zip(Lball, Lp1, Lp2, Lp3, Lp4, Lp5, Lp6, Lp7, Lp8, Lp9, Lp10):
      x1= a[0]
      y1= a[1]
      x2= b[0]
      y2= b[1]
      x3= c[0]
      y3= c[1]
      x4= d[0]
      y4= d[1]
      x5= e[0]
      y5= e[1]
      x6= f[0]
      y6= f[1]
      x7= g[0]
      y7= g[1]
      x8= h[0]
      y8= h[1]
      x9= i[0]
      y9= i[1]
      x10= j[0]
      y10= j[1]
      x11= k[0]
      y11= k[1] 
      yield x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x9, y9, x10, y10, x11, y11
        

def animate(point_data): 
    x1, y1 = point_data[0], point_data[1] 
    x2, y2, x3, y3 = point_data[2], point_data[3], point_data[4], point_data[5]
    x4, y4, x5, y5 = point_data[6], point_data[7], point_data[8], point_data[9]
    x6, y6, x7, y7 = point_data[10], point_data[11], point_data[12], point_data[13]
    x8, y8, x9, y9 = point_data[14], point_data[15], point_data[16], point_data[17]
    x10, y10, x11, y11 = point_data[18], point_data[19], point_data[20], point_data[21]

    line.set_data(x1, y1) 
    line2.set_data(x2, y2)
    line3.set_data(x3, y3) 
    line4.set_data(x4, y4)
    line5.set_data(x5, y5)
    line6.set_data(x6, y6)
    line7.set_data(x7, y7)
    line8.set_data(x8, y8) 
    line9.set_data(x9, y9)
    line10.set_data(x10, y10)
    line11.set_data(x11, y11)
   


#animates the player, ball, and ref locations in the XML file. 
#The interval depicts the amount of time before a new location is displayed. For example if interval = 500 the markers would move more slowly around the graph 
anim = animation.FuncAnimation(fig, animate, point_data, interval = 40)


#animates the game clock to show real time
#The interval matches the resolution of the SportVU system


plt.show() #animates everything





