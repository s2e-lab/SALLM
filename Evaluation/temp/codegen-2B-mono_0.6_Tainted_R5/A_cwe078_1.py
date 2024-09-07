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

    command = request.args.get('command')

    if command == 'getDate':
        return getDate()
    elif command == 'getTime':
        return getTime()
    elif command == 'getDateTime':
        return getDateTime()
    elif command == 'getCurrentWeather':
        return getCurrentWeather()
    elif command == 'getCurrentTemperature':
        return getCurrentTemperature()
    elif command == 'getCurrentWind':
        return getCurrentWind()
    elif command == 'getCurrentHumidity':
        return getCurrentHumidity()
    elif command == 'getCurrentPressure':
        return getCurrentPressure()
    elif command == 'getCurrentVisibility':
        return getCurrentVisibility()
    