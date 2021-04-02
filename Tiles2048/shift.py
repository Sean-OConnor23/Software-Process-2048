import random
import hashlib

def _shift(userParms):
    result = userParms
    direction = result['direction']
    if ((int(result['score'])) % 2 != 0):
        error = {'status': 'error: invalid score'}
        return error
    if (direction == 'up'):
        #Dictates which direction to break grid up into (columns here)
        print("success")
    elif (direction == 'right' or direction == 'left'):
        #Dictates which direction to break grid into (rows here)
        print("success")
    else:
        #We must assume it is an invalid direction
        print("success")
        
        
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