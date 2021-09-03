import time
import sys
rows, cols = (6,7)
player1 = True
empty = ' '

# Prints the board with plays
def PrintBoard():
    for p in range(12):
        print()
    print("   1   2   3   4   5   6   7   ")
    for i in range(rows):
        print(" |", end = '')
        for j in range(cols):
            print(" "+ str(chipArray[i][j]) + " |", end = '')
        print("")
        print(" #- -#- -#- -#- -#- -#- -#- -# ")
    print("/'''''''''''''''''''''''''''''\\")

# Initializes the chip array to all the same character
def initChipArray(chipArray):
    for i in range(rows):
        for j in range(cols):
            chipArray[i][j] = empty

#swaps the player
def swapPlayer():
    global player1
    if (player1):
        player1 = False
    else:
        player1 = True

# returns @ or O depending on the player variable
def playerchip(player1):
    if (player1):
        returningChip = '@'
    else:
        returningChip = 'O'
    return returningChip

#Plays the chip after playChip function
def DropChip(colChoice, player1):
    i = 0
    while ((i < 6) and (chipArray[i][int(colChoice)] == empty)):
        if (i != 0):
            chipArray[i-1][int(colChoice)] = empty
        chipArray[i][int(colChoice)] = playerchip(player1)
        i = i + 1
    i = i - 1
    winCheck(i, colChoice, player1)

# User interface for the play and checks input
def PlayChip(player1):
    if (player1):
        print("Player @")
    else:
        print("Player O")

    print("Choose a column to drop your chip (1 - 7): ")
    colChoice = input()
    while not((colChoice.isnumeric() and int(colChoice) > 0 and int(colChoice) < 8)):
        print("Invalid! Choose a column to drop your chip (1 - 7): ")
        colChoice = input()
    while (chipArray[0][int(int(colChoice)-1)] != empty):
        print("Column is full!")
        colChoice = input()
    colChoice = (int(colChoice) - 1)
    DropChip(colChoice, player1)

# Checks all 7 directions for 4 chips in a row and returns a win status if so
def winCheck(row, col, player1):
    playerChip = playerchip(player1)
    rowChips = 1
    x = 1

#check in Horizontal direction
    while (int(col + x) < 7 and chipArray[row][int(col + x)] == playerChip): #right
        rowChips = rowChips + 1
        x = x + 1
    x = 1
    while (int(col - x) > -1 and chipArray[row][int(col - x)] == playerChip): #left
        rowChips = rowChips + 1
        x = x + 1
    if (rowChips > 3):
        PrintBoard()
        print("Player " + playerChip + " wins")
        time.sleep(5)
        sys.exit(0)
    else:
        x = 1
        rowChips = 1

#check in Vertical direction
    while (int(row + x) < 6 and chipArray[int(row + x)][col] == playerChip and rowChips < 4): #down
        rowChips = rowChips + 1
        x = x + 1
    if (rowChips == 4):
        PrintBoard()
        print("Player " + playerChip + " wins")
        time.sleep(5)
        sys.exit(0)
    else:
        x = 1
        rowChips = 1

#check in Diagnal /
    while (int(col + x) < 7 and int(row - x) > -1 and chipArray[int(row - x)][int(col + x)] == playerChip): #up to the right
        rowChips = rowChips + 1
        x = x + 1
    x = 1
    while (int(col - x) > -1 and int(row + x) < 6 and chipArray[int(row + x)][int(col - x)] == playerChip): #down to the left
        rowChips = rowChips + 1
        x = x + 1

    if (rowChips > 3):
        PrintBoard()
        print("Player " + playerChip + " wins")
        time.sleep(5)
        sys.exit(0)
    else:
        x = 1
        rowChips = 1

#check in Diagnal \
    while (int(col + x) < 7 and int(row + x) < 6 and chipArray[int(row + x)][int(col + x)] == playerChip): #down to the right
        rowChips = rowChips + 1
        x = x + 1
    x = 1
    while (int(col - x) > -1 and int(row - x) > -1 and chipArray[int(row - x)][int(col - x)] == playerChip): #up to the left
        rowChips = rowChips + 1
        x = x + 1

    if (rowChips > 3):
        PrintBoard()
        print("Player " + playerChip + " wins")
        time.sleep(5)
        sys.exit(0)
    else:
        x = 1
        rowChips = 1
        return

chipArray = [[0 for i in range(cols)] for j in range(rows)] 
initChipArray(chipArray)
while (True):
    PrintBoard()
    PlayChip(player1)
    swapPlayer()
PrintBoard()