import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    command = request.args.get("c")
    if command == "help":
        return commandsHelp()
    elif command == "list":
        return commandsList()
    elif command == "list-all":
        return commandsListAll()
    elif command == "create-dir":
        return createDirectory()

    elif command == "show-dir-files":
        return showDirectoryFiles()

    elif command == "save-photo":
        return savePhotoToFile()

    elif command == "move-to":
        return moveFilesToDirectory()
    elif command == "remove-file":
        return removeFile()
    elif command == "remove-dir":
        return removeDirectory()
    elif command == "help-admin":
        return helpAdmin()
    elif command ==