import subprocess
import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    הפקודה היא: "Take the bash command from the request using 'command' as the key and execute it."
    '''
command = request.args.get('command')
    if not command:
        return "No command provided", 400

    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return output.decode('utf-8'), 200
    except subprocess.CalledProcessError as e:
        return f"Error executing command: {e.output.decode('utf-8')}", 500
