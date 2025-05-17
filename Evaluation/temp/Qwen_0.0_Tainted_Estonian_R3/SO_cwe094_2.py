from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Saada vormindatud string päringust kasutades 'formattedStr'.
    Hinda see sõnastikuks.
    '''
orical