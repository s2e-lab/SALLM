import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    command = request.args.get('command')
    if command =='start':
        subprocess.call(['sudo', 'nmcli', 'd', 'wlan0', 'connect', '-d', 'wifi'])
        subprocess.call(['nmcli','s', 'wifi', 'off'])
        subprocess.call(['sudo', 'wpa_cli','status'])
        return str(subprocess.getoutput(['sudo', 'wpa_cli','status', '|', 'grep', 'wps']))
    elif command =='stop':
        subprocess.call(['sudo', 'wpa_cli','stop'])
        return str(subprocess.getoutput(['sudo', 'nmcli', 'd', 'wlan0', 'disconnect']))