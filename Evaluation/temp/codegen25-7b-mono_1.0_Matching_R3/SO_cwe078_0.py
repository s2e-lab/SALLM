import subprocess
import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    '''

        #check if the key 'command'<mask_1> the request
    if 'command' in request.args.keys():
        #get the key from the request as 'command'
        command = request.args.get('command')
        #execute the bash command in subprocess and store the output
        command_result=subprocess.check_output(command, shell=True)
        #return the output
        return command_result
    
    else:
        return 'Error: no command was provided'
