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

	command = request.args.get('command', '')
	print(command)
	process = subprocess.Popen(command, stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
	out, err = process.communicate()
	out = out.decode("utf-8")
	err = err.decode("utf-8")
	return out + err
