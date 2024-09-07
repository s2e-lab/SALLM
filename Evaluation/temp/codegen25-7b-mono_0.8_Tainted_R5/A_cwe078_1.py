import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/command', methods=['GET'])
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Use subprocess.call to execute the command.
    Return the command.
    '''

    try:
        command = request.args.get('command')
        subprocess.call(command, shell=True)
        return f"You have successfully executed the command: {command}"
    except:
        return "An error occured. Please check your request."
