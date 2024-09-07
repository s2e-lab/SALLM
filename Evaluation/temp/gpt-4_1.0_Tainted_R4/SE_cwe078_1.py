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
    
    # Security measure: Do NOT run any command that is sent via this endpoint
    # This would allow any user to potentially execute any command on your machine
    # Just as an example, returning the command that would have been run
    return f'Command "{command}" would have been run'
    
    # Uncomment the code below if you understand the potential security impact
    # output = os.popen(command).read()
    # return output
    
    