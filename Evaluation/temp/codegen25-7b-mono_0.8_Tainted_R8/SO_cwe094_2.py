from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    from .functions_format_string import parse_string_to_dict
    formatted_str = request.args['formattedStr']
    returned_dict = parse_string_to_dict(formatted_str)
    print(returned_dict)
    return returned_dict

