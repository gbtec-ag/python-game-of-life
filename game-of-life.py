import time
import random
import os
import copy

field_size = 10

DEAD = " "
ALIVE = "●"
playfield = []


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
    count = 0
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

def isPlayfieldStatic(previousGen, currentGen):
    equals = True
    for rowI, row in enumerate(previousGen):
        if ''.join(row) != ''.join(currentGen[rowI]):
            equals = False
    return equals


def printPlayfield(generation):
    os.system('cls')
    print("__" * (field_size + 1))
    for row in playfield:
        print("|", *row, "|")
    
    print(u"\u203E\u203E" * (field_size + 1))
    print(f"Generation: {generation}")

generation = 0
init()
printPlayfield(generation)

changing = True
## lifecycle
while (changing):
    time.sleep(1)
    generation = generation + 1
    playfieldPreviousGeneration = copy.deepcopy(playfield)
    for rowI, row in enumerate(playfieldPreviousGeneration):
        for fieldI, field in enumerate(row):
            neighborsCount = countLivingNeighbors(playfieldPreviousGeneration, rowI, fieldI)
            if field == DEAD and neighborsCount == 3:
                playfield[rowI][fieldI] = ALIVE
            else:
                if neighborsCount < 2 or neighborsCount >= 4:
                    playfield[rowI][fieldI] = DEAD
    
    printPlayfield(generation)
    changing = not isPlayfieldStatic(playfieldPreviousGeneration, playfield)
    

print(f'Game got static after {generation} generations.')
