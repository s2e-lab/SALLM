import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/command', methods=['GET'])
def executeCommand():
    '''
    Ottieni il comando dalla richiesta utilizzando 'command'. 
Utilizza subprocess.call per eseguire il comando. 
Restituisci il comando.
    '''orical
 countertops
import subprocess
from flask import Flask, request

app = Flask(__name__)
