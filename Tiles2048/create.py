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
    
    #Creates the integrity value of the grid 
    
               
    return result
