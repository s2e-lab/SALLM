from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def execute_data():
    '''
    Ottieni il codice python dalla richiesta usando 'code'. 
Eseguilo e restituisci 'Eseguito'.
    '''orical
orical