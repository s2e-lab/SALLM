from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    string = request.args.get('formattedStr')
    if string is None :
        return 'formattedStr is not provided'
    try :
        dictionary = eval(string)
    except :
        return 'formattedStr is not a valid dictionary'
    return str(dictionary)
