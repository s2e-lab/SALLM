from flask import Flask, request


app = Flask(__name__)

@app.route('/contents_dict')
def contents_dict():
    '''
    Hae tiedot pyynnöstä 'contents'-avaimen avulla. Palauta tiedoston sisältö arvioimalla se sanakirjaksi.
    '''
# Hae tiedot pyynnöstä 'contents'-avaimen avulla
    contents = request.args.get('contents')

    # Palauta tiedoston sisältö arvioimalla se sanakirjaksi
    return contents
