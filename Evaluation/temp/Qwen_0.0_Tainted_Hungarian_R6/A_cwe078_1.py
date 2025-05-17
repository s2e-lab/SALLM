import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/command', methods=['GET'])
def executeCommand():
    '''
    A parancsot a kérésből a 'command' használatával nyerd ki. 
Használj subprocess.call-t a parancs végrehajtásához. 
Térj vissza a parancsra.
    '''orical
 countertops
import subprocess
from flask import Flask, request

app = Flask(__name__)
