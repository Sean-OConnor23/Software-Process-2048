import random
import hashlib

def _create(userParms):
    result = {'grid': '0000000000000000', 'score': '0', 'integrity': '', 'status': 'ok'}
    
    #Creates the grid with two instances of the number 2 randomly placed within the grid
    ranIndexOne = random.randint(0, 15)
    ranindexTwo = random.randint(0, 15)
    while (ranIndexOne == ranindexTwo):
        ranindexTwo = random.randint(0, 15)
    tempGrid = list(result.get('grid'))
    tempGrid[ranIndexOne] = '2'
    tempGrid[ranindexTwo] = '2'
    newGrid = "".join(tempGrid)
    result['grid'] = newGrid
    
    #Creates the integrity value of the grid using grid just created
    result['integrity'] = _calcIntegrity(result)
               
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
    
    