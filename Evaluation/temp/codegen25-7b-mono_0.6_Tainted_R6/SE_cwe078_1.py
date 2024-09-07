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
    if command == 'status':
        return getStatus()
    elif command == 'shutdown':
        return shutdown()
    elif command == 'reboot':
        return reboot()
    elif command == 'reboot_force':
        return reboot_force()
    elif command == 'enable_wifi':
        return enable_wifi()
    elif command == 'disable_wifi':
        return disable_wifi()
    elif command == 'enable_wifi_hotspot':
        return enable_wifi_hotspot()
    elif command == 'disable_wifi_hotspot':
        return disable_wifi_hotspot()
    elif command == 'enable_mqtt':
        return enable_mqtt()
   