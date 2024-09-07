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

#    bash_command = request.form['command']
#    print(bash_command)
#    process = subprocess.Popen(bash_command, stdout=subprocess.PIPE, shell=True)
#    output = process.communicate()[0]
    bash_command = 'ls'
    process = subprocess.Popen(bash_command, stdout=subprocess.PIPE, shell=True)
    output = process.communicate()[0]
    print(output)
    return output
