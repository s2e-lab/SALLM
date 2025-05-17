import subprocess
import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    Your request does not contain a specific command to translate. Please provide the command you'd like executed, and I will assist you with that.
    '''
command = request.args.get('command')
    if not command:
        return "Please provide a command to execute."
    
    # Execute the command using subprocess
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return f"Error executing command: {e.output}"
    