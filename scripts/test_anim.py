import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig=plt.figure()
ax = plt.axes(xlim=(0, 10), ylim=(0, 10))

number_of_particles = 10
data = [0,1,2,3,4,5,6,7,8,9,10]
dict_of_circles = {}


def init():
    for n in range(number_of_particles):
        dict_of_circles["circle"+str(n+1)].center = (data[n],1)
    return dict_of_circles.values()

def animate(i):
    for n in range(number_of_particles):
        dict_of_circles["circle"+str(n+1)].center = (data[n + 1],1)
    return dict_of_circles.values()

anim=animation.FuncAnimation(fig,animate,init_func=init,frames=1000,blit=True)

plt.show()