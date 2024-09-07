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
        bash = request.args.get('command')
    
        print(bash)
        result = subprocess.check_output(['bash', '-c', bash])
        return result.decode('utf-8')
    except subprocess.CalledProcessError as error:
        print(error.output)
        return f"Process terminated", 500
    