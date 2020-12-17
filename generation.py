from random import randint
from mayavi import mlab
import noise
import numpy as np
import cv2
import scipy

shape = (500, 500)
worldLayer1 = np.zeros(shape)
worldLayer2 = np.zeros(shape)

b1 = randint(0,100)
b2 = randint(0,100)

for i in range(shape[0]):
    for j in range(shape[1]):
        worldLayer1[i][j] = noise.pnoise2(i / 200, j / 200, octaves=3, persistence=0.5,
                                          lacunarity=2, repeatx=500, repeaty=500, base=b1) * 150
        worldLayer2[i][j] = noise.pnoise2(i / 100, j / 100, octaves=6, persistence=0.5,
                                          lacunarity=2, repeatx=500, repeaty=500, base=b2) * 50



print(1)
# print(world)
#
# cv2.imshow("image", worldLayer1)
# cv2.imshow("imagee", worldLayer2)


cv2.imshow("dd", np.divide(np.add(worldLayer2,worldLayer1),2)*arr)

