#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import  animation
import matplotlib.colors as mcolors
from perlin_numpy import (
    generate_perlin_noise_2d, generate_fractal_noise_2d
)
fire = 2



def fire_spread(size,forest,fire_tracker):
    region = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
    prob_spread = 0.5
    lst = []
    for x in range(1,size-1):
        for y in range(1,size-1):
            if fire_tracker[x,y] > 1:
                lst.append((x,y))
                    
                    
    for x,y in lst:
        for p,q in region:
            if fire_tracker[x+p,y+q] < 1 and np.random.random() <= prob_spread*forest[x+p,y+q]:
                        fire_tracker[x+p,y+q] = 1+forest[x+p,y+q]
                        
    return forest, fire_tracker

def initialize_forest(seed,size):
    np.random.seed(seed)
    rock = 0
    forest = generate_fractal_noise_2d((size, size), (8, 8), 5)

    for x in range(0,size):
        for y in range(0,size):
            forest[x,y] +=1
            forest[x,y] = forest[x,y]*1/2
            if np.random.random()<0.05:
               forest[x,y] = rock
    
    
    fire_map = np.zeros((size,size),dtype=float)
    burn_time = np.zeros((size,size),dtype=float)
    
    return forest, fire_map, burn_time

def burn_out(size,forest,fire_tracker,burn_time):
    for x in range(1,size-1):
        for y in range(1,size-1):
            
            fire_tracker[x,y] = fire_tracker[x,y] - (1/6)*forest[x,y]
            if fire_tracker[x,y] > 1:
                burn_time[x,y] +=1
            if burn_time[x,y] == 5:
                forest[x,y] = 0
            
    
    return forest,fire_tracker


def combine_grids(size,forest,fire_tracker):
 
    show_grid = np.zeros((size,size),dtype=float)
    
    for x in range(1,size-1):
        for y in range(1,size-1):
            if fire_tracker[x,y] >= 1:
                show_grid[x,y] = fire_tracker[x,y]
            else:
                show_grid[x,y] = forest[x,y]
                
    return show_grid


def animate(i):
    global SIZE
    global FOREST
    global FIRE_MAP
    global MATRIX
    
    FOREST, FIRE_MAP = fire_spread(SIZE,FOREST,FIRE_MAP) 
    
    show_grid = combine_grids(SIZE,FOREST,FIRE_MAP)
   
    burn_out(SIZE, FOREST, FIRE_MAP, BURN_TIME)
   
    MATRIX.set_array(show_grid)
    
    return MATRIX,FOREST,FIRE_MAP



colors1 = plt.cm.Greens(np.linspace(0., 1, 128))
colors2 = plt.cm.Reds(np.linspace(0, 1, 128))

# combine them and build a new colormap
colors = np.vstack((colors1, colors2))
cmap = mcolors.LinearSegmentedColormap.from_list('my_colormap', colors)

fig, ax = plt.subplots()

SIZE = 256

SEED = np.random.randint(0,1000)

FOREST, FIRE_MAP, BURN_TIME= initialize_forest(SEED,SIZE)



MATRIX = ax.matshow(FOREST,cmap = cmap,vmin = 0,vmax= 2)

FIRE_MAP[128,128] = 2  
np.random.seed(SEED)

ani = animation.FuncAnimation(fig, animate, frames=20000, interval=500)

plt.show()

