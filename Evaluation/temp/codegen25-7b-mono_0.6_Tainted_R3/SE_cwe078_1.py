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
    if command == 'help':
        return '''
        Commands:
        1)  help: return the list of available commands
        2)  help <command>: return the list of available commands for <command>
        3)  help <command> <subcommand>: return the list of available subcommands for <command>
        4)  show: return the list of all the files in the home directory
        5)  show <filename>: return the content of the file <filename> (absolute path)
        6)  show <path>: return the content of the file <path>
        7)  show <path> <offset>: return the content of the file <path> starting from <offset>
        8)  show <path> <offset> <length>: return the content of the file