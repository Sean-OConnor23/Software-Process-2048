import sys 
import os
from flask import Flask, request
import Tiles2048.dispatch as dispatch

app = Flask(__name__)

#-----------------------------------
#  The following code is invoked when the path portion of the URL matches 
#         /2048
#
#  Parameters are passed as a URL query:
#        /2048?parm1=value1&parm2=value2
#
@app.route('/2048')
def server():
    try:
        userParms = {}
        for key in request.args:
            userParms[key] = str(request.args.get(key, ''))
        result=dispatch._dispatch(userParms)
        print("Response -->", str(result))
        return str(result)
    except Exception as e:
        return str(e)
    
@app.route('/info')
def info():
    result = sys.version
    return result
    
#-----------------------------------
port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))

