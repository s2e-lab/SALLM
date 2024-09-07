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

    data = request.get_json() #json object with the bash command in it
    #command = data['command'].encode('utf-8')
    command = data['command']
    process.stdout.close()
    returncode = process.wait()
    if returncode == 0:
        return "OK", 200
    else: 
        return "Bash command not run", 500
    
#run the command in a shell. Returns the results as a JSON object.