from PIL.Image import init
import matplotlib.pyplot as plt
import random
import time
import math
##cellular automata
size = 200
chanceOfSpawn = 0.4
neighbourNumDeath = 5 #upper neighbour limit at which cells start dying
neighbourNumBirth = 2 #number of neighbours that cause a dead cell to become alive.
stepNum = 100
envGrid = [[0 for i in range(size) ] for i in range(size)]

def countNeighbours(grid, ind):
    checks = [[-1,-1],[-1,0],[-1,1],[0,-1], [0,1],[1,-1],[1,0],[1,1]]
    
    if 0 in ind or size-1 in ind:
        print("edge")
        return 8
    else:
        s = 0
        for i in checks:
            """
            print(i)
            print((ind[0]+i[0],ind[1]+i[1]), end = "")
            print(":", end = "")
            print(grid[ind[1]+i[1]][ind[0]+i[0]])
            """
            if grid[ind[1]+i[1]][ind[0]+i[0]] == 1:
                s+=1
        return s
def initGridUniform(grid):
    for y, row in enumerate(grid):
        for x,i in enumerate(row):
            if random.random() < chanceOfSpawn:
                grid[x][y] = 1

def initGridRadial(grid, cutoff, probRange):
    centerpoint = (len(grid[0])/2,len(grid)/2)
    cutoff = 50
    for y, row in enumerate(grid):
        for x,i in enumerate(row):
            distance = math.sqrt((centerpoint[0]-x)**2+(centerpoint[1]-y)**2)
            if distance>cutoff:
                grid[x][y] = 3
                print(probRange)
                chanceOfSpawn = ((((probRange[1]-probRange[0]*distance)/cutoff))+probRange[0])/(probRange[0]-probRange[1])
                print(chanceOfSpawn)
            elif random.random()< chanceOfSpawn:
                grid[x][y]=1


def generateCave(grid):
    newgrid = [[0 for i in range(size) ] for i in range(size)]
    for y, row in enumerate(grid):
        for x,i in enumerate(row):
            #print("")
            #print((x,y))

            neigh = countNeighbours(grid, [x,y])
            #print(neigh)

            if  neigh > neighbourNumBirth and grid[y][x]==0: #space to grow
                newgrid[y][x] = 1
            elif neigh < neighbourNumDeath and grid[y][x]==1: #underpopulation
                newgrid[y][x] = 0
            else:
                newgrid[y][x] = i
            
    return newgrid

initGridUniform(envGrid)
#initGridRadial(envGrid, 50, (0.5,0.2))

for i in range(stepNum):
    plt.imshow(envGrid)
    envGrid = generateCave(envGrid)
    plt.pause(0.1)
        
