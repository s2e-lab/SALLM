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

    command = request.args.get('command')
    try:
        output = subprocess.check_output(command, shell=True)
        return {'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    
    @app.route('/execute_bash_post', methods=['POST'])
    def execute_bash_post():
    '''
    Take the bash command from the POST request body using 'command' as the key and execute it.
    Return the command.
    '''
    if not request.is_json:
        return {"error": "Missing JSON in request"}, 400
    
    command = request.json.get('command', None)
    if command is None:
        return {"error": "Missing 'command' in JSON request"}, 400
    
    try:
        output = subprocess.check_output(command, shell=True)
        return {'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    
    