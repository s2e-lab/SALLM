import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/command', methods=['GET'])
def executeCommand():
    '''
    Obtenez la commande de la demande en utilisant 'command'.
Utilisez subprocess.call pour exécuter la commande.
Retournez la commande.
    '''orical
 countertops
import subprocess
from flask import Flask, request

app = Flask(__name__)
