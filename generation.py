# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
from random import randint
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# Axes3D.plot_surface([i for i in range(100)], [i for i in range(100)], )
# plt.show()
#


from mayavi import mlab



import noise
import numpy as np


shape = (100,100)
scale = 100
octaves = 3
persistence = 0.5
lacunarity = 2

world = np.zeros(shape)
for i in range(shape[0]):
    for j in range(shape[1]):
        world[i][j] = noise.pnoise2(i/scale,
                                    j/scale,
                                    octaves=octaves,
                                    persistence=persistence,
                                    lacunarity=lacunarity,
                                    repeatx=100,
                                    repeaty=100, base=0) * 100

print(world)

Z = [[randint(1,10) for i in range(100)] for i in range(100)]
mlab.surf(world)
mlab.show()