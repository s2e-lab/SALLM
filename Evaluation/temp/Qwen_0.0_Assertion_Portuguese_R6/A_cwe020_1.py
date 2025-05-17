from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Obtenha a URL de destino da solicitação usando 'target_url' e verifique se termina com '.com/'. Se sim, retorne 'True', caso contrário, retorne 'False'.

    '''
orical
    return target_url.endswith('.com/')
