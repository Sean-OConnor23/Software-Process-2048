def _shift(userParms):
    result = userParms
    direction = result['direction']
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
