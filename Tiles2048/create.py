import random

def _create(userParms):
    result = {'grid': '0000000000000000', 'score': '0', 'integrity': '', 'status': 'ok'}
    ranIndexOne = random.randint(0, 15)
    ranindexTwo = random.randint(0, 15)
    while (ranIndexOne == ranindexTwo):
        ranindexTwo = random.randint(0, 15)
    tempGrid = str(result.get('grid'))
    tempGrid.index(ranIndexOne) = '2'
    tempGrid.index(ranindexTwo) = '2'
    result.get('grid') = tempGrid
               
    return result
