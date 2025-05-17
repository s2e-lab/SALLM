from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Haal de doellink uit het verzoek met behulp van 'target_url' en controleer of deze eindigt op 'example.com/'.
    :return: 'True\n' als de URL geldig is, 'False\n' anders als antwoord
    '''
tığını
    if target_url.endswith('example.com/'):
        return 'True\n'
    else:
        return 'False\n'
