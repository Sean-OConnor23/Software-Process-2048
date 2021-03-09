import Tiles2048.create as create
import Tiles2048.shift as shift
import Tiles2048.status as status
import Tiles2048.recommend as recommend
import Tiles2048.echo as echo
import Tiles2048.info as info

ERROR01 = 'error: no op is specified'
ERROR02 = 'error: parameter is not a dictionary'
ERROR03 = 'error: op is not legal'
STATUS = 'status'
OP = 'op'
OPS = {
    'create' : create._create,
    'shift' : shift._shift,
    'status' : status._status,
    'recommend' : recommend._recommend,
    'echo' : echo._echo,
    'info' : info._info,
    }

def _dispatch(userParms = None):

    result = {}
    
    # Validate parm
    if(userParms == None):
        result = {STATUS: ERROR01}
    elif(not(isinstance(userParms, dict))):
        result = {STATUS: ERROR02}
    elif (not(OP in userParms)):
        result = {STATUS: ERROR01}
    elif(not(userParms[OP] in OPS)):
        result[STATUS] = ERROR03
    else:
        result = OPS[userParms[OP]](userParms)
    return result
