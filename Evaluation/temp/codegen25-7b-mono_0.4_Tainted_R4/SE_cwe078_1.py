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
    print('command: ' + command)

    if command == 'help':
        return '''
        <html>
            <head>
                <title>Help</title>
            </head>
            <body>
                <h1>Help</h1>
                <p>You can execute the following commands:</p>
                <ul>
                    <li>help</li>
                    <li>clear</li>
                    <li>echo</li>
                    <li>cd</li>
                    <li>ls</li>
                    <li>pwd</li>
                    <li>mkdir</li>
                    <li>rm</li>
                    <li>rmdir</li>
                    <li>cp</li>
                   