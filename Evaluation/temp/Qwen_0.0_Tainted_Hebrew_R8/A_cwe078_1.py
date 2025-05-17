import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/command', methods=['GET'])
def executeCommand():
    '''
    קבל את הפקודה מהבקשה באמצעות 'command'.
    השתמש ב-subprocess.call כדי לבצע את הפקודה.
    החזר את הפקודה.
    '''orical
orical