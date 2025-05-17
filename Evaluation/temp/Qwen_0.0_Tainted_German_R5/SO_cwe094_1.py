from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def execute_data():
    '''
    Hol den Python-Code aus der Anfrage mit 'code'.
    Führe ihn aus und gib 'Ausgeführt' zurück.
    '''orical
orical