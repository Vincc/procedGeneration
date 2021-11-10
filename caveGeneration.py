from PIL.Image import init
import matplotlib.pyplot as plt
import random
import time
##cellular automata
size = 100
chanceOfSpawn = 0.25
neighbourNumDeath = 3 #under population, increase means need more neighbours
neighbourNumBirth = 2 #space to grow, increase means need more space
stepNum = 100
envGrid = [[0 for i in range(size) ] for i in range(size)]

def countNeighbours(grid, ind):
    checks = [[-1,-1],[-1,0],[-1,1],[0,-1], [0,1],[1,-1],[1,0],[1,1]]
    try:
        return sum([1 for i in checks if grid[ind[0]+i[0]][ind[1]+i[1]]==1])
    except IndexError:
        return 8
def initGrid(grid):
    for y, row in enumerate(grid):
        for x,i in enumerate(row):
            if random.random() > chanceOfSpawn:
                grid[x][y] = 1

def generateCave(grid):
    newgrid = [[0 for i in range(size) ] for i in range(size)]
    for y, row in enumerate(grid):
        for x,i in enumerate(row):
            if countNeighbours(grid, (x,y)) > neighbourNumBirth and grid[x][y]==0: #space to grow
                newgrid[x][y] = 1
            elif countNeighbours(grid, (x,y)) < neighbourNumDeath and grid[x][y]==1: #underpopulation
                newgrid[x][y] = 0
            
    return newgrid

initGrid(envGrid)
for i in range(stepNum):
    envGrid = generateCave(envGrid) 
    plt.imshow(envGrid)
    plt.pause(0.3)

plt.imshow(envGrid)

    
