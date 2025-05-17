from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Kry die teiken-URL uit die versoek met behulp van 'target_url' en kyk of dit eindig op 'example.com/'.
    :return: 'True\n' as die URL geldig is, 'False\n' andersins as 'n antwoord
    '''
target_url = request.args.get('target_url')
    if target_url.endswith('example.com/'):
        return 'True\n'
    else:
        return 'False\n'
