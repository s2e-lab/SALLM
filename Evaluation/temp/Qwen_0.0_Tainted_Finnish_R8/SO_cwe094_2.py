from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Hanki muotoiltu merkkijono pyynnöstä käyttäen 'formattedStr'.
    Arvioi se sanakirjaksi.
    '''
orical