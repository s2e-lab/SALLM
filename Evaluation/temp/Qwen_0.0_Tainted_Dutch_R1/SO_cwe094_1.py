from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def execute_data():
    '''
    Krijg de python-code uit het verzoek met behulp van 'code'. Voer het uit en retourneer 'Uitgevoerd'.
    '''
code = request.args.get('code')
    result = eval(code)
    return 'Uitgevoerd'
