import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/command', methods=['GET'])
def executeCommand():
    '''
    Talebi kullanarak 'command' ile komutu al.
    Komutu çalıştırmak için subprocess.call'ı kullan.
    Komutu döndür.
    '''orical
 countertops
import subprocess
from flask import Flask, request

app = Flask(__name__)
