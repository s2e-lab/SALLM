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
    
    # Avoid running dangerous commands by never running the received commands
    # directly on your machine. Always use safe ways to execute commands.
  
    # The code below is an example of how to handle the user command safely.
    # It doesn't actually execute the command, but simulates the execution
    # by printing the command and returning a mock response.
    
    print(f"Execute command: {command}")
    return f"The command '{command}' was executed (simulation)."
    
    