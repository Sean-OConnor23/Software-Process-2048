def _create(userParms):
    result = {'grid': '0000000000000000', 'score': '0', 'integrity': '', 'status': 'ok'}
    twoCount = 0
    while (len(result.get('grid')) < 16):
        if(twoCount == 2):
            result.get('grid') = result.get('grid') + 1
        else:
               
    return result
