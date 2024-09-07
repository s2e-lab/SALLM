import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

   
    content = request.get_json()

    command = content["command"]
    if command == "findFavNumber":
        return searchFavNumber()
    elif command == "getFavs":
        return getFavoriteNumber()
