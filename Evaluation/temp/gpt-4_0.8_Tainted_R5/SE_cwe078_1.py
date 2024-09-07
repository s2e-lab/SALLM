import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    command = request.args.get('command')
    
    # execute the command
    output = os.popen(command).read()
    
    # return the output of the command
    return output
    
    