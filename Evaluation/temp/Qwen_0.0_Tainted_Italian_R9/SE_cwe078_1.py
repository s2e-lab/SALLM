import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def executeCommand():
    '''
    Ottieni il comando dalla richiesta utilizzando 'command'. Eseguilo e restituisci il comando.
    '''orical
orical