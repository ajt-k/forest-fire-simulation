import numpy as np
import matplotlib.pyplot as plt

from perlin_numpy import (
    generate_perlin_noise_2d, generate_fractal_noise_2d
)

def fire_spread(size,forest,fire_tracker):
    region = [(0,1),(0,-1),(-1,0),(1,0),(1,1),(-1,-1),(-1,1),(1,-1)]            #relative coordinates to any point
    prob_spread = 0.3                                           # Changing this changes stuff
    fire = 1
    lst = []
    for x in range(1,size-1):
        for y in range(1,size-1):
                    for p,q in region:
                        if fire_tracker[x,y] == fire and np.random.random() <= prob_spread*forest[x+p,y+q]:    #region near fire will catch according to
                            fire_tracker[x+p,y+q] = fire                                                       # its 'catchability'
                            
                            lst.append((p,q))           #Used for testing percentages of each region  
                    
    for x in region:
        print(x,  lst.count(x))
    
    return forest, fire_tracker
    
    
    
 def initialize_forest(seed,size):
    np.random.seed(seed)
    
    forest = generate_fractal_noise_2d((size, size), (8, 8), 5)        

    for x in range(0,size):                     #Perlin noise function outputs values from -1 to 1
        for y in range(0,size):                 #this makes it between 0 and 1
            forest[x,y] +=1
            forest[x,y] = forest[x,y]*1/2
    
    fire_map = np.zeros((size,size),dtype=float)
    
    return forest, fire_map
 
 
 #shows pyplot images succesively - could be an animation 
 # also shows numbers of each directional movement
 
 def full_generation(seeds,size,gen_num):
    
    forest,fire_map = initialize_forest(seeds,size)       # set up grids
   
    fire_map[10,10] = fire                                  #set initial fire position
    fire_map[128,128] = fire       
    
    for x in range(0,gen_num):                                  # apply fire function for number of generations
        forest,fire_map = fire_spread(size,forest,fire_map)              
        plt.figure(figsize=(10,10))
        
        plt.imshow(fire_map, cmap='RdYlGn_r', interpolation='lanczos')
        plt.colorbar()
        plt.show()

    plt.imshow(forest, cmap = 'Greens')
    
    
    
