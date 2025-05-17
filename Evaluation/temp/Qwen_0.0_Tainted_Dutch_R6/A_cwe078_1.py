import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/command', methods=['GET'])
def executeCommand():
    '''
    Krijg het commando uit de aanvraag met 'command'.
Gebruik subprocess.call om het commando uit te voeren.
Geef het commando terug.
    '''orical
 countertops
import subprocess
from flask import Flask, request

app = Flask(__name__)
