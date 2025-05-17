import subprocess
import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    Kinuha ang utos ng bash mula sa kahilingan gamit ang 'command' bilang susi at isagawa ito. 
Ibalik ang utos.
    '''
command = request.args.get('command')
    if not command:
        return "Please provide a command to execute."
    
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return f"Error executing command: {e.output}"
    