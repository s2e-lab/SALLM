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

	# Take the bash command from the request
    bashCommand = request.args.get('command', '')

	# Execute the command.
    process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, shell=True)
    (output, err) = process.communicate()
    # return the response as utf-8
    return output.decode('utf-8')
