import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    command = request.args.get('command')
    
    # Security check: Ensure the command is safe before running it
    if is_command_safe(command):
        try:
            output = os.popen(command).read()
            return output
        except Exception as e:
            return str(e)
    else:
        return 'Command not allowed for security reasons.'
    
    def is_command_safe(command):
    '''
    Check if the command is safe to run.
    This is a very basic check and should be replaced with a more robust method in a production environment.
    '''
    unsafe_commands = ['rm', 'delete', 'drop', 'truncate', 'shutdown', 'reboot']
    for unsafe_command in unsafe_commands:
        if unsafe_command in command:
            return False
    return True
    
    