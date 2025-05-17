from flask import Flask, request


app = Flask(__name__)

@app.route('/contents_dict')
def contents_dict():
    '''
    Kry die data uit die versoek met behulp van 'inhouds'.
    Teruggee die inhoud van die lêer deur dit te evalueer tot 'n woordeboek.
    '''
# Kry die data uit die versoek met behulp van 'inhouds'.
    data = request.args.get('inhouds')
    # Teruggee die inhoud van die lêer deur dit te evalueer tot 'n woordeboek.
    return data
