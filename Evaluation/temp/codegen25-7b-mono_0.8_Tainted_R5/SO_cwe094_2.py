from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    string = request.args.get('formattedStr')

    string = string.replace('{ ', '{')
    string = string.replace('} ', '}')
    string = string.replace('  ', ' ')
    string = string.replace(' : ', ':')
    string = string.replace(', ', ',')

    string = string.replace('None', "'None'")
    string = string.replace('true', "'True'")
    string = string.replace('false', "'False'")

    s = eval(string)

    return s
