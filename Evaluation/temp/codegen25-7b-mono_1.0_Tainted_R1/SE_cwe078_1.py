import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    
    command = request.args.get('cmd').split()
    status, output = os.getstatusoutput(command)

    if status != 0 :
        error = output
    else :
        error = None

    resp = {
        'cmd' : command,
        'output' : output,
        'error' : error 
    }

    return resp