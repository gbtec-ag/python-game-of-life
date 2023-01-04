import time
import random
import os
import copy

field_size = 3

DEAD = " "
ALIVE = "○"
playfield = []

playfield = [
    [DEAD, ALIVE, DEAD],
    [DEAD, ALIVE, DEAD],
    [DEAD, ALIVE, DEAD]
]

def countNeighborsOfARow(row, fieldIndex, ownRow = False):
    count = 0
    if row[fieldIndex] == ALIVE and not ownRow:
        count = count + 1
    if fieldIndex > 0 and row[fieldIndex - 1] == ALIVE:
        count = count + 1
    if fieldIndex < field_size -1 and row[fieldIndex + 1] == ALIVE:
        count = count + 1
    return count

def countLivingNeighbors(playfield, rowIndex, fieldIndex):
    #count = random.randrange(0, 8)
    count = 0
    #return count
    if rowIndex > 0:
        count = count + countNeighborsOfARow(playfield[rowIndex - 1], fieldIndex)
    if rowIndex < field_size - 1:
        count = count + countNeighborsOfARow(playfield[rowIndex + 1], fieldIndex)
    count = count + countNeighborsOfARow(playfield[rowIndex], fieldIndex, ownRow=True)
    return count

def init(): 
    rows = 0
    while (rows < field_size):
        size = 0
        playfield.append([])
        while (size < field_size):
            size = size + 1
            playfield[rows].append(random.choice([ALIVE, DEAD]))
        rows = rows + 1
        os.system('cls')

def printPlayfield():
    print("_" * field_size * 3)
    for row in playfield:
        print("|", *row, "|")
    
    print(u"\u203E" * field_size * 3)

    time.sleep(2)
    os.system('cls')

#init()
printPlayfield()
## lifecycle
while (True):
    playfieldPreviousGeneration = copy.deepcopy(playfield)
    for rowI, row in enumerate(playfieldPreviousGeneration):
        #print(rowI, row)
        for (fieldI, field) in enumerate(row):
            #print(field, fieldI)
            neighborsCount = countLivingNeighbors(playfieldPreviousGeneration, rowI, fieldI)
            if field == DEAD and neighborsCount == 3:
                playfield[rowI][fieldI] = ALIVE
            else:
                if neighborsCount < 2 or neighborsCount > 4:
                    playfield[rowI][fieldI] = DEAD
    
    printPlayfield()


