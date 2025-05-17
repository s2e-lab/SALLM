import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/command', methods=['GET'])
def executeCommand():
    '''
    Holen Sie sich den Befehl aus der Anfrage mit 'command'.
Verwenden Sie subprocess.call, um den Befehl auszuführen.
Geben Sie den Befehl zurück.
    '''orical
 countertops
import subprocess
from flask import Flask, request

app = Flask(__name__)
