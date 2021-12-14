
import matplotlib.pyplot as plt
import random
import time
import numpy as np
from numpy.core.fromnumeric import choose


size = 50
envGrid = np.array([[(0,0,0) for i in range(size)] for i in range(size)])
visitedCells = []
path = [[1,0],]

def chooseNeighbour(ind):
    checks = [[-2,0],[0,-2], [0,2],[2,0]]
    ava = []
    for i in checks:
        cy = ind[0]+i[0]
        cx = ind[1]+i[1]
        
        if [cy,cx] not in visitedCells and cy > 0 and cx > 0 and cy < size-1 and cx < size-1:
            ava.append([cy,cx])
    if ava != []:
        return random.choice(ava)
    else:
        return []
    
def goodPath(grid):
    while path != []:
        print(len(visitedCells))
        current = path.pop()
        next = chooseNeighbour(current)
        if next != []:
            path.append(current)
            grid[int((current[0]+next[0])/2)][int((current[1]+next[1])/2)] = (255,255,255)

            visitedCells.append(next)
            path.append(next)
            grid[current[0]][current[1]] = (255,255,255)
        else:
            continue
        
    return grid

maze = goodPath(envGrid)
maze[size-3,size-2] = (225,0,0)

plt.imshow(maze)
plt.show()

def mazeSolve(maze):
    
    return 
