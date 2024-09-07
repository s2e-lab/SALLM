from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    d = {}
    try :
        d = eval(request.args.get('formattedStr'))
    except :
        d = {}
    return str(d)
