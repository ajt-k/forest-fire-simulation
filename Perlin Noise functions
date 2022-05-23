##Github:   Pvigier/perlin-numpy

import matplotlib.pyplot as plt
import numpy as np



##Smooth perlin noise function

from perlin_numpy import (
    generate_fractal_noise_2d, generate_fractal_noise_3d,
    generate_perlin_noise_2d, generate_perlin_noise_3d
)

noise = generate_perlin_noise_2d((256, 256), (8, 8))
plt.figure()
for x in range(0,256):
    for y in range(0,256):
        noise[x,y] = abs(noise[x,y])+noise[x,y]/10+0.1
        
plt.imshow(noise, cmap=cm.coolwarm, interpolation='lanczos')
noise[0,1]
noise[1,0]
plt.colorbar()



## Fractal noise function


from perlin_numpy import (
    generate_perlin_noise_2d, generate_fractal_noise_2d
)

np.random.seed(np.random.randint(0,10000))
noise = generate_fractal_noise_2d((256, 256), (4, 4), 5)
for x in range(0,256):
    for y in range(0,256):
        noise[x,y] +=1
        noise[x,y] = noise[x,y]*1/2
        
plt.figure()
plt.imshow(noise, cmap='coolwarm', interpolation='lanczos')
plt.colorbar()
plt.show()
