import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import colors

# function to randomly spread fire


def fire_spread(forest, size):
    lat_region = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    diag_region = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    prob_spread = 0.2
    fire, tree = 2, 1
    for x in range(0, size + 1):
        for y in range(0, size + 1):
            if forest[x, y] == fire:
                for p, q in lat_region:
                    if forest[x + p, y + q] == tree and np.random.random() <= prob_spread:
                        forest[x + p, y + q] = fire

                for r, s in diag_region:
                    if forest[x + p, y + q] == tree and np.random.random() <= prob_spread:
                        forest[x + p, y + q] = fire

    return forest


# initializes a numpy array that will be updated using functions


def populate_grid(size):
    prob_tree, prob_ignite = 0.8, 0.05
    fire, tree, empty = 2, 1, 0
    forest = np.zeros((size + 1, size + 1), dtype=int)
    for x in range(0, size):
        for y in range(0, size):
            if forest[x, y] == empty and np.random.random() <= prob_tree:
                forest[x, y] = tree

            if forest[x, y] == tree and np.random.random() <= prob_ignite:
                forest[x, y] = fire
    return forest


# Checks for where fire is located and adds "time counter" to mirror array


def burn_out(forest, burn_time, size):
    fire, tree = 2, 1
    for x in range(0, size):
        for y in range(0, size):
            if forest[x, y] == fire:
                burn_time[x, y] += 1
            if burn_time[x, y] == 3:
                forest[x, y] = burnt
    return forest, burn_time


SIZE = 500
FOREST = populate_grid(SIZE)
BURN_TIME = np.zeros((SIZE, SIZE), dtype=int)

fig, ax = plt.subplots()
cmap = colors.ListedColormap(["#d4a78c", "lawngreen", "#02a102", "#c73838"])

MATRIX = ax.matshow(FOREST, cmap=cmap)


def animate(i):
    global FOREST
    global BURN_TIME
    global MATRIX
    FOREST = fire_spread(FOREST, SIZE)
    FOREST, BURN_TIME = burn_out(FOREST, BURN_TIME, SIZE)
    MATRIX.set_array(FOREST)


ani = matplotlib.animation.FuncAnimation(fig, animate, frames=20000, interval=1000)
plt.show()
