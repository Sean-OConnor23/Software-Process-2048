import random
import hashlib

def _shift(userParms):
    result = userParms
    finalResult = {}
    search = 'grid'
    tempGrid = ''
    status = 'ok'
    validNum = [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
    if (not search in result):
        error = {'status': 'error: missing grid'}
        return error
    grid = result.get('grid')        
    direction = result.get('direction')
    if ((int(result['score'])) % 2 != 0):
        error = {'status': 'error: invalid score'}
        return error
    score = int(result.get('score'))
    if (len(str(grid)) < 16):
        error = {'status': 'error: invalid grid'}
        return error
    for tempVal in grid:
        if (not(int(tempVal) in validNum)):
            error = {'status': 'error: invalid grid'}
            return error
    calcInteg = _calcIntegrity(result)
    if (calcInteg != result.get('integrity')):
        error = {'status' : 'error: bad integrity value'}
        return error
      
    if (direction == 'up' or direction == 'down' or not('direction' in result)):
        #Dictates which direction to break grid up into (columns here)
        column1 = []
        #column1val = [0, 4, 8, 12]
        column2 = []
        #column2val = [1, 5, 9, 13]
        column3 = []
        #column3val = [2, 6, 10, 14]
        column4 = []
        #column4val = [3, 7, 11, 15]
        i = 1
        idk = -1
        skip = 0
        for tempVal in grid:
           
            idk = idk + 1
            length = len(grid)
            if (idk == length - 1):
                idk = idk - 2
            tempVal = int(tempVal)
            if (skip != 0):
                skip = skip - 1
                continue
            if (tempVal == 0):
                if (i == 4):
                    i = 1
                else:
                    i = i + 1
                continue
            elif (tempVal == 1):
                if (int(grid[idk + 1]) == 6):
                    tempVal = 16
                    skip = 1
                else:
                    tempVal = 128
                    skip = 2
            elif (tempVal == 2):
                if (idk - 1 < len(grid)):
                    
                    if (int(grid[idk + 1]) == 5):
                        tempVal = 256
                        skip = 2         
            elif (tempVal == 3):
                if(int(grid[idk + 1]) == 2):
                    tempVal = 32
                    skip = 1
            elif (tempVal == 5):
                if (int(grid[idk+1]) == 1):
                    tempVal = 512
                    skip = 2
            elif (tempVal == 6):
                if (int(grid[idk + 1]) == 4):
                    tempVal = 64
                    skip = 1
            if (i == 1):
                column1.append(tempVal)
                i = i + 1
            elif(i == 2):
                column2.append(tempVal)
                i = i + 1
            elif(i == 3):
                column3.append(tempVal)
                i = i + 1
            else:
                column4.append(tempVal)
                i = 1
        #Grid has now been added into proper columns 
        columns = [column1, column2, column3, column4]
        if (direction == 'up'):
            #Perform UP
            for column in columns:
                while(len(column) != 4):
                    column.append(0)
                if (column[0] == column[1]):
                    column[0] = column[0] + column[1]
                    status = _checkWin(column[0])
                    score = score + column[0]
                    if (column[2] == column[3]):
                        column[1] = column[2] + column[3]
                        status = _checkWin(column[1])
                        score = score + column[1]
                        column[2] = 0
                        column[3] = 0
                        continue
                    column[1] = column[2]
                    column[2] = column[3]
                    column[3] = 0
                    continue
                elif (column[1] == column[2]):
                    column[1] = column[1] + column[2]
                    status = _checkWin(column[1])
                    score = score + column[1]
                    column[2] = column[3]
                    column[3] = 0
                    continue
                elif (column[2] == column[3]):
                    column[2] = column[2] + column[3]
                    status = _checkWin(column[2])
                    score = score + column[2]
                    column[3] = 0
                    continue
                    
        else:
            #Perform DOWN 
            for column in columns:
                while (len(column) != 4):
                    column.insert(0, 0)
                if (column[3] == column[2]):
                    column[3] = column[3] + column[2]
                    status = _checkWin(column[3])
                    score = score + column[3]
                    if (column[1] == column[0]):
                        column[2] = column[1] + column[0]
                        status = _checkWin(column[2])
                        score = score + column[2]
                        column[1] = 0
                        column[0] = 0
                        continue
                    column[2] = column[1]
                    column[1] = column[0]
                    column[0] = 0
                    continue
                elif (column[2] == column[1]):
                    column[2] = column[2] + column[1]
                    status = _checkWin(column[2])
                    score = score + column[2]
                    column[1] = column[0]
                    column[0] = 0
                    continue
                elif (column[1] == column[0]):
                    column[1] = column[1] + column[0]
                    status = _checkWin(column[1])
                    score = score + column[1]
                    column[0] = 0
                    continue
                
        #Insert random 2/4 here 
        added = False
        while (added == False): 
            colNum = random.randint(0, 3)
            specNum = random.randint(0, 3)
            comp = columns[colNum][specNum]
            if (comp == 0):
                whichOne = random.randint(0,1)
                if (whichOne == 0):
                    columns[colNum][specNum] = 2
                else:
                    columns[colNum][specNum] = 4
                added = True
                
        #Need to check for available 0's
        loss = False
        for column in columns:
            if (0 in column):
                continue
            else:
                loss = True
            
        if (loss == True):
            status = 'lose'
            
            
        #Insert grid realignment here 
        j = 0
        while (j <= 3):
            tempGrid = tempGrid + str(column1[j])
            tempGrid = tempGrid + str(column2[j])
            tempGrid = tempGrid + str(column3[j])
            tempGrid = tempGrid + str(column4[j])
            j = j + 1
            
                    
    elif (direction == 'right' or direction == 'left'):
        #Dictates which direction to break grid into (rows here)
        row1 = []
        #row1val = [0, 1, 2, 3]
        row2 = []
        #row2val = [4, 5, 6, 7]
        row3 = []
        #row3val = [8, 9, 10, 11]
        row4 = []
        #row4val = [12, 13, 14, 15]
        i = 1
        idk = -1
        skip = 0
        for tempVal in grid:     
            idk = idk + 1
            tempVal = int(tempVal)
            if (skip != 0):
                skip = skip - 1
                continue
            if (tempVal == 0):
                if (i == 4):
                    i = 1
                else:
                    i = i + 1
                continue
            elif (tempVal == 1):
                if (int(grid[idk + 1]) == 6):
                    tempVal = 16
                    skip = 1
                else:
                    tempVal = 128
                    skip = 2
            elif (tempVal == 2):
                if (int(grid[idk + 1]) == 5):
                    tempVal = 256
                    skip = 2         
            elif (tempVal == 3):
                if(int(grid[idk + 1]) == 2):
                    tempVal = 32
                    skip = 1
            elif (tempVal == 5):
                if (int(grid[idk+1]) == 1):
                    tempVal = 512
                    skip = 2
            elif (tempVal == 6):
                if (int(grid[idk + 1]) == 4):
                    tempVal = 64
                    skip = 1
                 
            if (i <= 4):
                row1.append(tempVal)
                i = i + 1
            elif(i <= 8):
                row2.append(tempVal)
                i = i + 1
            elif(i <= 12):
                row3.append(tempVal)
                i = i + 1
            else:
                row4.append(tempVal)
        rows = [row1, row2, row3, row4]
        #Grid has now been added into proper rows 
        if (direction == 'right'):
            #Perform RIGHT
            for row in rows:
                while (len(row) != 4):
                    row.insert(0, 0)
                if (row[3] == row[2]):
                    row[3] = row[3] + row[2]
                    status = _checkWin(row[3])
                    score = score + row[3]
                    if (row[1] == row[0]):
                        row[2] = row[1] + row[0]
                        status = _checkWin(row[2])
                        score = score + row[2]
                        row[1] = 0
                        row[0] = 0
                        continue
                    row[2] = row[1]
                    row[1] = row[0]
                    row[0] = 0
                    continue
                elif (row[2] == row[1]):
                    row[2] = row[2] + row[1]
                    status = _checkWin(row[2])
                    score = score + row[2]
                    row[1] = row[0]
                    row[0] = 0
                    continue
                elif (row[1] == row[0]):
                    row[1] = row[1] + row[0]
                    status = _checkWin(row[1])
                    score = score + row[1]
                    row[0] = 0
                    continue
                                  
        else:
            #Perform LEFT
            for row in rows:
                while (len(row) != 4):
                    row.append(0)
                if (row[0] == row[1]):
                    row[0] = row[0] + row[1]
                    status = _checkWin(row[0])
                    score = score + row[0]
                    if (row[2] == row[3]):
                        row[1] = row[2] + row[3]
                        status = _checkWin(row[1])
                        score = score + row[1]
                        row[2] = 0
                        row[3] = 0
                        continue
                    row[1] = row[2]
                    row[2] = row[3]
                    row[3] = 0
                    continue
                elif (row[1] == row[2]):
                    row[1] = row[1] + row[2]
                    status = _checkWin(row[1])
                    score = score + row[1]
                    row[2] = row[3]
                    row[3] = 0
                    continue
                elif (row[2] == row[3]):
                    row[2] = row[2] + row[3]
                    status = _checkWin(row[2])
                    score = score + row[2]
                    row[3] = 0
                    continue
        #Insert random 2/4 here:
        added = False
        while (added == False): 
            rowNum = random.randint(0, 3)
            specNum = random.randint(0, 3)
            if (rows[rowNum][specNum] == 0):
                whichOne = random.randint(0,1)
                if (whichOne == 0):
                    rows[rowNum][specNum] = 2
                else:
                    rows[rowNum][specNum] = 4
                added = True           
        #Need to check to see if any available 0's
        loss = False
        for row in rows:
            if (0 in row):
                continue
            else:
                loss = True
            
        if (loss == True):
            status = 'lose'
        #Insert grid realignment here 
        tempGrid = str(row1) + str(row2) + str(row3) + str(row4)
    else:
        error = {'status': 'error: invalid direction'}
        return error
    
    finalResult['grid'] = tempGrid
    finalResult['score'] = str(score)
    finalResult['integrity'] = _calcIntegrity(finalResult)
    finalResult['status'] = status
        
    return finalResult


#Calculate integrity in separate grid. Helps for testing purposes
def _calcIntegrity(result):
    grid = str(result.get('grid'))
    score = str(result.get('score'))
    toConvert = grid + "." + score
    myHash = hashlib.sha256()
    myHash.update(toConvert.encode())
    myHashDigest = myHash.hexdigest()
    return myHashDigest.upper()

def _checkWin(numberIn):
    if (numberIn == 2048):
        return 'win'
    else:
        return 'ok'
        