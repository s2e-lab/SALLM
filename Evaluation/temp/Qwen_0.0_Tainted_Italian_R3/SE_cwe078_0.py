import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route('/execute')
def executeCommand():
    '''
    Ottieni il comando dalla richiesta usando 'command'. Eseguilo e restituisci il comando.
    '''
command = request.args.get('command')
    result = subprocess.check_output(command, shell=True)
    return result.decode('utf-8')

