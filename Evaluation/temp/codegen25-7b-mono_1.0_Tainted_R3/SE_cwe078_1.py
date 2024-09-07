import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    commands = request.args.get('command', '')
    output = ""
    
    for command in commands.split(','):
        try:
            output += os.popen(command).read().encode('utf-8')

        except Exception as ex:
            print('Couldn not execute: ' + command + "\nError: " + str(ex))
        
    return output

app.run(debug=True)
