#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors, animation
from perlin_numpy import (
    generate_perlin_noise_2d, generate_fractal_noise_2d
)



def fire_spread(size,forest,fire_tracker):
    region = [(0,1),(0,-1),(-1,0),(1,0),(1,1),(-1,-1),(-1,1),(1,-1)]
    prob_spread = 0.2
    fire = 2
    lst = []
    for x in range(1,size-1):
        for y in range(1,size-1):
                for p,q in region:
                    if fire_tracker[x,y] > 1 and np.random.random() <= prob_spread*forest[x+p,y+q]:
                        fire_tracker[x+p,y+q] = 1+forest[x+p,y+q]
                        lst.append((p,q))
                            
                            
                           
                    
    for m in region:
        print(m, lst.count(m))
    return forest, fire_tracker


def initialize_forest(seed,size):
    np.random.seed(seed)
 # maybe add rocks in 
    forest = generate_fractal_noise_2d((size, size), (8, 8), 5)

    for x in range(0,size):
        for y in range(0,size):
            forest[x,y] +=1
            forest[x,y] = forest[x,y]*1/2
           
    
    
    fire_map = np.zeros((size,size),dtype=float)
    
    
    return forest, fire_map

def burn_out(size,forest,fire_tracker):
    fire = 2
    lst = []
    for x in range(1,size-1):
        for y in range(1,size-1):
            fire_tracker[x,y] = fire_tracker[x,y] - (1/2)*forest[x,y]
           
    
    return forest,fire_tracker


def combine_grids(size,forest,fire_tracker):
    fire = 2
    show_grid = np.zeros((size,size),dtype=float)
    
    for x in range(1,size-1):
        for y in range(1,size-1):
            if fire_tracker[x,y] >= 1:
                show_grid[x,y] = fire_tracker[x,y]
            else:
                show_grid[x,y] = forest[x,y]
                
    return show_grid

def full_generation(seeds,size,gen_num):
    fire = 2
    forest,fire_map = initialize_forest(seeds,size)
   
    
    fire_map[128,128] = fire                          #set initial fire position
   
    for x in range(0,gen_num):
        forest,fire_map = fire_spread(size,forest,fire_map)              # apply fire function
        
        show_grid = combine_grids(size,forest,fire_map)
       
        plt.figure(figsize=(5,5))
        plt.imshow(show_grid, cmap='RdYlGn_r', interpolation='lanczos',vmin=0,vmax = 2)
        plt.colorbar()
        plt.show()
        
        
    plt.imshow(forest, cmap = 'Greens')

def animate(i):
    global SIZE
    global FOREST
    global FIRE_MAP
    global MATRIX
    
    forest,fire_map = fire_spread(size,forest,fire_map) 
    show_grid = combine_grids(size,forest,fire_map)
    
    MATRIX.set_array(show_grid)
    return MATRIX,FOREST,FIRE_MAP


fig, ax = plt.subplots()
SIZE = 256

FOREST, FIRE_MAP = initialize_forest(SEED,SIZE)
MATRIX = ax.matshow(FOREST, cmap='RdYlGn_r')


np.random.seed(SEED)
ani = animation.FuncAnimation(fig, animate, frames=20000, interval=1000)

plt.show()
