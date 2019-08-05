import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import matplotlib.patches as patches


data_frame = pd.read_json('game.json')
#print(data_frame)
game_id = data_frame['gameid'][0]
game_date = data_frame['gamedate'][0]
events = data_frame['events']

coords = {}
next_moments = []
for row in events:
    moments = row['moments']
    eventid = row['eventId']
    visitor = row['visitor']
    home = row['home']

    visitor_name = visitor['name']
    visitor_id = visitor['teamid']
    visitor_players = visitor['players']

    home_name = home['name']
    home_id = home['teamid']
    home_players = home['players']
    if (eventid == '1'):
        for arr in moments:
            period = arr[0]
            clock = arr[2]
            shot_clock = arr[3]
            all_coords = arr[5]
            start_moment = [list[1:4] for list in arr[5]]
            print(start_moment[1][1])
            break

        count = 0

        for arr in moments:
            if(count == 0):
                count += 1
                break
        for x in range(0, len(moments[0][5])):
            print(x)
        next_moments += [list[1:4] for list in moments[0][5][0:12]]
print(next_moments)
dict_of_circles = {}
for i in range (0, 11):
    dict_of_circles[str(start_moment[i][0])] = plt.Circle((start_moment[i][1], start_moment[i][2]), radius = 1)

def init():
    for i in range(0, 11):
        dict_of_circles[str(start_moment[i][0])].center = (start_moment[i][1], start_moment[i][2])
        ax.add_patch(dict_of_circles[str(start_moment[i][0])])
    return dict_of_circles.values()

def animate(n):
    count = 0
    for i in range(0, len(next_moments)):
        dict_of_circles[str(next_moments[i][0])].center = (next_moments[i][1], next_moments[i][2])
        ax.add_patch(dict_of_circles[str(next_moments[i][0])])
    return dict_of_circles.values()

#print(coords)
fig = plt.figure()
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



anim=anim.FuncAnimation(fig,animate,init_func=init, frames=100, interval=1000, repeat=True)

plt.show()

