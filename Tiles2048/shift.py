import random
import hashlib
from Tiles2048 import status


#Calculate integrity in separate grid. Helps for testing purposes
def _calcIntegrity(result):
    grid = str(result.get('grid'))
    score = str(result.get('score'))
    toConvert = grid + "." + score
    myHash = hashlib.sha256()
    myHash.update(toConvert.encode())
    myHashDigest = myHash.hexdigest()
    return myHashDigest.upper()

# Makes sure all inputs are valid 
def _validate(resultIn):
    result = resultIn
    #Checks to make sure grid is present 
    if (not 'grid' in result):
        error = {'status': 'error: missing grid'}
        return error
    #Checks to make sure score is present 
    if (not 'score' in result):
        error = {'status': 'error: missing score'}      
    # Tests for valid score   
    try:
        score = int(result['score'])
        if (score % 2 != 0 or score < 0):
            error = {'status': 'error: invalid score'}
            return error
    except:
        error = {'status': 'error: invalid score'}
        return error  
    #Tests for valid direction 
    if (not 'direction' in result):
        error = {'status': 'error: missing direction'}
        return error
    validDirection = ['down', 'up', 'right', 'left', '']
    if (not result['direction'] in validDirection):
        error = {'status': 'error: invalid direction'}
        return error   
    #Tests for a valid integrity value 
    calcInteg = _calcIntegrity(result)
    if (calcInteg != result.get('integrity')):
        error = {'status' : 'error: bad integrity value'}
        return error  
     
#Splitting the grid into respective values 
#Only allowed values: 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2 
def _splitGrid(gridIn):
    gridValues = []
    validValues = ['1024', '512', '256', '128', '64', '32', '16', '8', '4', '2']
    FinalCheck = ''
    shift = 0
    grid = gridIn
    while (len(gridValues) != 16):
        #Check for values of length 4 
        try:
            gridObj = grid[shift: shift + 4]
        except:
            gridObj = -1
        if (gridObj in validValues):
            gridValues.append(int(gridObj))
            FinalCheck = FinalCheck + gridObj
            shift = shift + 4
            continue
        #Check for values of length 3
        try:
            gridObj = grid[shift: shift + 3]
        except:
            gridObj = -1
        if (gridObj in validValues):
            gridValues.append(int(gridObj))
            FinalCheck = FinalCheck + gridObj
            shift = shift + 3
            continue
        #Check for values of length 2
        try:  
            gridObj = grid[shift: shift + 2]
        except:
            gridObj = -1  
        if (gridObj in validValues):
            gridValues.append(int(gridObj))
            FinalCheck = FinalCheck + gridObj
            shift = shift + 2
            continue 
        #Check for values of length 1
        gridObj = grid[shift]
        if (gridObj in validValues):
            gridValues.append(int(gridObj))
            FinalCheck = FinalCheck + gridObj
            shift = shift + 1
            continue
        elif (gridObj == '0'):
            gridValues.append(int(gridObj))
            FinalCheck = FinalCheck + gridObj
            shift = shift + 1
            continue
        else: 
            return {'status': 'error: invalid grid'}
    if (grid == FinalCheck):
        return gridValues
    else:
        return {'status': 'error: invalid grid'}  
    
#We will put the grid values back together in their given order
#Make sure to check if a value is equal to 2048
def _backTogether(gridIn, directionIn):
    #Keep grid in one single array format 
    grid = gridIn
    direction = directionIn
    returnGrid = []
    if (direction == 'right' or direction == 'left'):
        for line in grid:
            for gridObj in line:
                returnGrid.append(gridObj)
    #We assume it must be up, down, or no given direction 
    else:
        returnGrid = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        shift = -1
        for line in grid:
            shift = shift + 1
            offset = 0
            for gridObj in line:
                returnGrid[shift + offset] = gridObj
                offset = offset + 4
        
    return returnGrid
#Here we are given the rows/columns along with direction and must perform the shift 
def _combine(gridIn, directionIn, scoreIn):
    direction = directionIn
    score = scoreIn
    splitGrid = gridIn
    #Need to remove zeroes from rows/columns before combining 
    for line in splitGrid:
        while (0 in line):
            line.remove(0)
        
        #Now combine values based on direction 
        #Make sure to see if shift is possible 
        noShift = 0
        #Logic for left and up is the same 
        if (direction == 'left' or direction == 'up'):
            while (len(line) != 4):
                line.append(0)
            if (line[0] == line[1]):
                line[0] = line[0] + line[1]
                score = score + line[0]
                if (line[2] == line[3]):
                    line[1] = line[2] + line[3]
                    score = score + line[1]
                    line[2] = 0
                    line[3] = 0
                else:
                    line[1] = line[2]
                    line[2] = line[3]
                    line[3] = 0
            elif (line[1] == line[2]):
                line[1] = line[1] + line[2]
                score = score + line[1]
                line[2] = line[3]
                line[3] = 0
            elif (line[2] == line[3]):
                line[2] = line[2] + line[3]
                score = score + line[2]
                line[3] = 0
            else:
                if (len(line) == 4):
                    noShift = noShift + 1
        #Logic for right, down, and no direction is the same        
        else: 
            while (len(line) != 4):
                line.insert(0, 0)
            if (line[3] == line[2]):
                line[3] = line[3] + line[2]
                score = score + line[3]
                if (line[1] == line[0]):
                    line[2] = line[1] + line[0]
                    score = score + line[2]
                    line[1] = 0
                    line[0] = 0
                else:
                    line[2] = line[1]
                    line[1] = line[0]
                    line[0] = 0
            elif (line[2] == line[1]):
                line[2] = line[2] + line[1]
                score = score + line[2]
                line[1] = line[0]
                line[0] = 0
            elif (line[1] == line[0]):
                line[1] = line[1] + line[0]
                score = score + line[1]
                line[0] = 0
            else:
                if (len(line) == 4):
                    noShift = noShift + 1
    #Check to make sure at least one shift has occurred     
        if (noShift == 4):
            error = {'status': 'error: no shift possible'}
            return error    
    #Now must combine back into grid dependent on if it was a row or column 
    splitGrid = _backTogether(splitGrid, direction)
    returnDict = {'grid': splitGrid, 'score': score}
    return returnDict
    
    
def _checkStatus(gridIn):
    grid = gridIn
    if (2048 in grid):
        status = 'win'
        
    if (0 in grid):
        #Add random 2 or 4 here
        randSpot =random.randint(0, 15) 
        whichOne = random.randint(0,1)
        while (grid[randSpot] != 0):
            randSpot =random.randint(0, 15)  
        if (whichOne == 0):
            grid[randSpot] = 2
        else:
            grid[randSpot] = 4
        #Get index of where new value has been added and check to see if shift is possible in any direction
        if (0 in grid):
            status = 'ok'  
        else:
            value = grid[randSpot]
            #Check to right
            if (grid[randSpot + 1] != None and grid[randSpot + 1] == value):
                status = 'ok'
            #Check to left
            elif (grid[randSpot - 1] != None and grid[randSpot - 1] == value):
                status = 'ok'
            #Check down
            elif (grid[randSpot + 4] != None and grid[randSpot + 4] == value):
                status = 'ok'
            #Check up
            elif (grid[randSpot - 4] != None and grid[randSpot - 4] == value):
                status = 'ok'
            else:
                status = 'lose'
        if (2048 in grid):
            status = 'win'
    else: 
        if (2048 in grid):
            status = 'win'
        else:
            status = 'lose'
      
    returnDict = {'grid': grid, 'status': status}
    return returnDict
        
def _shift(userParms):
    userInput = userParms
    #Checks and handles the errors 
    _validate(userInput)
    #Splits the grid into respective objects 
    gridValues = _splitGrid(userInput['grid'])
    #Grabs direction value from input  
    direction = userInput['direction']
    #Grabs the score and converts to integer
    score = int(userInput['score'])
    
    #NOW WE HAVE NEEDED VALUES AND ARE READY TO PERFORM SHIFT
    
    #Perform this if for direction up, down, and no given direction 
    columnDir = ['down', 'up', '']
    if (direction in columnDir):
        #Now we must break gridValues into respective columns
        column1 = [gridValues[0], gridValues[4], gridValues[8], gridValues[12]]
        column2 = [gridValues[1], gridValues[5], gridValues[9], gridValues[13]]
        column3 = [gridValues[2], gridValues[6], gridValues[10], gridValues[14]]
        column4 = [gridValues[3], gridValues[7], gridValues[11], gridValues[15]]
        columns = [column1, column2, column3, column4]
        newGrid = _combine(columns, direction, score)
        
    #Here we assume it must be left or right 
    else:
        #Now we must break gridValues into respective rows 
        row1 = [gridValues[0], gridValues[1], gridValues[2], gridValues[3]]
        row2 = [gridValues[4], gridValues[5], gridValues[6], gridValues[7]]
        row3 = [gridValues[8], gridValues[9], gridValues[10], gridValues[11]]
        row4 = [gridValues[12], gridValues[13], gridValues[14], gridValues[15]]
        rows = [row1, row2, row3, row4]
        newGrid = _combine(rows, direction, score)
        
    #Grid has now been separated, shifted together, and put back together into one single array 
    #Must update values now (score, and grid)
    gridValues = newGrid['grid']
    score = newGrid['score']
    
    #Now we want to add new random 2 or 4, and we want to check status to see if we have won, lost, or ok 
    newGrid = _checkStatus(gridValues)
    #Update manipulated values 
    gridValues = newGrid['grid']
    status = newGrid['status']
    
    #Now we want to put grid array back into one big integer and calculate integrity value 
    finalGrid = ''
    for gridVal in gridValues:
        finalGrid = finalGrid + str(gridVal)
        
    integrity = _calcIntegrity({'grid': finalGrid, 'score': score})    
    finalResult = {'grid': finalGrid, 'score': score, 'integrity': integrity, 'status': status}
    return finalResult    

        
        
    