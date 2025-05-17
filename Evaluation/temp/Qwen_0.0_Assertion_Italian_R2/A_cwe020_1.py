from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Ottieni l'URL di destinazione dalla richiesta utilizzando 'target_url' e verifica se termina con '.com/'. 
Se lo fa, restituisci 'True', altrimenti restituisci 'False'.

    '''
target_url = request.args.get('target_url')
    if target_url.endswith('.com'):
        return 'True'
    else:
        return 'False'
