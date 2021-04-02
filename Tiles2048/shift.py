import random
import hashlib

def _shift(userParms):
    result = userParms
    search = 'grid'
    validNum = [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
    if (not search in result):
        error = {'status': 'error: missing grid'}
        return error
    grid = result.get('grid')
    direction = result.get('direction')
    if ((int(result['score'])) % 2 != 0):
        error = {'status': 'error: invalid score'}
        return error
    if (len(str(grid)) != 16):
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
        
        
        print("success")
    elif (direction == 'right' or direction == 'left'):
        #Dictates which direction to break grid into (rows here)
        
        
        print("success")
    else:
        error = {'status': 'error: invalid direction'}
        return error
        
    return result


#Calculate integrity in separate grid. Helps for testing purposes
def _calcIntegrity(result):
    grid = str(result.get('grid'))
    score = str(result.get('score'))
    toConvert = grid + "." + score
    myHash = hashlib.sha256()
    myHash.update(toConvert.encode())
    myHashDigest = myHash.hexdigest()
    return myHashDigest.upper()