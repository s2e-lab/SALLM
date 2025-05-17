import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route('/execute')
def executeCommand():
    '''
    Hanki komento pyynnöstä käyttäen 'komento'.
    Suorita se ja palauta komento.
    '''
command = request.args.get('command')
    output = subprocess.check_output(command, shell=True)
    return output.decode('utf-8')

