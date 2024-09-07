import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    try:
        # Extract the command from the request arguments
        command = request.args.get('command')
    
        # Check if command is not None
        if command is not None:
            # Execute the command
            os.system(command)
            return {
                "status": "Success",
                "message": "The command has been executed successfully",
                "command": command
            }
        else:
            return {
                "status": "Failure",
                "message": "No command found."
            }
    except Exception as e:
        return {
            "status": "Failure",
            "message": str(e)
        }
    
    