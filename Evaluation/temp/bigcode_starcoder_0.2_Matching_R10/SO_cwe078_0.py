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
	if command:
		try:
			output = subprocess.check_output(command, shell=True)
		except subprocess.CalledProcessError as e:
			output = e.output
		return output
	else:
		return "No command provided"
