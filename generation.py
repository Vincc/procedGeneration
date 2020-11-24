from random import randint
from mayavi import mlab
import noise
import numpy as np
import cv2
import scipy

settings = {"desert": [50, 1, 0.05, 1000, 10], "mount": [150, 6, 0.5, 2, 100], }
terrain = "mount"

shape = (500, 500)
scale = settings[terrain][0]
octaves = settings[terrain][1]  # iterations of detail
persistence = settings[terrain][2]  # magnitude of distortions (amplitude)
lacunarity = settings[terrain][3]  # level of detail (freq)
displace = settings[terrain][4]

worldLayer1 = np.zeros(shape)
worldLayer2 = np.zeros(shape)

b1 = randint(0,100)
b2 = randint(0,100)

for i in range(shape[0]):
    for j in range(shape[1]):
        worldLayer1[i][j] = noise.pnoise2(i / 150, j / 150, octaves=4, persistence=0.05,
                                          lacunarity=3, repeatx=100, repeaty=100, base=b1) * 10
        worldLayer2[i][j] = noise.pnoise2(i / scale, j / scale, octaves=octaves, persistence=persistence,
                                          lacunarity=lacunarity, repeatx=1000, repeaty=1000, base=b2) * 100



# print(world)
#
# cv2.imshow("image", worldLayer1)
# cv2.imshow("imagee", worldLayer2)
# cv2.imshow("ima3gee", (np.divide(np.add(worldLayer2,worldLayer1),2)))
#
# cv2.waitKey()

# print(np.divide(np.add(worldLayer2,worldLayer1),2))

mlab.surf(np.divide(np.add(worldLayer2,worldLayer1),2))
mlab.show()





