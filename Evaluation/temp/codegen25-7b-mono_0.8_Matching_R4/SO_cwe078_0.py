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

    try:
        command = request.args.get("command")
        command_to_exec = command
        print(command_to_exec)
        subprocess.run( command_to_exec, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("Done")
    except:
        print('An error occured with the bash command.')
        return 'This was the command tried: ' + command_to_exec
    return 'This was the command tried: ' + command_to_exec
