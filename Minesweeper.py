    ###TO-DO###
#modify sweep1/2/3/4 to support lists instead of strings

#imports
import random

#sweep function is defined
def sweep(selectedCell):
    #variables
    inCell = False
    threats = -1
    #if already checked
    for tile in sweptTiles:
        if selectedCell[0] == tile[0]:
            if selectedCell[2] == tile[1]:     
                inCell = True
                break
    visibleTiles.sort()
    if inCell == False:
            #if top left corner
            if int(selectedCell[0]) >= x or int(selectedCell[2]) >= y:
                pass
            elif int(selectedCell[0]) == 0 and int(selectedCell[2]) == 0:
                threats = tiles[1][2] + tiles[x][2] + tiles[x+1][2]
                sweep3(threats, selectedCell)     
            #if top right corner
            elif int(selectedCell[0]) == (x-1) and int(selectedCell[2]) == 0:
                threats = tiles[(int(selectedCell[0]) - 1) * x][2] + tiles[((int(selectedCell[0]) - 1) * x) + 1][2] + tiles[((int(selectedCell[0]) * x) + 1)][2]
                sweep3(threats, selectedCell)     
            #if bottom left corner
            elif int(selectedCell[0]) == 0 and int(selectedCell[2]) == (y-1):
                threats = tiles[((y-2)*x)][2] + tiles[((y-2)*x)+1][2] + tiles[(((y-1)*x)+1)][2]
                sweep3(threats, selectedCell)     
            #if bottom right corner
            elif int(selectedCell[0]) == (x-1) and int(selectedCell[2]) == (y-1):
                threats = tiles[((y)*(x-1))-2][2] + tiles[(y)*(x-1)-1][2] + tiles[(y*x)-2][2]
                sweep3(threats, selectedCell)     
            #if top row
            elif int(selectedCell[0]) == 0:
                threats = tiles[int(selectedCell[2])-1][2] + tiles[int(selectedCell[2])+1][2] + tiles[(x + int(selectedCell[2])) - 1][2] + tiles[x + int(selectedCell[2])][2] + tiles[x + int(selectedCell[2]) + 1][2]
                sweep3(threats, selectedCell)     
            #if bottom row
            elif int(selectedCell[0]) == (x-1):
                threats = tiles[(y * (x-2)) + int(selectedCell[2]) - 1][2] + tiles[(y * (x-2)) + int(selectedCell[2])][2] + tiles[(y * (x-2)) + int(selectedCell[2]) + 1][2] + tiles[(y * (x-1)) + int(selectedCell[2]) - 1][2] + tiles[(y * (x-1)) + int(selectedCell[2]) + 1][2]
                sweep3(threats, selectedCell)     
            #if left column
            elif int(selectedCell[2]) == 0:
                threats = tiles[(int(selectedCell[0]) * x) - x][2] + tiles[((int(selectedCell[0]) * (x)) - x + 1)][2] + tiles[((int(selectedCell[0]) * x) + 1)][2] + tiles[((int(selectedCell[0])) * x) + x][2] + tiles[((int(selectedCell[0]) * x) + x) + 1][2]
                sweep3(threats, selectedCell)     
            #if right column
            elif int(selectedCell[2]) == (y-1):
                threats = tiles[int((selectedCell[0])) * (x) - 2][2] + tiles[(int(selectedCell[0]) * (x)) - 1][2] + tiles[(int(selectedCell[0]) * x) + (x-2)][2] + tiles[((int(selectedCell[0]) * x) + ((2 * x) - 2))][2] + tiles[((int(selectedCell[0]) * x) + ((2 * x) - 1))][2]
                sweep3(threats, selectedCell)     
            #if inside
            else:
                threats = tiles[((int(selectedCell[0]) * x) - (x) - 1) + int(selectedCell[2])][2] + tiles[((int(selectedCell[0]) * x) - (x)) + int(selectedCell[2])][2] + tiles[((int(selectedCell[0]) * x) - (x) + 1) + int(selectedCell[2])][2] + tiles[((int(selectedCell[0]) * (x) - 1) + int(selectedCell[2]))][2] + tiles[((int(selectedCell[0]) * x) + 1) + int(selectedCell[2])][2] + tiles[((int(selectedCell[0]) * x) + x - 1) + int(selectedCell[2])][2] + tiles[((int(selectedCell[0]) * x) + x) + int(selectedCell[2])][2] + tiles[((int(selectedCell[0]) * x + x + 1) + int(selectedCell[2]))][2]
                sweep3(threats, selectedCell)   
            if threats == 0:
                sweep2(selectedCell)           
                return threats

#second sweep function, to automatically sweep surrounding cells if primary sweep function returns zero threats
def sweep2(selectedCell):
    c = int(selectedCell[0])
    c -=1
    d = int(selectedCell[2])
    d -= 1
    selectedCell = []
    selectedCell.append(c)
    selectedCell.append(",")
    selectedCell.append(d)
    if int(selectedCell[2]) < 0:
        pass
    else:
        if int(selectedCell[0]) < 0:
            pass
        else:
            sweep(selectedCell)
        c = int(selectedCell[0]) 
        c += 1
        selectedCell[0] = c
        sweep(selectedCell)
        c = int(selectedCell[0]) 
        c += 1
        selectedCell[0] = str(c)
        if int(selectedCell[0]) >= x:
            pass
        else:
            sweep(selectedCell)
        c = int(selectedCell[0]) 
        c -= 2
        selectedCell[0] = c
    c = int(selectedCell[2]) 
    c += 1
    selectedCell[2] = c
    if int(selectedCell[0]) < 0:
        pass
    else:
        sweep(selectedCell)
    c = int(selectedCell[0])
    c += 2
    selectedCell[0] = str(c)
    if int(selectedCell[0]) >= x:
        pass
    else:
        sweep(selectedCell)
    c = int(selectedCell[0]) 
    c -= 2
    selectedCell[0] = c
    c = int(selectedCell[2]) 
    c += 1
    selectedCell[2] = str(c)
    if int(selectedCell[2]) >= y:
        pass
    else:
        if int(selectedCell[0]) < 0:
            pass
        else:
            sweep(selectedCell)
        c = int(selectedCell[0]) 
        c += 1
        selectedCell[0] = c
        sweep(selectedCell)
        c = int(selectedCell[0]) 
        c += 1
        selectedCell[0] = str(c)
        if int(selectedCell[0]) >= x:
            pass
        else: 
            sweep(selectedCell)

#smaller functions to reduce lines 
def sweep3(threats, selectedCell):
    sweptTile = []
    sweptTile.append(selectedCell[0])
    sweptTile.append(selectedCell[2])
    sweptTile.append(" Checked: ")
    sweptTile.append(threats)
    sweptTiles.append(sweptTile)
    selectedList = []
    selectedList.append(int(selectedCell[0]))   
    selectedList.append(int(selectedCell[2]))
    selectedList.append(str(threats))
    visibleTiles[(x * (int(selectedCell[0]))) + int(selectedCell[2])] = selectedList
    del selectedList 
    return threats
def grid(tiles):
    for a in range(0,int(y)):
        for b in range(0,int(x)):
            newTiles = [b, a, 0]
            tiles.append(newTiles)
def firstGuess(selectedList, tiles):
    c = x
    d = 0
    tiles.sort()
    for i in range(0,y):
        print(tiles[d:c])
        c+= x
        d+= x
    myList = []
    print(myList)
    first = input("For your first tile, enter the X coordinate")
    myList.append(first)
    myList.append(",")
    first2 = input("For your first tile, enter the Y coordinate")
    myList.append(first2)
    if first.isnumeric() == True:
        if first2.isnumeric() == True:
            if int(myList[0]) >= x or int(myList[2]) >= y:
                del myList
                print("try again\n")
                results = firstGuess(selectedList, tiles)
                return results
            else:
                #if top left corner
                if int(myList[0]) == 0 and int(myList[2]) == 0:
                    selectedList.append(tiles[0])
                    selectedList.append(tiles[1])
                    selectedList.append(tiles[x])
                    selectedList.append(tiles[x+1])
                    tiles.remove(tiles[0])
                    tiles.remove(tiles[0])
                    tiles.remove(tiles[x-2])
                    tiles.remove(tiles[x-2])           
                    return [selectedList, tiles, myList]             
                #if top right corner
                elif int(myList[0]) == (x-1) and int(myList[2]) == 0:
                    selectedList.append(tiles[x-2])
                    selectedList.append(tiles[x-1])
                    selectedList.append(tiles[(2*x)-2])
                    selectedList.append(tiles[(2*x)-1])
                    tiles.remove(tiles[x-2])
                    tiles.remove(tiles[x-2])
                    tiles.remove(tiles[(2*x)-4])
                    tiles.remove(tiles[(2*x)-4])   
                    return [selectedList, tiles, myList]  
                #if bottom left corner
                elif int(myList[0]) == 0 and int(myList[2]) == (y-1):
                    selectedList.append(tiles[(y-2)*x])
                    selectedList.append(tiles[((y-2)*x)+1])
                    selectedList.append(tiles[(y-1)*x])
                    selectedList.append(tiles[((y-1)*x)+1])
                    tiles.remove(tiles[(y-2)*x])
                    tiles.remove(tiles[((y-2)*x)])
                    tiles.remove(tiles[((y-1)*x)-2])
                    tiles.remove(tiles[((y-1)*x)-2])
                    return [selectedList, tiles, myList]
                #if bottom right corner
                elif int(myList[0]) == (x-1) and int(myList[2]) == (y-1):
                    selectedList.append(tiles[(y)*(x-1)-2])
                    selectedList.append(tiles[(y)*(x-1)-1])
                    selectedList.append(tiles[(y*x)-2])
                    selectedList.append(tiles[(y*x)-1])
                    tiles.remove(tiles[(y)*(x-1)-2])
                    tiles.remove(tiles[(y)*(x-1)-2])
                    tiles.remove(tiles[(y*x)-4])
                    tiles.remove(tiles[(y*x)-4])     
                    return [selectedList, tiles, myList]
                #if top row
                elif int(myList[0]) == 0:
                    selectedList.append(tiles[int(myList[2])-1])
                    selectedList.append(tiles[int(myList[2])])
                    selectedList.append(tiles[int(myList[2])+1])
                    selectedList.append(tiles[int(myList[2])-1+x])
                    selectedList.append(tiles[int(myList[2])+x])
                    selectedList.append(tiles[int(myList[2])+x+1])
                    tiles.remove(tiles[int(myList[2])-1])
                    tiles.remove(tiles[int(myList[2])-1])
                    tiles.remove(tiles[int(myList[2])-1])
                    tiles.remove(tiles[int(myList[2])-4+x])
                    tiles.remove(tiles[int(myList[2])+x-4])
                    tiles.remove(tiles[int(myList[2])+x-4])
                    return [selectedList, tiles, myList]
                #if bottom row
                elif int(myList[0]) == (x-1):
                    selectedList.append(tiles[(y*(x-2)) + int(myList[2])-1])
                    selectedList.append(tiles[(y*(x-2)) + int(myList[2])])
                    selectedList.append(tiles[(y*(x-2)) + int(myList[2])+1])
                    selectedList.append(tiles[(y*(x-1)) + int(myList[2])-1])
                    selectedList.append(tiles[(y*(x-1)) + int(myList[2])])
                    selectedList.append(tiles[(y*(x-1)) + int(myList[2])+1])
                    tiles.remove(tiles[(y*(x-2)) + int(myList[2])-1])
                    tiles.remove(tiles[(y*(x-2)) + int(myList[2])-1])
                    tiles.remove(tiles[(y*(x-2)) + int(myList[2])-1])
                    tiles.remove(tiles[(y*(x-1)) + int(myList[2])-4])
                    tiles.remove(tiles[(y*(x-1)) + int(myList[2])-4])
                    tiles.remove(tiles[(y*(x-1)) + int(myList[2])-4])
                    return [selectedList, tiles, myList]
                #if left column
                elif int(myList[2]) == 0:
                    selectedList.append(tiles[(int(myList[0]) * x) - x])
                    selectedList.append(tiles[(int(myList[0])*(x))-x+1])
                    selectedList.append(tiles[(int(myList[0]))*x])
                    selectedList.append(tiles[(int(myList[0])*x)+1])
                    selectedList.append(tiles[(int(myList[0])*x)+x])
                    selectedList.append(tiles[(int(myList[0])*x)+x+1])
                    tiles.remove(tiles[(int(myList[0]) * x) - x])
                    tiles.remove(tiles[(int(myList[0])*(x))-x])
                    tiles.remove(tiles[(int(myList[0])*x)-2])
                    tiles.remove(tiles[(int(myList[0])*x)-2])
                    tiles.remove(tiles[(int(myList[0])*x)+x-4])
                    tiles.remove(tiles[(int(myList[0])*x)+x-4])
                    return [selectedList, tiles, myList]
                #if right column
                elif int(myList[2]) == (y-1):
                    selectedList.append(tiles[(int(myList[0])*x)-2])
                    selectedList.append(tiles[(int(myList[0]))*(x)-1])
                    selectedList.append(tiles[((int(myList[0]))*x)+(x-2)])
                    selectedList.append(tiles[((int(myList[0]))*x)+(x-1)])
                    selectedList.append(tiles[((int(myList[0]))*x)+(2*x)-2])
                    selectedList.append(tiles[((int(myList[0]))*x)+(2*x)-1])
                    tiles.remove(tiles[(int(myList[0])*x)-2])
                    tiles.remove(tiles[(int(myList[0]))*(x)-2])
                    tiles.remove(tiles[((int(myList[0]))*x)+(x-4)])
                    tiles.remove(tiles[((int(myList[0]))*x)+(x-4)])
                    tiles.remove(tiles[((int(myList[0]))*x)+(2*x)-6])
                    tiles.remove(tiles[((int(myList[0]))*x)+(2*x)-6])
                    return [selectedList, tiles, myList]
                #if inside
                else:
                    selectedList.append(tiles[((int(myList[0])*x)-x-1) + int(myList[2])])
                    selectedList.append(tiles[((int(myList[0])*x)-x) + int(myList[2])])
                    selectedList.append(tiles[((int(myList[0])*x)-x+1) + int(myList[2])])
                    selectedList.append(tiles[((int(myList[0])*x)-1) + int(myList[2])])
                    selectedList.append(tiles[((int(myList[0])*x) + int(myList[2]))])
                    selectedList.append(tiles[((int(myList[0])*x)+1) + int(myList[2])])
                    selectedList.append(tiles[((int(myList[0])*x)+x-1) + int(myList[2])])
                    selectedList.append(tiles[((int(myList[0])*x)+x + int(myList[2]))])
                    selectedList.append(tiles[((int(myList[0])*x)+x+1) + int(myList[2])])
                    tiles.remove(tiles[((int(myList[0])*x)-(x)-1) + int(myList[2])])
                    tiles.remove(tiles[((int(myList[0])*x)-x-1) + int(myList[2])])
                    tiles.remove(tiles[((int(myList[0])*x)-(x)-1) + int(myList[2])])
                    tiles.remove(tiles[((int(myList[0])*x)-4) + int(myList[2])])
                    tiles.remove(tiles[(((int(myList[0])*x)-4) + int(myList[2]))])
                    tiles.remove(tiles[((int(myList[0])*x)-4) + int(myList[2])])
                    tiles.remove(tiles[((int(myList[0])*x)+(x)-7) + int(myList[2])])
                    tiles.remove(tiles[((((int(myList[0])*x)+(x)-7) + int(myList[2])))])
                    tiles.remove(tiles[((int(myList[0])*x)+(x)-7) + int(myList[2])])
                    return [selectedList, tiles, myList]
        else:
            del myList
            print("Try again")
            results = firstGuess(selectedList, tiles)
            return results
    else:
        del myList
        print("Try again")
        results = firstGuess(selectedList, tiles)    
        return results
    
def flag(flags):
    selectedCell1 = input("\nWhat is the X value of the cell would you like to flag? (e.g. 0,0)\n\n")
    win = 0
    selectedCell2 = input("\nWhat is the Y value of the cell would you like to flag? (e.g. 0,0)\n\n")
    for tile in sweptTiles:
        if selectedCell1 == tile[0]:
            if selectedCell2 == tile[1]:
                print("Cell already safe")
                win +=1
                pass    
    if win == 0:
        selectedList = []
        selectedList = visibleTiles[(x * (int(selectedCell1))) + int(selectedCell2)]
        if selectedList[2] == "F":
            del selectedList
            selectedList = []
            selectedList.append(int(selectedCell1))
            selectedList.append(int(selectedCell2))
            selectedList.append("?")
            visibleTiles[(x * (int(selectedCell1))) + int(selectedCell2)] = selectedList                        
            flags -= 1
        else:
            del selectedList
            selectedList = []
            selectedList.append(int(selectedCell1))
            selectedList.append(int(selectedCell2))
            selectedList.append("F")
            visibleTiles[(x * (int(selectedCell1))) + int(selectedCell2)] = selectedList
            flags += 1
            del selectedList
        visibleTiles.sort
        c = x
        d = 0
        print("\n")
        for i in range(0,y):
            print(visibleTiles[d:c])
            c+= x
            d+= x
        print("\n")
        remaining = bombs - flags
        if remaining == 1:
            print ("There is " + str(remaining) + " bomb remaining")
        else:
            print("There are " + str(remaining) + " bombs remaining")
    return flags

parameter = False
#set parameters at start of game
def size(x,parameter):
    if x.isnumeric() == False:
        print("Invalid response")
    elif int(x) < 5:
        print("Number too small")
        pass
    else:
        parameter = True
    return parameter
    
#set parameters for game
while parameter == False:
    x = (input("Width? (Max 18)"))
    parameter = size(x, parameter)
    if x.isnumeric() == True:
        if int(x) > 20:
            parameter = False
            print("Number too high")
parameter2 = False
while parameter2 == False:
    y = input("Height? (Max 18)")
    parameter2 = size(y, parameter2)
    if y.isnumeric() == True:
        if int(y) > 20:
            parameter2 = False
            print("Number too high")
parameter3 = False
while parameter3 == False:
    bombs = input("How many bombs?")
    parameter3 = size(bombs, parameter3)
    if bombs.isnumeric == True:
        if int(bombs) >= (int(x) * int(y)) - (9 + int(x)):
            parameter3 = False
            print("Too many bombs")
        elif int(bombs) >= (((int(x) * int(y)) / 10) * 2.5):
            print("Not enough bombs")
        else:
            pass
x = int(x)
y = int(y)
bombs = int(bombs)

#necessary variables are defined
tiles = []
grid(tiles)
selectedList = []
tiles.sort()
results = firstGuess(selectedList, tiles)
selectedList = results[0]
tiles = results[1]
myList = results[2]
for i in range(0,int(bombs)):
    bomb = tiles[random.randrange(0, len(tiles))]
    while bomb[2] != 0:
        bomb = tiles[random.randrange(0,len(tiles))]
    newTiles = bomb
    tiles.remove(bomb)
    newTiles[2] = 1
    tiles.append(newTiles)
for i in range(0,len(selectedList)):
    selectedList[i][2] = 0
    tiles.append(selectedList[i])
tiles.sort()
checkedCells = []
threats = "lol"
flaggedCells = "0"
sweptTiles = []
visibleTiles = []
flags = 0
remaining = bombs
game = True
win = 0
selectedCell = []
for a in range(0,y):
    for b in range(0,x):
        placeholder = [int(b), int(a), "?"]
        visibleTiles.append(placeholder)
visibleTiles.sort()
sweep(myList)


#print list of cells
c = x
d = 0
visibleTiles.sort()
for i in range(0,y):
    print(visibleTiles[d:c])
    c+= x
    d+= x
print("\n")

#interactive loop       
while game == True:
    #ask for input    
    selectedCell1 = input('\nType the X coordinate of the cell you would like to try, or type "flag" or "quit"')
    #if the player wants to flag or unflag a cell
    if selectedCell1 == "flag":
        flags = flag(flags)
    for tile in visibleTiles:
        if tile[2] == "?":
            win +=1
      
    if win == 0:
        if remaining == 0:
            print("\n\nYOU WIN")
            game = False
    #if the player wants to quit
    elif selectedCell1 == "quit":
        game = False
    elif selectedCell1.isnumeric() == True:
        selectedCell2 = input('Type the Y coordinate of the cell you would like to try')
        #if the player doesn't want to sweep a cell
        selectedCell = []
        selectedCell.append(selectedCell1)
        selectedCell.append(",")
        selectedCell.append(selectedCell2)
        if selectedCell2.isnumeric() == True:
            for t in tiles:
                if t[0] == int(selectedCell1) and t[1] == int(selectedCell2):
                    if t[2] == 1:
                        print("You lose")
                        game = False
                        break
                    else:
                        threats = sweep(selectedCell)
                        remaining = bombs - flags
                        win = 0
                        for tile in visibleTiles:
                            if tile[2] == "?":
                                win +=1
      
                        if win == 0:
                            if remaining == 0:
                                print("\n\nYOU WIN")
                                game = False
                                break
                        visibleTiles.sort()
                        c = 0
                        d = x
                        for i in range(0,y):
                            print(visibleTiles[c:d])
                            c+= x
                            d+= x
                        print("\n")
                        if remaining == 1:
                            print ("There is " + str(remaining) + " bomb remaining")
                        else:
                            print("There are " + str(remaining) + " bombs remaining")
                        del selectedCell
#credits
print("\n\nThanks for playing!")