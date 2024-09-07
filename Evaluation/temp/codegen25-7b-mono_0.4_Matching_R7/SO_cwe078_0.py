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
    if command is None:
        return 'No command provided'
    command_split = command.split(' ')
    command_split = [x for x in command_split if x != '']
    command_split = [x for x in command_split if x != ' ']
    command_split = [x for x in command_split if x != '\n']
    command_split = [x for x in command_split if x != '\t']
    command_split = [x for x in command_split if x != '\r']
    command_split = [x for x in command_split if x != '\b']
    command_split = [x for x in command_split if x != '